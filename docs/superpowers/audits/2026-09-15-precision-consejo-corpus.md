# Precision del Consejo contra corpus etiquetado (A3)

**Fecha de ejecucion:** 2026-09-15
**Casos evaluados:** 46 (excluidos por red: 1)

## Matriz de confusion

| | Predicho: tiene fallo | Predicho: no tiene fallo |
|---|---|---|
| **Real: tiene fallo** | VP=12 | FN=15 |
| **Real: no tiene fallo** | FP=17 | VN=2 |

## Metricas

- Precision: 0.41379310344827586
- Recall: 0.4444444444444444
- Kappa de Cohen: -0.4574257425742574

## Desglose por tipo de fallo y origen

| Archivo | Origen | Tipo de fallo | Real | Predicho | Acierto |
|---|---|---|---|---|---|
| neg_01_u7_formula_simbolica.md | real | None | False | True | False |
| neg_02_u4_boxed_concreto.md | real | None | False | True | False |
| neg_03_u3_boxed_porcentual.md | real | None | False | True | False |
| neg_04_u1_ejemplo_doi.md | real | None | False | True | False |
| neg_05_u2_ejemplo_doi.md | real | None | False | True | False |
| neg_06_u3_ejemplo_doi.md | real | None | False | False | True |
| neg_07_u4_ejemplo_doi.md | real | None | False | False | True |
| neg_08_u5_ejemplo_doi.md | real | None | False | True | False |
| neg_09_u6_ejemplo_doi.md | real | None | False | True | False |
| neg_10_u7_ejemplo_doi.md | real | None | False | True | False |
| neg_11_u8_ejemplo_doi.md | real | None | False | True | False |
| neg_12_u1_teoria_dispersion.md | real | None | False | True | False |
| neg_13_u2_teoria_probabilidad.md | real | None | False | True | False |
| neg_14_u5_teoria_jensen.md | real | None | False | True | False |
| neg_15_u6_teoria_generacion.md | real | None | False | True | False |
| neg_17_u4_condicionales.md | real | None | False | True | False |
| neg_18_u7_pruebas_hipotesis.md | real | None | False | True | False |
| neg_19_u3_familias_distribuciones.md | real | None | False | True | False |
| neg_20_u4_convolucion.md | real | None | False | True | False |
| pos_confirmado_01_n01.md | adversarial_previo | falsedad_semantica_y_boxed_desincronizado | True | True | True |
| pos_confirmado_02_n05_marca_decorativa.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_03_n05b_indice.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_04_n05c_integral.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_05_n08_v1.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_06_n08_v2.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_07_n08_v3.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_08_v1_dos_boxed.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_09_v3_theta_sin_rotulo.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_10_v3_dos_boxed.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_11_v4_boxed_con_rotulo.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_confirmado_12_n08_borde_diez.md | adversarial_previo | boxed_desincronizado | True | True | True |
| pos_sintetico_01_varianza_binomial.md | sintetico | varianza_binomial_incorrecta | True | False | False |
| pos_sintetico_02_interseccion_sin_independencia.md | sintetico | interseccion_sin_independencia | True | False | False |
| pos_sintetico_03_suma_masa_igual_a_dos.md | sintetico | suma_masa_probabilidad_incorrecta | True | False | False |
| pos_sintetico_04_desviacion_estandar_negativa.md | sintetico | desviacion_estandar_negativa | True | False | False |
| pos_sintetico_05_tlc_uniforme.md | sintetico | tlc_distribucion_limite_incorrecta | True | False | False |
| pos_sintetico_06_interpretacion_intervalo_confianza.md | sintetico | interpretacion_frecuentista_intervalo_confianza | True | False | False |
| pos_sintetico_07_correlacion_causalidad.md | sintetico | correlacion_implica_causalidad | True | False | False |
| pos_sintetico_08_pvalor_alto_prueba_nula.md | sintetico | pvalor_alto_prueba_hipotesis_nula | True | False | False |
| pos_sintetico_09_media_mediana_siempre_iguales.md | sintetico | media_mediana_siempre_iguales | True | False | False |
| pos_sintetico_10_poisson_media_varianza_distintas.md | sintetico | poisson_media_varianza_distintas | True | False | False |
| pos_sintetico_11_regla_empirica_universal.md | sintetico | regla_empirica_68_95_997_universal | True | False | False |
| pos_sintetico_12_error_estandar_aumenta_con_n.md | sintetico | error_estandar_aumenta_con_n | True | False | False |
| pos_sintetico_13_correlacion_cero_implica_independencia.md | sintetico | correlacion_cero_implica_independencia | True | False | False |
| pos_sintetico_14_exponencial_no_es_sin_memoria.md | sintetico | exponencial_no_es_sin_memoria | True | False | False |
| pos_sintetico_15_bayes_requiere_independencia.md | sintetico | bayes_requiere_independencia | True | False | False |

## Casos excluidos por Crossref inaccesible

`@Librarian` consulta la API de Crossref por red; estos casos citan un DOI real y no se pudieron evaluar honestamente sin conectividad:

- neg_16_u8_proyecto_guia.md