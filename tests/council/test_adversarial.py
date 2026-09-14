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


def _documento_con_boxed_final(boxed_extra: str) -> str:
    """Reemplaza la última línea de `\\boxed{}` de `_DOCUMENTO_ADAPTATIVO_N01`
    (`$$\\boxed{p = 0.42}$$`) por `boxed_extra`, manteniendo el resto del
    documento (relleno gramatical, código real, gráfico) intacto."""
    return _DOCUMENTO_ADAPTATIVO_N01.replace(r"$$\boxed{p = 0.42}$$", boxed_extra)


def test_v1_dos_boxed_calibrados_dentro_del_factor_2x_se_reportan(council):
    """N-03, V1: dos `\\boxed{}` en la misma sección, ambos fabricados
    dentro del factor 2x de los valores reales (z=-1.5216, p=0.1281).
    Ratios verificados: 2.4/1.5216=1.577, 0.21/0.1281=1.639, ambos en
    [0.5, 2.0]. Control positivo: cuando hay ambigüedad real (>=2 boxed),
    el emparejamiento por rótulo asigna cada uno a SU valor rotulado y
    compara contra el correcto, no contra el más conveniente."""
    doc = _documento_con_boxed_final(
        r"$$\boxed{z = -2.4000}$$" "\n\n" r"$$\boxed{p = 0.2100}$$"
    )
    resultado = council.process_content(doc, unit_name="ADV-GEN4-V1")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v2_numero_correcto_con_nombre_incorrecto_es_limite_conocido_n04(council):
    """N-04 (BAJO, no accionable con el diseño heurístico actual): un
    `\\boxed{0.1281}` sin rótulo cuyo número coincide exactamente con el
    p-valor real, pero el texto lo nombra "significancia crítica" cuando
    es un p-valor. No hay discrepancia numérica que detectar -el valor es
    correcto-, así que ningún agente heurístico puede levantar esto sin
    comprensión semántica del nombre. Documentado como límite de diseño,
    NO como bug a resolver: ver N-04 en la auditoría del 2026-09-13."""
    doc = _documento_con_boxed_final(r"$$\boxed{0.1281}$$")
    resultado = council.process_content(doc, unit_name="ADV-GEN4-V2")
    assert resultado["approved"] is True


def test_v3_rotulo_ausente_con_un_solo_boxed_se_detecta_tras_fix_de_n03(council):
    """N-03 (ALTO): el caso real que este fix cierra. Un único
    `\\boxed{\\hat{\\theta} = 0.4200}` cuyo nombre (theta) no aparece
    como rótulo en el stdout (el código imprime z y p, no theta). Antes
    del fix: `_el_codigo_apunta_al_valor` devolvía False en la guarda
    `if not valores_rotulados: return False`, y la discrepancia se
    descartaba sin reportar (approved=True, hallazgos=[]). Tras el fix:
    con un solo `\\boxed{}` no simbólico en la sección, se compara
    directo contra los números producidos sin exigir rótulo."""
    doc = _documento_con_boxed_final(r"$$\boxed{\hat{\theta} = 0.4200}$$")
    resultado = council.process_content(doc, unit_name="ADV-GEN4-V3")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v3_variante_rotulo_ausente_con_dos_boxed_sigue_sin_detectarse(council):
    """Límite conocido de A1, documentado explícitamente para que no se
    redescubra como sorpresa: con >=2 `\\boxed{}` en la sección, un
    `\\boxed{}` sin rótulo SIGUE sin detectarse -A1 solo relaja el caso
    de un único `\\boxed{}` no ambiguo. Con dos, `_el_codigo_apunta_al_valor`
    aún puede devolver False en la guarda de `valores_rotulados` vacío
    para el primero. No accionable sin tocar también la rama de rótulo
    presente (fuera de alcance de este spec)."""
    doc = _documento_con_boxed_final(
        r"$$\boxed{\hat{\theta} = 0.4200}$$" "\n\n" r"$$\boxed{p = 0.2100}$$"
    )
    resultado = council.process_content(doc, unit_name="ADV-GEN4-V3-DOS-BOXED")
    # El segundo boxed (p=0.21, rotulado, dentro del factor 2x) sí se
    # detecta -por eso approved sigue False-, pero el hallazgo del theta
    # sin rótulo no debe estar entre los reportados.
    assert resultado["approved"] is False
    mensajes = [
        h["mensaje"]
        for h in resultado["final_qa"]["hallazgos"]
        if h["tipo"] == "desajuste_ejemplo_salida"
    ]
    assert not any("0.42" in m or "theta" in m.lower() for m in mensajes)


