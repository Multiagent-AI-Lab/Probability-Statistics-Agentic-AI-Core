"""
Backend LLM multi-proveedor para el juez semántico del Consejo
(ver docs/superpowers/specs/2026-09-23-semantic-auditor-agent-design.md).

Una única función pública, `llamar_juez_semantico`, que nunca lanza: toda
excepción o respuesta vacía del proveedor se traduce a `None`, y es
responsabilidad exclusiva del llamador (SemanticAuditorAgent) decidir cómo
degradar ante esa ausencia -- fail-open, nunca fail-closed (ver spec).

Inicialización de cliente siempre perezosa, dentro de cada función `_via_*`
-- nunca a nivel de módulo ni en un `__init__` -- mismo patrón que
`StatsTutorAgent.ask()` (stats_tutor_agent.py), por la misma razón: no
depender del orden en que se configuran variables de entorno.
"""

import logging
import os

import requests
from google import genai

try:
    import anthropic
except ImportError:  # pragma: no cover - anthropic es dependencia opcional
    anthropic = None

logger = logging.getLogger(__name__)

_BACKENDS_VALIDOS = ("gemini", "anthropic", "openrouter")


def llamar_juez_semantico(prompt: str, backend: str | None = None) -> str | None:
    """Invoca el LLM configurado como juez semántico.

    Retorna `None` si la llamada falla, el proveedor no está disponible, o
    el modelo no produce texto (p. ej. contenido bloqueado por safety
    filters) -- nunca lanza. El llamador decide cómo degradar ante `None`.
    """
    backend = backend or os.environ.get("SEMANTIC_JUDGE_BACKEND", "gemini")
    if backend not in _BACKENDS_VALIDOS:
        raise ValueError(
            f"backend desconocido: {backend!r} -- válidos: {_BACKENDS_VALIDOS}"
        )
    if backend == "gemini":
        return _via_gemini(prompt)
    if backend == "anthropic":
        return _via_anthropic(prompt)
    return _via_openrouter(prompt)


def _via_gemini(prompt: str) -> str | None:
    try:
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        if response.text is None:
            logger.warning("Gemini devolvió response.text=None para el juez semántico")
            return None
        return response.text
    except Exception:
        logger.exception("Fallo al invocar Gemini como juez semántico")
        return None


def _via_anthropic(prompt: str) -> str | None:
    if anthropic is None:
        logger.error("El paquete 'anthropic' no está instalado")
        return None
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        if not response.content:
            logger.warning("Anthropic devolvió content vacío para el juez semántico")
            return None
        return response.content[0].text
    except Exception:
        logger.exception("Fallo al invocar Anthropic como juez semántico")
        return None


def _via_openrouter(prompt: str) -> str | None:
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
                "Content-Type": "application/json",
            },
            json={
                "model": "google/gemini-2.5-flash",
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=30,
        )
        response.raise_for_status()
        datos = response.json()
        contenido = datos["choices"][0]["message"]["content"]
        if not contenido:
            logger.warning("OpenRouter devolvió contenido vacío para el juez semántico")
            return None
        return contenido
    except Exception:
        logger.exception("Fallo al invocar OpenRouter como juez semántico")
        return None
