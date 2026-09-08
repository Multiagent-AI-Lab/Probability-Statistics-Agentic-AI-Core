"""
Tests for ContentAuditorAgent.
"""

from src.multiagent_core.content_auditor_agent import ContentAuditorAgent


def test_content_auditor():
    auditor = ContentAuditorAgent()
    nano_paragraph = (
        "En este problema aplicado a nanotecnología estudiamos el comportamiento "
        "de nanopartículas de oro dispersas en una solución coloidal. " * 15
    )
    sample_text = (
        """# Teoría Completa
"""
        + "palabra " * 850
        + f"""

## Ejemplo Analítico Paso a Paso
El paso 1 consiste en calcular el potencial zeta de nanopartículas de oro.
{nano_paragraph}
La solución final es \\boxed{{42.0}}.

```python
import sympy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.histplot([1, 2, 3])
plt.figure()
sns.boxplot([1, 2, 3])
```

## Interpretación y Diccionario de Variables
Interpretación detallada del modelo estadístico.
"""
    )
    res = auditor.audit_content(sample_text)
    assert res["passed"] is True
    assert res["component_checks"]["Teoría Completa"] is True
    assert res["component_checks"]["Contexto Nanotecnológico"] is True


def test_nano_context_fails_when_mention_is_too_short():
    auditor = ContentAuditorAgent()
    sample_text = (
        """# Teoría Completa
"""
        + "palabra " * 850
        + """

## Ejemplo Analítico Paso a Paso
El paso 1 consiste en calcular algo. La solución final es \\boxed{42.0}.
Mencion breve de nanopartículas sin desarrollo real del contexto aplicado.

```python
import sympy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.histplot([1, 2, 3])
plt.figure()
sns.boxplot([1, 2, 3])
```

## Interpretación y Diccionario de Variables
Interpretación detallada del modelo estadístico.
"""
    )
    res = auditor.audit_content(sample_text)
    assert res["component_checks"]["Contexto Nanotecnológico"] is False


def test_nano_context_passes_with_150_plus_words():
    auditor = ContentAuditorAgent()
    nano_paragraph = (
        "En este problema aplicado a nanotecnología estudiamos el comportamiento "
        "de nanopartículas de oro dispersas en una solución coloidal. " * 15
    )
    sample_text = (
        """# Teoría Completa
"""
        + "palabra " * 850
        + f"""

## Ejemplo Analítico Paso a Paso
El paso 1 consiste en calcular el potencial zeta de nanopartículas de oro.
{nano_paragraph}
La solución final es \\boxed{{42.0}}.

```python
import sympy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.histplot([1, 2, 3])
plt.figure()
sns.boxplot([1, 2, 3])
```

## Interpretación y Diccionario de Variables
Interpretación detallada del modelo estadístico.
"""
    )
    res = auditor.audit_content(sample_text)
    assert res["component_checks"]["Contexto Nanotecnológico"] is True


def test_diccionario_variables_como_9no_componente_independiente():
    auditor = ContentAuditorAgent()
    assert len(auditor.mandatory_components) == 9
    assert any("Diccionario de Variables" in c for c in auditor.mandatory_components)


def test_component_checks_falla_diccionario_si_esta_ausente():
    auditor = ContentAuditorAgent()
    texto_sin_diccionario = "teoría " * 850  # sin lista de simbolo: descripcion
    result = auditor.audit_content(texto_sin_diccionario)
    assert result["component_checks"]["Diccionario de Variables"] is False


def test_component_checks_pasa_diccionario_si_tiene_formato_correcto():
    auditor = ContentAuditorAgent()
    texto_con_diccionario = (
        "teoría " * 850
        + "\n\n* $x$: diámetro medido de la nanopartícula.\n"
        + "* $n$: tamaño de la muestra.\n"
        + "* $\\bar{x}$: media muestral del diámetro.\n"
    )
    result = auditor.audit_content(texto_con_diccionario)
    assert result["component_checks"]["Diccionario de Variables"] is True


def test_verificacion_sympy_exige_uso_real_no_solo_la_palabra():
    """H-08: hoy 'sympy' in text.lower() basta, sin usar sp.Symbol/subs de verdad."""
    auditor = ContentAuditorAgent()
    texto_falso = "# esto menciona sympy pero no lo usa"
    resultado = auditor.audit_content(texto_falso)
    assert resultado["component_checks"]["Verificación SymPy"] is False


def test_verificacion_sympy_pasa_con_symbol_y_subs_reales():
    """Caso positivo: symbols(...) y .subs( en el mismo bloque de codigo."""
    auditor = ContentAuditorAgent()
    texto_real = (
        "Desarrollo teórico.\n\n"
        "```python\n"
        "import sympy as sp\n"
        "x = sp.symbols('x')\n"
        "expr = x ** 2\n"
        "resultado = expr.subs(x, 3)\n"
        "```\n"
    )
    resultado = auditor.audit_content(texto_real)
    assert resultado["component_checks"]["Verificación SymPy"] is True


def test_interpretacion_debe_ir_despues_del_grafico():
    """H-08: hoy la posicion relativa no se verifica, solo la presencia de la palabra."""
    auditor = ContentAuditorAgent()
    texto_interpretacion_antes = (
        "Interpretación: esto es alto.\n```python\nplt.plot(x, y)\n```"
    )
    resultado = auditor.audit_content(texto_interpretacion_antes)
    assert resultado["component_checks"]["Interpretación Post-Gráfico"] is False


def test_interpretacion_pasa_cuando_va_despues_del_grafico():
    """Caso positivo: el parrafo de interpretacion aparece tras el bloque con plt."""
    auditor = ContentAuditorAgent()
    texto_ok = (
        "```python\nplt.plot(x, y)\n```\n\n"
        "Interpretación: el diámetro promedio aumenta con la concentración."
    )
    resultado = auditor.audit_content(texto_ok)
    assert resultado["component_checks"]["Interpretación Post-Gráfico"] is True


def test_conteo_de_palabras_excluye_bloques_de_codigo():
    """H-08: hoy cuenta el documento entero, incluido codigo y tablas."""
    auditor = ContentAuditorAgent()
    texto_con_codigo_largo = "Teoria breve.\n```python\n" + "x = 1\n" * 500 + "```"
    resultado = auditor.audit_content(texto_con_codigo_largo)
    assert resultado["total_words"] < 800
