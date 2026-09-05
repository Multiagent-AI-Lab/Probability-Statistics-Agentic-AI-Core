"""
QAAgent (@QA): Supreme Quality Auditor for the 8 mandatory components and Protocolo Maestro.
"""

from typing import Any

SEVERIDAD_BLOQUEANTE = "bloqueante"
SEVERIDAD_ADVERTENCIA = "advertencia"

# Categorías de hallazgo del dominio. Cada una nombra un problema concreto
# de contenido, de modo que el reporte diga QUÉ está mal y no solo que
# algún agente devolvió False.
TIPO_DESAJUSTE_EJEMPLO_SALIDA = "desajuste_ejemplo_salida"
TIPO_INVARIANTE_VIOLADO = "invariante_violado"
TIPO_ARITMETICA_INCONSISTENTE = "aritmetica_inconsistente"
TIPO_SUPUESTO_NO_VERIFICADO = "supuesto_no_verificado"
TIPO_REFERENCIA_INEXISTENTE = "referencia_inexistente"
TIPO_INTERPRETACION_AUSENTE = "interpretacion_ausente"
TIPO_TEORIA_INSUFICIENTE = "teoria_insuficiente"
TIPO_ERROR_DE_EJECUCION = "error_de_ejecucion"
TIPO_FALLO_SIN_CLASIFICAR = "fallo_sin_clasificar"


class QAAgent:
    """Supreme Auditor Agent verifying final approval for publication."""

    def final_audit(self, council_reports: dict[str, Any]) -> dict[str, Any]:
        """Decide sobre hallazgos tipados, no sobre un AND de banderas.

        H-01: el criterio anterior era
        `all(rep.get("passed", False) for rep in reports)`, que colapsa todo
        el trabajo del Consejo en un booleano —sin decir qué falló, sin
        distinguir un error de contenido de un aviso pedagógico, y
        aprobando en bloque cuando cada agente aprobaba por su cuenta con
        criterios de subcadena.

        Ahora cada reporte se traduce a hallazgos `{tipo, severidad, agente,
        mensaje}` y la publicación se bloquea solo si hay al menos uno
        bloqueante. Las advertencias (supuestos estadísticos sin verificar,
        p. ej.) se reportan sin bloquear: informan al autor sin convertir
        cada aviso menor en un gate de publicación.
        """
        hallazgos: list[dict[str, Any]] = []
        for agente, reporte in council_reports.items():
            hallazgos.extend(self._clasificar(agente, reporte))

        resumen = {
            SEVERIDAD_BLOQUEANTE: sum(
                1 for h in hallazgos if h["severidad"] == SEVERIDAD_BLOQUEANTE
            ),
            SEVERIDAD_ADVERTENCIA: sum(
                1 for h in hallazgos if h["severidad"] == SEVERIDAD_ADVERTENCIA
            ),
        }

        return {
            "approved": resumen[SEVERIDAD_BLOQUEANTE] == 0,
            "hallazgos": hallazgos,
            "resumen": resumen,
            "reports": council_reports,
        }

    def _clasificar(self, agente: str, reporte: Any) -> list[dict[str, Any]]:
        """Traduce el reporte de un agente a hallazgos tipados."""
        if not isinstance(reporte, dict):
            return [
                self._hallazgo(
                    TIPO_FALLO_SIN_CLASIFICAR,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    "el agente no devolvió un reporte interpretable",
                )
            ]

        # Un agente advisory (@Architect fuera del flujo por lección) no
        # audita esta lección: no aporta hallazgos ni bloquea.
        if reporte.get("skipped"):
            return []

        hallazgos: list[dict[str, Any]] = []

        for invariante in reporte.get("invariantes_violados", []):
            hallazgos.append(
                self._hallazgo(
                    TIPO_INVARIANTE_VIOLADO,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    f"invariante estadístico violado: {invariante}",
                )
            )

        for inconsistencia in reporte.get("aritmetica_inconsistente", []):
            hallazgos.append(
                self._hallazgo(
                    TIPO_ARITMETICA_INCONSISTENTE,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    inconsistencia,
                )
            )

        for discrepancia in reporte.get("discrepancias", []):
            hallazgos.append(
                self._hallazgo(
                    TIPO_DESAJUSTE_EJEMPLO_SALIDA,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    (
                        f"el texto declara {discrepancia.get('valor_declarado')} "
                        f"en {discrepancia.get('seccion')}, pero el código produce "
                        f"{discrepancia.get('valores_producidos')}"
                    ),
                )
            )

        for error in reporte.get("errores_de_ejecucion", []):
            hallazgos.append(
                self._hallazgo(
                    TIPO_ERROR_DE_EJECUCION,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    (
                        f"el código de {error.get('seccion')} no se pudo "
                        f"ejecutar: {error.get('error')}"
                    ),
                )
            )

        for doi in reporte.get("dois_no_resueltos", []):
            hallazgos.append(
                self._hallazgo(
                    TIPO_REFERENCIA_INEXISTENTE,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    f"el DOI citado no resuelve: {doi}",
                )
            )

        # Los warnings del Safety Gate son pedagógicos salvo que el propio
        # agente los marque como críticos (anacronismo curricular).
        severidad_gate = (
            SEVERIDAD_BLOQUEANTE if reporte.get("critical") else SEVERIDAD_ADVERTENCIA
        )
        for warning in reporte.get("warnings", []):
            hallazgos.append(
                self._hallazgo(
                    TIPO_SUPUESTO_NO_VERIFICADO, severidad_gate, agente, warning
                )
            )

        for warning in reporte.get("monte_carlo_warnings", []):
            hallazgos.append(
                self._hallazgo(
                    TIPO_SUPUESTO_NO_VERIFICADO,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    warning,
                )
            )

        if reporte.get("has_interpretation") is False:
            hallazgos.append(
                self._hallazgo(
                    TIPO_INTERPRETACION_AUSENTE,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    "falta interpretación posterior a la visualización",
                )
            )

        if reporte.get("tiene_formulas_estructuradas") is False:
            hallazgos.append(
                self._hallazgo(
                    TIPO_TEORIA_INSUFICIENTE,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    "no hay fórmulas LaTeX con estructura matemática real",
                )
            )

        # Red de seguridad: un agente que reprueba sin exponer un detalle
        # tipado sigue bloqueando. Nunca se aprueba por no saber clasificar.
        if not reporte.get("passed", False) and not hallazgos:
            hallazgos.append(
                self._hallazgo(
                    TIPO_FALLO_SIN_CLASIFICAR,
                    SEVERIDAD_BLOQUEANTE,
                    agente,
                    "el agente reprobó sin detallar el motivo",
                )
            )

        return hallazgos

    @staticmethod
    def _hallazgo(
        tipo: str, severidad: str, agente: str, mensaje: str
    ) -> dict[str, Any]:
        return {
            "tipo": tipo,
            "severidad": severidad,
            "agente": agente,
            "mensaje": mensaje,
        }
