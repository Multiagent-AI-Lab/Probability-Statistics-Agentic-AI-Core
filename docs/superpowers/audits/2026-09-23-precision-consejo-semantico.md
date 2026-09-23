# Precision del SemanticAuditorAgent (corpus adversarial semantico)

**Fecha de ejecucion:** 2026-09-23
**Casos evaluados:** 16

Primera medicion del 9no agente del Consejo (el unico con LLM), contra
inversion semantica y constante falsa -- la brecha que
`docs/superpowers/audits/2026-09-23-precision-consejo-unidades.md`
documenta como limite conocido del resto del Consejo (heuristico puro).

## Matriz de confusion (agregada, ambos tipos de fallo)

| | Predicho: tiene fallo | Predicho: no tiene fallo |
|---|---|---|
| **Real: tiene fallo** | VP=3 | FN=5 |
| **Real: no tiene fallo** | FP=3 | VN=5 |

## Metricas

- Precision: 0.5
- Recall: 0.375

## Desglose por caso

| Archivo | Unidad origen | Tipo de fallo | Real | Predicho | Acierto | Auditoria incompleta |
|---|---|---|---|---|---|---|
| neg_u1_estadistica_descriptiva.md | UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md | None | False | True | False | False |
| neg_u2_probabilidad_combinatoria.md | UNIDAD_2_PROBABILIDAD_COMBINATORIA.md | None | False | True | False | False |
| neg_u3_variables_discretas.md | UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md | None | False | False | True | False |
| neg_u4_distribuciones_conjuntas.md | UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md | None | False | False | True | False |
| neg_u5_variables_continuas.md | UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md | None | False | True | False | False |
| neg_u6_modelado_simulacion.md | UNIDAD_6_MODELADO_SIMULACION.md | None | False | False | True | False |
| neg_u7_inferencia_estimacion.md | UNIDAD_7_INFERENCIA_ESTIMACION.md | None | False | False | True | False |
| neg_u8_proyecto_integrador.md | UNIDAD_8_PROYECTO_INTEGRADOR.md | None | False | False | True | False |
| pos_inversion_u1_estadistica_descriptiva.md | UNIDAD_1_ESTADISTICA_DESCRIPTIVA.md | inversion_semantica | True | True | True | False |
| pos_inversion_u2_probabilidad_combinatoria.md | UNIDAD_2_PROBABILIDAD_COMBINATORIA.md | inversion_semantica | True | False | False | False |
| pos_inversion_u3_variables_discretas.md | UNIDAD_3_VARIABLES_ALEATORIAS_DISCRETAS.md | inversion_semantica | True | False | False | False |
| pos_inversion_u4_distribuciones_conjuntas.md | UNIDAD_4_DISTRIBUCIONES_CONJUNTAS.md | inversion_semantica | True | True | True | False |
| pos_inversion_u5_variables_continuas.md | UNIDAD_5_VARIABLES_ALEATORIAS_CONTINUAS.md | inversion_semantica | True | True | True | False |
| pos_inversion_u6_modelado_simulacion.md | UNIDAD_6_MODELADO_SIMULACION.md | inversion_semantica | True | False | False | False |
| pos_inversion_u7_inferencia_estimacion.md | UNIDAD_7_INFERENCIA_ESTIMACION.md | inversion_semantica | True | False | False | False |
| pos_inversion_u8_proyecto_integrador.md | UNIDAD_8_PROYECTO_INTEGRADOR.md | inversion_semantica | True | False | False | False |
