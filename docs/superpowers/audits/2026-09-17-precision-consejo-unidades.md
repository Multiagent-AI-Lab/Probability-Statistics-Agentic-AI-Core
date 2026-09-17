# Precision del Consejo contra unidades completas (A3-U)

> **⚠️ CIFRA INVALIDA -- NO CITAR.** Los 8 negativos de esta corrida dieron falso positivo por un bug de infraestructura (crash nativo `0xC0000005` en `scipy.linalg.cholesky` vía `scipy.stats.gaussian_kde`, disparado por `seaborn.histplot(kde=True)` en `UNIDAD_1`/otras unidades reales -- confirmado con `faulthandler`, no relacionado con el contenido del corpus ni con el mecanismo de deteccion del Consejo). Precision/recall/kappa de este reporte NO miden el comportamiento real del Consejo. Ver ledger de `docs/superpowers/plans/2026-09-17-a3-unidades-completas-plan.md` (Task 6/6b) y memoria persistente para el diagnostico completo. Este reporte se conserva como evidencia del bloqueo, no como resultado valido de A3-U -- Task 6 debe re-ejecutarse una vez resuelto el bug de scipy/OpenBLAS.

**Fecha de ejecucion:** 2026-09-17
**Casos evaluados:** 16 (excluidos por red: 0)

Complementario a A3 (`docs/superpowers/audits/2026-09-16-precision-consejo-corpus.md`), que mide contra fragmentos recortados de las 8 unidades. A3-U mide especificamente deteccion de `boxed_desincronizado` (el unico tipo de fallo del catalogo de A3 con mecanismo real confirmado en `_contraste_boxed.py`) sobre unidades completas sin recortar. No es comparable 1:1 con la cifra global de A3 -- ver GOVERNANCE.md SS5.1/D6 para la comparacion completa.

## Matriz de confusion

| | Predicho: tiene fallo | Predicho: no tiene fallo |
|---|---|---|
| **Real: tiene fallo** | VP=8 | FN=0 |
| **Real: no tiene fallo** | FP=8 | VN=0 |

## Metricas

- Precision: 0.5
- Recall: 1.0
- Kappa de Cohen: 0.0

## Desglose por unidad de origen

| Archivo | Unidad origen | Tipo de fallo | Real | Predicho | Acierto |
|---|---|---|---|---|---|
| neg_u1_estadistica_descriptiva.md | UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md | None | False | True | False |
| neg_u2_probabilidad_combinatoria.md | UNIDAD_2_PROBABILIDAD_COMBINATORIA.md | None | False | True | False |
| neg_u3_variables_discretas.md | UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md | None | False | True | False |
| neg_u4_distribuciones_conjuntas.md | UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md | None | False | True | False |
| neg_u5_variables_continuas.md | UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md | None | False | True | False |
| neg_u6_modelado_simulacion.md | UNIDAD_6_MODELADO_SIMULACION.md | None | False | True | False |
| neg_u7_inferencia_estimacion.md | UNIDAD_7_INFERENCIA_ESTIMACION.md | None | False | True | False |
| neg_u8_proyecto_integrador.md | UNIDAD_8_PROYECTO_INTEGRADOR.md | None | False | True | False |
| pos_u1_estadistica_descriptiva.md | UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md | boxed_desincronizado | True | True | True |
| pos_u2_probabilidad_combinatoria.md | UNIDAD_2_PROBABILIDAD_COMBINATORIA.md | boxed_desincronizado | True | True | True |
| pos_u3_variables_discretas.md | UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md | boxed_desincronizado | True | True | True |
| pos_u4_distribuciones_conjuntas.md | UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md | boxed_desincronizado | True | True | True |
| pos_u5_variables_continuas.md | UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md | boxed_desincronizado | True | True | True |
| pos_u6_modelado_simulacion.md | UNIDAD_6_MODELADO_SIMULACION.md | boxed_desincronizado | True | True | True |
| pos_u7_inferencia_estimacion.md | UNIDAD_7_INFERENCIA_ESTIMACION.md | boxed_desincronizado | True | True | True |
| pos_u8_proyecto_integrador.md | UNIDAD_8_PROYECTO_INTEGRADOR.md | boxed_desincronizado | True | True | True |