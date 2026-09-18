# Precision del Consejo contra unidades completas (A3-U)

**Fecha de ejecucion:** 2026-09-18
**Casos evaluados:** 16 (excluidos por red: 0)

Complementario a A3 (`docs/superpowers/audits/2026-09-16-precision-consejo-corpus.md`), que mide contra fragmentos recortados de las 8 unidades. A3-U mide especificamente deteccion de `boxed_desincronizado` (el unico tipo de fallo del catalogo de A3 con mecanismo real confirmado en `_contraste_boxed.py`) sobre unidades completas sin recortar. No es comparable 1:1 con la cifra global de A3 -- ver GOVERNANCE.md SS5.1/D6 para la comparacion completa.

## Matriz de confusion

| | Predicho: tiene fallo | Predicho: no tiene fallo |
|---|---|---|
| **Real: tiene fallo** | VP=4 | FN=4 |
| **Real: no tiene fallo** | FP=0 | VN=8 |

## Metricas

- Precision: 1.0
- Recall: 0.5
- Kappa de Cohen: 0.5

## Desglose por unidad de origen

| Archivo | Unidad origen | Tipo de fallo | Real | Predicho | Acierto |
|---|---|---|---|---|---|
| neg_u1_estadistica_descriptiva.md | UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md | None | False | False | True |
| neg_u2_probabilidad_combinatoria.md | UNIDAD_2_PROBABILIDAD_COMBINATORIA.md | None | False | False | True |
| neg_u3_variables_discretas.md | UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md | None | False | False | True |
| neg_u4_distribuciones_conjuntas.md | UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md | None | False | False | True |
| neg_u5_variables_continuas.md | UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md | None | False | False | True |
| neg_u6_modelado_simulacion.md | UNIDAD_6_MODELADO_SIMULACION.md | None | False | False | True |
| neg_u7_inferencia_estimacion.md | UNIDAD_7_INFERENCIA_ESTIMACION.md | None | False | False | True |
| neg_u8_proyecto_integrador.md | UNIDAD_8_PROYECTO_INTEGRADOR.md | None | False | False | True |
| pos_u1_estadistica_descriptiva.md | UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md | boxed_desincronizado | True | False | False |
| pos_u2_probabilidad_combinatoria.md | UNIDAD_2_PROBABILIDAD_COMBINATORIA.md | boxed_desincronizado | True | True | True |
| pos_u3_variables_discretas.md | UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md | boxed_desincronizado | True | False | False |
| pos_u4_distribuciones_conjuntas.md | UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md | boxed_desincronizado | True | True | True |
| pos_u5_variables_continuas.md | UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md | boxed_desincronizado | True | False | False |
| pos_u6_modelado_simulacion.md | UNIDAD_6_MODELADO_SIMULACION.md | boxed_desincronizado | True | True | True |
| pos_u7_inferencia_estimacion.md | UNIDAD_7_INFERENCIA_ESTIMACION.md | boxed_desincronizado | True | False | False |
| pos_u8_proyecto_integrador.md | UNIDAD_8_PROYECTO_INTEGRADOR.md | boxed_desincronizado | True | True | True |