def test_v4_boxed_unico_con_rotulo_presente_dentro_del_factor_2x_se_reporta(council):
    """Control: un solo `\\boxed{p = 0.2100}` con rótulo presente (p),
    dentro del factor 2x del valor real (0.1281). Ya funciona hoy vía la
    rama de magnitud existente; tras A1 pasa por el camino nuevo (un
    solo boxed no simbólico -> comparación directa), y debe seguir
    reportando."""
    doc = _documento_con_boxed_final(r"$$\boxed{p = 0.2100}$$")
    resultado = council.process_content(doc, unit_name="ADV-GEN4-V4")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v5_marca_simbolica_decorativa_con_valor_real_se_reporta(council):
    """N-05 (ALTO, auditoría 2026-09-14): una marca de sumatoria decorativa
    junto a un valor numérico real desactivaba el fix de N-03 -- la
    compuerta `_es_formula_simbolica` bastaba con que la marca apareciera
    en cualquier parte de la expresión, sin exigir que la expresión
    careciera de un valor concreto. `\\hat{\\theta} = \\sum \\; 0.4200` no es
    una fórmula simbólica genuina (tiene un valor real, 0.42), pero
    activaba la exclusión igual que `\\frac{1}{n}\\sum_{i=1}^n X_i` (sin
    ningún valor concreto, U7 §6.2, el caso que la exclusión protege)."""
    doc = _documento_con_boxed_final(r"$$\boxed{\hat{\theta} = \sum \; 0.4200}$$")
    resultado = council.process_content(doc, unit_name="ADV-N05")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v5b_indice_decorativo_con_valor_real_se_reporta(council):
    """N-05, variante con el patrón de índice de sumatoria (`_{i=1}^`)
    en vez de `\\sum` explícito."""
    doc = _documento_con_boxed_final(r"$$\boxed{\hat{\theta}_{i=1}^{n} = 0.4200}$$")
    resultado = council.process_content(doc, unit_name="ADV-N05B")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v5c_integral_decorativa_con_valor_real_se_reporta(council):
    """N-05, variante con `\\int` decorativo."""
    doc = _documento_con_boxed_final(r"$$\boxed{\hat{\theta} = \int 0.4200}$$")
    resultado = council.process_content(doc, unit_name="ADV-N05C")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v6_entero_pequeno_ya_no_evade(council):
    """N-08 (ALTO, auditoría 2026-09-14), vector 1: un entero <=10 dentro
    del `\\boxed{}` desactivaba el fix de N-05 porque `_operandos_distintivos`
    descarta enteros con abs<=10 -mismo umbral que protege el caso legítimo
    de U7 §6.2 (donde el único número es el índice `1` de una sumatoria)."""
    doc = _documento_con_boxed_final(r"$$\boxed{\hat{\theta} = \sum \; 7}$$")
    resultado = council.process_content(doc, unit_name="ADV-N08-V1")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v6b_valor_en_text_ya_no_evade(council):
    """N-08, vector 2: un valor dentro de `\\text{}` desactivaba el fix de
    N-05 porque `_limpiar_latex` descarta el contenido de `\\text{}` antes
    de que `_operandos_distintivos` vea nada."""
    doc = _documento_con_boxed_final(
        r"$$\boxed{\hat{\theta} = \sum \; \text{0.4200}}$$"
    )
    resultado = council.process_content(doc, unit_name="ADV-N08-V2")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v6c_valor_como_exponente_ya_no_evade(council):
    """N-08, vector 3: un valor como exponente desactivaba el fix de N-05
    porque `_limpiar_latex` descarta exponentes `^{...}`."""
    doc = _documento_con_boxed_final(r"$$\boxed{\hat{\theta} = \sum \; 10^{-3}}$$")
    resultado = council.process_content(doc, unit_name="ADV-N08-V3")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_v6d_borde_entero_diez_ya_no_evade(council):
    """Confirma que el nuevo criterio no reintroduce el viejo umbral
    abs<=10 en otro punto: el entero exactamente 10 tampoco debe evadir."""
    doc = _documento_con_boxed_final(r"$$\boxed{\hat{\theta} = \sum \; 10}$$")
    resultado = council.process_content(doc, unit_name="ADV-N08-V4")
    assert resultado["approved"] is False
    tipos = {h["tipo"] for h in resultado["final_qa"]["hallazgos"]}
    assert "desajuste_ejemplo_salida" in tipos


