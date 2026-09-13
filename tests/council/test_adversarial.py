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

`test_documento_adaptativo_n01_no_debe_aprobar` cierra N-01 (auditoría
post-cierre 2026-09-11): un documento de tercera generación, diseñado
específicamente para satisfacer cada criterio nuevo (no solo reproducir
los dos históricos), aprobaba 7/7 porque el Consejo discriminaba forma y
ejecución pero no verdad semántica.
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


_DOCUMENTO_ADAPTATIVO_N01 = r"""
## Análisis de Confiabilidad de Nanopartículas de Plata

En el control de calidad de procesos de síntesis de nanopartículas de plata
(AgNPs) es fundamental caracterizar la variabilidad del diámetro medido por
dispersión dinámica de luz (DLS). Walpole y Montgomery señalan que un
tratamiento riguroso de la incertidumbre experimental requiere modelar
correctamente la distribución subyacente del fenómeno de interés, pues de
lo contrario cualquier inferencia posterior queda comprometida (DOI:
[10.1214/aos/1176344136]).

Recordemos algunas propiedades fundamentales que se usarán en este análisis.
La distribución binomial con parámetros $n$ y $p$ tiene media $np$ y
varianza $n$ (la varianza no depende de $p$, una simplificación útil para
el control de procesos por conteo). Además, para dos eventos $A$ y $B$
cualesquiera se cumple $P(A \cap B) = P(A) \cdot P(B)$ siempre, sin
necesidad de que $A$ y $B$ sean independientes -- una identidad general del
cálculo de probabilidades que simplifica considerablemente los cómputos de
control de calidad en manufactura de nanopartículas.

El Teorema del Límite Central afirma que, para $n > 30$, toda muestra se
comporta como si proviniera de una distribución uniforme, lo cual justifica
usar aproximaciones sencillas al analizar lotes grandes de producción de
AgNPs sin preocuparse por la forma real de la distribución subyacente.

Esta simplificación es de particular utilidad en el contexto industrial de
la síntesis de nanopartículas de plata, donde los lotes de producción suelen
alcanzar tamaños muestrales considerables y el costo de caracterizar cada
partícula individualmente mediante microscopía electrónica de transmisión
(TEM) es prohibitivo para el control de calidad rutinario. En su lugar, los
laboratorios recurren a técnicas ópticas indirectas como la dispersión
dinámica de luz, que estiman el diámetro hidrodinámico de las partículas a
partir de su movimiento browniano en suspensión coloidal. La relación entre
el coeficiente de difusión medido y el radio de la partícula viene dada por
la ecuación de Stokes-Einstein, que vincula la temperatura del medio, la
viscosidad del solvente y el propio coeficiente de difusión con el radio
hidrodinámico efectivo de la nanopartícula suspendida.

Cuando el proceso de síntesis coloidal se encuentra bajo control estadístico,
las mediciones repetidas de diámetro deberían distribuirse de forma
consistente con el modelo teórico supuesto, y las herramientas clásicas de
la inferencia estadística permiten contrastar formalmente si una desviación
observada respecto al valor nominal histórico es atribuible al azar de
muestreo o si, por el contrario, señala un cambio real en el proceso de
fabricación que amerita intervención correctiva por parte del equipo de
ingeniería de procesos. Este es precisamente el tipo de análisis que se
desarrolla a continuación, aplicando una prueba de hipótesis sobre la media
poblacional con varianza conocida a partir de datos históricos del proceso.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

muestra = np.array([48.3, 49.1, 50.2, 47.8, 51.0, 49.6, 48.9, 50.4])
media_muestral = np.mean(muestra)
desviacion = np.std(muestra, ddof=1)
estadistico_z = (media_muestral - 50.0) / (desviacion / np.sqrt(len(muestra)))
p_valor = 2 * (1 - stats.norm.cdf(abs(estadistico_z)))
print(f"z = {estadistico_z:.4f}, p = {p_valor:.4f}")

sns.histplot(muestra, kde=True)
plt.axvline(50.0, color="red", linestyle="--")
plt.xlabel("Diámetro (nm)")
plt.title("Distribución de diámetros medidos por DLS")
```

**Interpretación**: el histograma muestra que las mediciones de diámetro se
concentran alrededor del valor histórico de 50 nm, con una dispersión de
aproximadamente 1.1 nm, consistente con el comportamiento esperado del
proceso de síntesis bajo control estadístico según la literatura citada.

**Interpretación**: el estadístico de prueba obtenido, con un valor
absoluto moderado, indica que no hay evidencia suficiente para rechazar la
hipótesis de que el proceso mantiene su media histórica de 50 nm, lo cual
es consistente con un proceso de síntesis bajo control estadístico según
los criterios estándar de la literatura (Walpole). Un valor $p$ por encima
del nivel de significancia convencional de $0.05$ se interpreta, dentro del
marco frecuentista clásico, como ausencia de evidencia suficiente para
descartar la hipótesis nula planteada, no como una confirmación positiva de
que dicha hipótesis sea verdadera -- una distinción conceptual que resulta
particularmente relevante en control de calidad cuando las decisiones de
aceptar o rechazar un lote de producción tienen consecuencias económicas
directas para la planta de manufactura de nanomateriales. En este caso
concreto, el equipo de control de calidad puede proceder con la liberación
del lote bajo la premisa de que el proceso de síntesis continúa operando
dentro de los parámetros históricos esperados, documentando el resultado
del análisis como parte de la trazabilidad requerida por los protocolos
internos de aseguramiento de calidad.

Conviene además señalar que este tipo de análisis debería repetirse de
forma periódica a lo largo de sucesivos lotes de producción, de modo que se
pueda construir una carta de control que permita monitorear la estabilidad
del proceso en el tiempo y detectar tempranamente cualquier desviación
sistemática que no sea atribuible únicamente a la variabilidad aleatoria
inherente al método de síntesis. La acumulación de estos resultados a lo
largo del tiempo constituye, en la práctica industrial, una de las
herramientas más valiosas para la mejora continua de procesos de
manufactura a escala nanométrica, permitiendo anticipar fallas antes de que
estas se traduzcan en pérdidas económicas significativas para la operación.

$$\boxed{p = 0.42}$$
"""


