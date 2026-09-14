"""Test de regresión: el badge de tests del README debe coincidir con el
número real de tests recolectados por pytest.

B1 (auditoría 2026-09-13): el badge decía 265 cuando el conteo real era
distinto -mismo defecto que la auditoría anterior ya había señalado con otro
número (226 vs 264)-. Este test convierte el desfase en un fallo de CI
detectable, en vez de un número que hay que recordar actualizar a mano.

Mantenimiento: si este test falla porque `NUMERO_TESTS_ESPERADO` quedó
desactualizado tras agregar/quitar tests, correr
`pytest --collect-only -q | tail -1` y actualizar la constante Y el
badge de README.md en el mismo commit que agrega/quita el test.
"""

import re
from pathlib import Path

_BADGE_PATTERN = re.compile(r"tests-(\d+)%20passing")

# Actualizar junto con el badge de README.md cada vez que cambie el
# número de tests del repo. Verificar con: pytest --collect-only -q | tail -1
NUMERO_TESTS_ESPERADO = 276


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
