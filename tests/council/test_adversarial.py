"""
Tests adversariales del Consejo de 8 Expertos (H-01).

La auditoría comprobó experimentalmente que el Consejo aprobaba 100/100
tanto documentos sintéticos sin contenido real como afirmaciones
estadísticas objetivamente falsas, porque cada agente decidía contando
subcadenas (`text.count("$")`, `"scipy" in code_text`, `"interpret" in
text.lower()`) en vez de verificar nada.

Estos tests son el gate de regresión de esa reconstrucción: si alguno
vuelve a pasar en verde con documentos basura, el Consejo volvió a ser
decorativo.
"""

from pathlib import Path

import pytest

from src.multiagent_core.pipeline import CouncilPipeline

_RAIZ_REPO = Path(__file__).resolve().parents[2]
_UNIDAD_1 = _RAIZ_REPO / "lecciones" / "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"

# Los documentos adversariales de la auditoría llevaban las subcadenas que
# cada agente buscaba (`scipy`, `plt.`, `sns.`, "Interpretación", "Walpole").
# Sin ellas el pipeline rechaza la basura por accidente —por ausencia de la
# palabra clave, no por haber verificado nada— y el test daría un verde
# falso que no prueba lo que H-01 denuncia. Este apéndice reproduce esas
# decoraciones para que la basura llegue viva hasta cada agente y sea el
# contenido, no la subcadena faltante, lo que decida el rechazo.
_DECORACION_QUE_ENGANA_AL_CONSEJO = """
```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.plot([1, 2, 3])
sns.histplot([1, 2, 3])
```

Interpretación: según Walpole y Montgomery, el resultado anterior confirma
lo esperado en el contexto de nanotecnología.
"""


@pytest.fixture
def council():
    return CouncilPipeline()


def test_basura_sintetica_no_debe_aprobar(council):
    """Reproduce H-01: 1742 palabras de frase repetida sin contenido real aprobaba 100/100."""
    basura = (
        "El nanotubo azul come probabilidad de lunes cuadrado sin sentido alguno "
        "porque la varianza del queso mide $x$ colores. "
    ) * 90 + _DECORACION_QUE_ENGANA_AL_CONSEJO + r"$\boxed{P = 99}$"

    resultado = council.process_content(basura)

    assert (
        resultado["approved"] is False
    ), "un documento sin contenido real no debe aprobar"


def test_matematicas_falsas_no_deben_aprobar(council):
    """Reproduce H-01: afirmaciones estadisticas objetivamente incorrectas aprobaban 100/100."""
    texto_falso = (
        (
            "la binomial tiene media n*p*p y varianza n. "
            "la suma de todas las probabilidades de una funcion de masa es siempre 2. "
            "P(A|B) = P(A)*P(B). "
            "la desviacion estandar puede ser negativa. "
            "el TLC afirma que toda muestra es uniforme. "
        )
        * 25
        + _DECORACION_QUE_ENGANA_AL_CONSEJO
        + r"$\boxed{P = 1.75}$"
    )

    resultado = council.process_content(texto_falso)

    assert (
        resultado["approved"] is False
    ), "matematicas objetivamente falsas no deben aprobar"


def test_probabilidad_fuera_de_rango_es_hallazgo_del_scientist(council):
    """Una probabilidad declarada fuera de [0,1] es un invariante de dominio
    violado, verificable sin LLM — el @Scientist debe señalarlo."""
    texto = ("teoría de la probabilidad aplicada a nanopartículas " * 200) + (
        r"Por lo tanto $P(A) = 1.75$ y entonces $\boxed{P(A) = 1.75}$."
    )

    resultado = council.process_content(texto)

    assert resultado["reports"]["scientist"]["passed"] is False
    assert resultado["reports"]["scientist"]["invariantes_violados"]


def test_contenido_real_correcto_sigue_aprobando(council):
    """Control: una unidad real sin errores conocidos no debe verse penalizada por el fix."""
    contenido_u1 = _UNIDAD_1.read_text(encoding="utf-8")

    resultado = council.process_content(contenido_u1, unit_name="UNIDAD 1")

    assert resultado["approved"] is True, "contenido real correcto no debe reprobarse"
