"""Test de regresión: el badge de tests del README debe coincidir con el
número real de tests recolectados por pytest.

B1 (auditoría 2026-09-13): el badge decía 265 cuando el conteo real era
distinto -mismo defecto que la auditoría anterior ya había señalado con otro
número (226 vs 264)-. Corregido entonces a 276 con este mismo test, pero se
desincronizó DE NUEVO dentro del propio plan que lo cerró: las Tasks 6, 9 y
10 (posteriores a la Task que fijó 276) agregaron 4 tests más (280 reales),
y nadie reajustó la constante ni el badge -- el gate comparaba README contra
sí mismo, nunca contra pytest, así que pasaba en verde con ambos números
desactualizados. Encontrado en la revisión final de rama del plan
`camino-a-100-cierre-brechas` (2026-09-14).

`session.testscollected`/`session.items` no sirven para un gate autónomo:
reflejan solo lo seleccionado tras `-k`/`-m`/un solo archivo, así que un
test que se apoye en ellos ve "1" al correr aislado -- se probó y se
descartó por esto mismo. La única forma de comparar contra el conteo REAL
de toda la suite sin un subproceso pytest anidado (frágil, la razón por la
que el diseño original ya lo evitaba) sigue siendo una constante mantenida
a mano. La mitigación real no es técnica sino de proceso: este test debe
correr como PARTE de `pytest tests/ -v` (nunca aislado) para que su
constante quede bajo la misma disciplina de "actualízala en el commit que
cambia el conteo" -- documentado aquí con la mayor claridad posible tras
haber fallado dos veces ya.

Mantenimiento: si este test falla porque `NUMERO_TESTS_ESPERADO` quedó
desactualizado, correr `pytest --collect-only -q | tail -1` y actualizar
la constante Y el badge de README.md en el mismo commit que agrega/quita
un test -- sin excepción, incluyendo tareas que parezcan no relacionadas
con testing (agregar un test de regresión para OTRA cosa también cambia
este número).

B1' (auditoría 2026-09-14): este test local sigue siendo estructuralmente
tautológico -compara README contra una constante mantenida a mano, nunca
contra pytest- y así se documenta arriba con toda intención. El gate REAL
contra el conteo real de pytest vive en CI (`.github/workflows/ci.yml`,
step "Verify README test badge matches real count"), que si compara
`pytest --collect-only` contra el badge en cada push/PR. Este test local
solo confirma que la constante y el badge coinciden ENTRE SÍ -si alguien
actualiza uno sin el otro, esto lo detecta; si ambos quedan
desactualizados por igual respecto al conteo real, el gate de CI lo
detecta.
"""

import re
from pathlib import Path

_BADGE_PATTERN = re.compile(r"tests-(\d+)%20passing")

# Actualizar junto con el badge de README.md cada vez que cambie el
# número de tests del repo. Verificar con: pytest --collect-only -q | tail -1
NUMERO_TESTS_ESPERADO = 380


def test_badge_de_tests_coincide_con_el_conteo_esperado():
    readme = Path(__file__).resolve().parents[1] / "README.md"
    contenido = readme.read_text(encoding="utf-8")
    match = _BADGE_PATTERN.search(contenido)
    assert match is not None, "no se encontró el badge de tests en README.md"
    numero_badge = int(match.group(1))
    assert numero_badge == NUMERO_TESTS_ESPERADO, (
        f"badge dice {numero_badge}, se esperaba {NUMERO_TESTS_ESPERADO} "
        "-- si agregaste/quitaste tests, actualiza esta constante Y el "
        "badge de README.md en el mismo commit"
    )
