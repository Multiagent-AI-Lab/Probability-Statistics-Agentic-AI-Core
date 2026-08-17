"""
Socratic Debugger Skill: Generates guided questions when student code or analysis has errors.
"""

class SocraticDebugger:
    """Skill for generating Socratic pedagogical feedback."""

    def generate_socratic_question(self, error_type: str, context: str) -> str:
        error_type_lower = error_type.lower()
        if "normality" in error_type_lower:
            return "¿Por qué es fundamental verificar la simetría y normalidad de los datos antes de aplicar una prueba t de Student?"
        elif "p_value" in error_type_lower:
            return "Si obtienes un p-valor de 0.03 con alpha = 0.05, ¿qué decisión tomas respecto a H0 y qué representa físicamente ese 0.03?"
        elif "variance" in error_type_lower:
            return "¿Qué diferencia existe entre evaluar la dispersión con la varianza frente al coeficiente de variación al comparar unidades distintas?"
        elif "zerodivisionerror" in error_type_lower:
            return (
                "Antes de darte la respuesta: revisa tu código. ¿Estás dividiendo entre "
                "una desviación estándar o un tamaño de muestra que podría valer cero? "
                f"Piensa en el contexto de {context}: ¿validaste el denominador antes "
                "de la operación?"
            )
        elif "indexerror" in error_type_lower:
            return (
                "Antes de darte la respuesta: ¿estás accediendo a una posición de un "
                "arreglo de mediciones sin verificar antes su tamaño? Revisa si usaste "
                "`len(tu_arreglo)` para confirmar que el índice existe."
            )
        elif "syntax_error" in error_type_lower or "syntaxerror" in error_type_lower:
            return (
                "Antes de darte la respuesta: revisa la llamada a la función de "
                "`scipy.stats` que usaste — ¿coinciden los paréntesis y las comas "
                "con la firma real de la función? Consulta la documentación oficial "
                "si tienes dudas del orden de los parámetros."
            )
        else:
            return f"Revisa el desarrollo del paso actual: ¿concuerdan las unidades y supuestos en {context}?"