def test_formula_simbolica_genuina_sin_valor_sigue_excluida():
    """Control negativo de N-05: una fórmula simbólica genuina (patrón
    real de UNIDAD 7 §6.2, `\\hat{\\mu}_{MLE} = \\bar{X} = \\frac{1}{n}
    \\sum_{i=1}^n X_i`), sin ningún valor numérico concreto -solo el
    índice `1` de la sumatoria, trivial-, debe seguir clasificándose
    como simbólica tras el rediseño. Test unitario directo sobre
    `_es_formula_simbolica`, sin pasar por el pipeline completo (el caso
    de integración ya lo cubre `test_codigo_solo_simbolico_no_genera_discrepancia`
    en `tests/council/test_engineer_agent.py`)."""
    from src.multiagent_core.council._contraste_boxed import _es_formula_simbolica

    formula_protegida = r"\hat{\mu}_{MLE} = \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i"
    assert _es_formula_simbolica(formula_protegida) is True


def test_valor_final_declarado_extrae_el_ultimo_numero_tras_el_ultimo_igual():
    """N-08 (auditoría 2026-09-14): tabla de casos conocidos del rediseño
    estructural. `_valor_final_declarado` reemplaza la pregunta "¿sobrevivió
    algún operando al filtro de ruido?" por "¿la expresión declara
    explícitamente un valor numérico al final?"."""
    from src.multiagent_core.council._contraste_boxed import _valor_final_declarado

    # Legítimo (U7 §6.2): termina en notación simbólica sin resolver -> None
    formula_protegida = r"\hat{\mu}_{MLE} = \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i"
    assert _valor_final_declarado(formula_protegida) is None

    # Legítimo (U4 §2.3): valor concreto real
    assert _valor_final_declarado(r"\int_0^{0.5} f(x)\,dx = 0.375") == pytest.approx(0.375)

    # Vector 1 (N-08): entero <=10, ya no se descarta
    assert _valor_final_declarado(r"\hat{\theta} = \sum \; 7") == pytest.approx(7.0)

    # Vector 2 (N-08): valor dentro de \text{}, ya no se descarta
    assert _valor_final_declarado(
        r"\hat{\theta} = \sum \; \text{0.4200}"
    ) == pytest.approx(0.42)

    # Vector 3 (N-08): valor como exponente, ya no se descarta
    assert _valor_final_declarado(r"\hat{\theta} = \sum \; 10^{-3}") == pytest.approx(0.001)

    # Borde: entero exactamente en el viejo umbral abs<=10
    assert _valor_final_declarado(r"\hat{\theta} = \sum \; 10") == pytest.approx(10.0)

    # Real (UNIDAD_3:439): "=" interno no asignativo dentro de P(X = 2)
    assert _valor_final_declarado(
        r"P(X = 2) = 190 \times 0.0025 \times 0.397214 \approx 0.18868 \quad (18.87\%)"
    ) == pytest.approx(18.87)