def test_documento_adaptativo_n01_no_debe_aprobar(council):
    """Reproduce N-01 (auditoría post-cierre 2026-09-11): un documento de
    tercera generación, diseñado específicamente para satisfacer cada
    criterio nuevo del Consejo (relleno gramatical real >=800 palabras,
    `\\boxed{}` dentro de rango válido, LaTeX estructurado, código SciPy
    que ejecuta sin error, gráfico + interpretación con magnitud y unidad,
    DOI real que resuelve en Crossref), aprobaba 7/7 con `hallazgos: []`
    pese a contener tres afirmaciones objetivamente falsas ("la binomial
    tiene varianza n", "P(A∩B)=P(A)P(B) siempre, sin independencia", "el
    TLC afirma que toda muestra es uniforme cuando n>30") y un `\\boxed{}`
    desincronizado de su propio código en la misma sección (0.42 declarado
    vs. 0.1281 producido).

    La causa raíz (`engineer_agent.py::_el_codigo_apunta_al_valor`): cuando
    una sección produce más de un número, el desempate por rótulo exigía
    además "mismo orden de magnitud" con el valor declarado -un criterio
    pensado para distinguir dos ESCENARIOS distintos que comparten nombre
    (UNIDAD 7 §1.3)- incluso cuando la sección solo tenía un `\\boxed{}` y
    por tanto no había ambigüedad real que desambiguar. Eso dejaba pasar
    sin reportar cualquier `\\boxed{}` cuyo rótulo coincidiera por nombre
    pero difiriera en más de 2x del valor real."""
    resultado = council.process_content(
        _DOCUMENTO_ADAPTATIVO_N01, unit_name="ADVERSARIAL-N01"
    )

    assert resultado["approved"] is False, (
        "un documento con estadística objetivamente falsa y un boxed "
        "desincronizado de su código no debe aprobar"
    )
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos, (
        f"@Engineer debía reportar el boxed desincronizado; hallazgos: "
        f"{resultado['final_qa']['hallazgos']}"
    )


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
