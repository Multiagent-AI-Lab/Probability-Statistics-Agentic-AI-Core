"""Tests for _llm_backend.llamar_juez_semantico.

Ningún test hace red real: todos mockean el cliente/SDK subyacente,
mismo patrón que tests/test_stats_tutor_agent.py con GEMINI_API_KEY.
"""

import os
from unittest.mock import MagicMock, patch

import pytest

from src.multiagent_core.council._llm_backend import llamar_juez_semantico


def test_backend_desconocido_lanza_value_error_sin_red():
    with pytest.raises(ValueError, match="backend desconocido"):
        llamar_juez_semantico("prompt de prueba", backend="modelo-inventado")


def test_default_backend_es_gemini_si_no_hay_variable_de_entorno():
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"}, clear=False):
        os.environ.pop("SEMANTIC_JUDGE_BACKEND", None)
        with patch(
            "src.multiagent_core.council._llm_backend._via_gemini",
            return_value="respuesta gemini",
        ) as mock_gemini:
            resultado = llamar_juez_semantico("prompt")

    mock_gemini.assert_called_once_with("prompt")
    assert resultado == "respuesta gemini"


def test_backend_gemini_devuelve_texto_de_la_respuesta():
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"}):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value.text = "texto real"
        with patch(
            "src.multiagent_core.council._llm_backend.genai.Client",
            return_value=mock_client,
        ):
            resultado = llamar_juez_semantico("prompt", backend="gemini")

    assert resultado == "texto real"


def test_backend_gemini_usa_un_modelo_vigente_no_el_retirado():
    """Bug real (2026-09-25): `gemini-2.0-flash` fue retirado del catálogo
    de Google -- una llamada real devuelve HTTP 404 con el mensaje "This
    model models/gemini-2.0-flash is no longer available", exactamente el
    mismo patrón ya visto con `google/gemini-2.0-flash-001` en OpenRouter
    (ver GOVERNANCE.md, fix de esa sesión). Este test no puede detectar un
    futuro retiro del modelo (eso requiere red real), pero sí documenta y
    protege contra volver a hardcodear el nombre ya retirado por error de
    copia/pega entre backends."""
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"}):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value.text = "texto real"
        with patch(
            "src.multiagent_core.council._llm_backend.genai.Client",
            return_value=mock_client,
        ):
            llamar_juez_semantico("prompt", backend="gemini")

    _, kwargs = mock_client.models.generate_content.call_args
    assert kwargs.get("model") != "gemini-2.0-flash"


def test_backend_gemini_devuelve_none_si_response_text_es_none():
    """Mismo caso borde ya documentado en stats_tutor_agent.py:507 --
    Gemini puede devolver response.text=None sin lanzar excepción
    (contenido bloqueado por safety filters)."""
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"}):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value.text = None
        with patch(
            "src.multiagent_core.council._llm_backend.genai.Client",
            return_value=mock_client,
        ):
            resultado = llamar_juez_semantico("prompt", backend="gemini")

    assert resultado is None


def test_backend_gemini_devuelve_none_si_la_llamada_lanza_excepcion():
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"}), patch(
        "src.multiagent_core.council._llm_backend.genai.Client",
        side_effect=RuntimeError("fallo de red simulado"),
    ):
        resultado = llamar_juez_semantico("prompt", backend="gemini")

    assert resultado is None


def test_backend_anthropic_devuelve_texto_de_la_respuesta():
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "fake-key"}):
        mock_client = MagicMock()
        mock_bloque = MagicMock()
        mock_bloque.text = "texto de claude"
        mock_client.messages.create.return_value.content = [mock_bloque]
        with patch(
            "src.multiagent_core.council._llm_backend.anthropic.Anthropic",
            return_value=mock_client,
        ):
            resultado = llamar_juez_semantico("prompt", backend="anthropic")

    assert resultado == "texto de claude"


def test_backend_anthropic_devuelve_none_si_la_llamada_lanza_excepcion():
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "fake-key"}), patch(
        "src.multiagent_core.council._llm_backend.anthropic.Anthropic",
        side_effect=RuntimeError("fallo simulado"),
    ):
        resultado = llamar_juez_semantico("prompt", backend="anthropic")

    assert resultado is None


def test_backend_openrouter_devuelve_texto_de_la_respuesta():
    with patch.dict(os.environ, {"OPENROUTER_API_KEY": "fake-key"}):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "texto de openrouter"}}]
        }
        with patch(
            "src.multiagent_core.council._llm_backend.requests.post",
            return_value=mock_response,
        ):
            resultado = llamar_juez_semantico("prompt", backend="openrouter")

    assert resultado == "texto de openrouter"


