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
_LECCIONES = _RAIZ_REPO / "lecciones"
_UNIDAD_1 = _LECCIONES / "UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md"
_UNIDAD_6 = _LECCIONES / "UNIDAD_6_MODELADO_SIMULACION.md"
_UNIDAD_7 = _LECCIONES / "UNIDAD_7_INFERENCIA_ESTIMACION.md"

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
        (
            "El nanotubo azul come probabilidad de lunes cuadrado sin sentido alguno "
            "porque la varianza del queso mide $x$ colores. "
        )
        * 90
        + _DECORACION_QUE_ENGANA_AL_CONSEJO
        + r"$\boxed{P = 99}$"
    )

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


def test_h05_de_unidad_6_ya_no_es_detectado_tras_la_correccion(council):
    """H-05 (corregido por Task 2): el texto de §2.3 declaraba T=12.3957 pero
    la celda SymPy resolvía la forma sin simplificar y producía 6.8447 para
    el mismo U=0.35. La celda ahora resuelve la forma simplificada
    (`sp.Eq(u, sp.exp(-(t/lam)**k))`), consistente con el texto y con
    `weibull_min.isf(0.35, c=1.5, scale=12) == 12.3953`.

    Este test invierte `test_detecta_el_bug_real_h05_de_unidad_6`: antes
    documentaba la capacidad de detección del Consejo con el bug presente;
    ahora confirma que, corregido el contenido, el Consejo aprueba y no deja
    un hallazgo de tipo `desajuste_ejemplo_salida` para U6.
    """
    resultado = council.process_content(
        _UNIDAD_6.read_text(encoding="utf-8"), unit_name="UNIDAD 6"
    )

    desajustes = [
        h
        for h in resultado["final_qa"]["hallazgos"]
        if h["tipo"] == "desajuste_ejemplo_salida"
    ]
    assert resultado["approved"] is True
    assert not desajustes, f"no debería quedar hallazgo de H-05: {desajustes}"


def test_h02_de_unidad_7_ya_no_es_detectado_tras_la_correccion(council):
    """H-02 (corregido por Task 2): `\\boxed{}` usaba la media nominal
    (145.19) en vez de la muestral real (142.19), y esa división no cerraba
    contra 0.75. El `\\boxed{}` ahora usa 142.19, consistente con
    `(142.19-125.37)/22.32 ≈ 0.7535`.

    Este test invierte `test_detecta_el_bug_real_h02_de_unidad_7`: antes
    documentaba la capacidad de detección del Consejo con el bug presente;
    ahora confirma que, corregido el contenido, el Consejo aprueba y no deja
    un hallazgo de tipo `aritmetica_inconsistente` para U7.
    """
    resultado = council.process_content(
        _UNIDAD_7.read_text(encoding="utf-8"), unit_name="UNIDAD 7"
    )

    inconsistencias = [
        h
        for h in resultado["final_qa"]["hallazgos"]
        if h["tipo"] == "aritmetica_inconsistente"
    ]
    assert resultado["approved"] is True
    assert not inconsistencias, f"no debería quedar hallazgo de H-02: {inconsistencias}"


def test_contenido_real_correcto_sigue_aprobando(council):
    """Control: una unidad real sin errores conocidos no debe verse penalizada por el fix.

    UNIDAD 1 no tiene ninguno de los bugs de contenido documentados
    (H-02 vive en UNIDAD 7, H-05 en UNIDAD 6), así que debe aprobar limpia.
    """
    contenido_u1 = _UNIDAD_1.read_text(encoding="utf-8")

    resultado = council.process_content(contenido_u1, unit_name="UNIDAD 1")

    # @Librarian consulta Crossref por red. Si el runner no tiene salida a
    # internet, el DOI no resuelve y la unidad reprobaría por un motivo
    # ajeno a lo que este test verifica; se distingue ese caso en vez de
    # dejar un fallo intermitente que se lea como una regresión del Consejo.
    if not resultado["reports"]["librarian"]["passed"]:
        pytest.skip("Crossref no accesible desde este entorno; control no aplicable")

    hallazgos = resultado["final_qa"]["hallazgos"]
    assert (
        resultado["approved"] is True
    ), f"contenido real correcto no debe reprobarse; hallazgos: {hallazgos}"