def test_backend_gemini_fija_temperatura_cero():
    """Determinismo (hallazgo real medido en producción, 2026-09-25): sin
    temperature=0, el mismo corpus y el mismo prompt dieron resultados
    distintos en corridas consecutivas (recall 0.375 vs 0.25) -- una
    medición de precisión/recall no es confiable si el propio juez no es
    determinista. Se fija temperature=0 en los 3 backends."""
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"}):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value.text = "texto real"
        with patch(
            "src.multiagent_core.council._llm_backend.genai.Client",
            return_value=mock_client,
        ):
            llamar_juez_semantico("prompt", backend="gemini")

    _, kwargs = mock_client.models.generate_content.call_args
    config = kwargs.get("config")
    assert config is not None, "generate_content debe recibir config con temperature"
    assert config.temperature == 0


def test_backend_gemini_fija_seed_para_reforzar_determinismo():
    """`temperature=0` reduce pero no elimina la varianza (ver GOVERNANCE.md,
    2026-09-25) -- Gemini expone además `seed`, un segundo control de
    determinismo independiente de `temperature`. Se fija junto con
    `temperature=0` para reforzar la reproducibilidad, no reemplazarla."""
    with patch.dict(os.environ, {"GEMINI_API_KEY": "fake-key"}):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value.text = "texto real"
        with patch(
            "src.multiagent_core.council._llm_backend.genai.Client",
            return_value=mock_client,
        ):
            llamar_juez_semantico("prompt", backend="gemini")

    _, kwargs = mock_client.models.generate_content.call_args
    config = kwargs.get("config")
    assert config.seed is not None


def test_backend_anthropic_no_pasa_kwargs_inexistentes_en_el_sdk_instalado():
    """Regresión real (2026-09-25): el SDK `anthropic` publicado ese mismo
    mes (1.8.0) eliminó `temperature` de `messages.create()` por completo
    -- confirmado inspeccionando la firma real del paquete instalado, sin
    ningún `temperature` en `inspect.signature(...)` ni en ningún tipo de
    `anthropic.types`. La versión anterior de este backend pasaba
    `temperature=0` y fallaba en producción con
    `TypeError: Messages.create() got an unexpected keyword argument
    'temperature'` -- nunca detectado por los tests porque `MagicMock()`
    acepta cualquier kwarg sin validar contra una firma real.

    Este test intercepta los kwargs reales que `_via_anthropic` construye
    y los valida con `inspect.signature(...).bind(...)` contra la firma
    REAL del SDK instalado -- si `_via_anthropic` volviera a pasar un
    kwarg que el SDK no acepta, `bind()` lanzaría `TypeError` aquí mismo,
    en vez de que el bug solo se manifieste en producción con una key
    real."""
    import inspect

    import anthropic as anthropic_real

    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "fake-key"}):
        mock_client = MagicMock()
        mock_bloque = MagicMock()
        mock_bloque.text = "texto de claude"
        mock_client.messages.create.return_value.content = [mock_bloque]
        with patch(
            "src.multiagent_core.council._llm_backend.anthropic.Anthropic",
            return_value=mock_client,
        ):
            resultado = llamar_juez_semantico("prompt", backend="anthropic")

    _, kwargs = mock_client.messages.create.call_args
    firma_real = inspect.signature(anthropic_real.Anthropic().messages.create)
    firma_real.bind(**kwargs)  # lanza TypeError si algún kwarg no existe

    assert resultado == "texto de claude"


def test_backend_openrouter_fija_temperatura_cero():
    with patch.dict(os.environ, {"OPENROUTER_API_KEY": "fake-key"}):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "texto de openrouter"}}]
        }
        with patch(
            "src.multiagent_core.council._llm_backend.requests.post",
            return_value=mock_response,
        ) as mock_post:
            llamar_juez_semantico("prompt", backend="openrouter")

    _, kwargs = mock_post.call_args
    assert kwargs["json"]["temperature"] == 0


def test_backend_openrouter_devuelve_none_si_la_peticion_falla():
    import requests

    with patch.dict(os.environ, {"OPENROUTER_API_KEY": "fake-key"}), patch(
        "src.multiagent_core.council._llm_backend.requests.post",
        side_effect=requests.RequestException("fallo simulado"),
    ):
        resultado = llamar_juez_semantico("prompt", backend="openrouter")

    assert resultado is None
