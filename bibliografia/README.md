# Bibliografía

Carpeta local (gitignored, no se publica en GitHub) para PDFs de referencias académicas del curso — libros de texto con copyright, no material de dominio propio del repo.

## Qué va aquí

Los libros de texto citados en la sección `## Referencias` de las 8 lecciones (`lecciones/UNIDAD_*.md`), ver `RUBRICA_GENERAL.md` y `PROTOCOLO_MAESTRO.md` para el criterio de bibliografía exigido. Referencias base del programa oficial (`docs/legado/Anexo 8- Planeación didáctica_..._extracted.txt`, Sección 8) y las agregadas durante el plan de uniformización de contenido (2026-08-15):

- Ross, S. — *A First Course in Probability*
- Wasserman, L. — *All of Statistics*
- Casella, G. & Berger, R. — *Statistical Inference*
- Montgomery, D. C. & Runger, G. C. — *Applied Statistics and Probability for Engineers*
- Walpole, R. E. et al. — *Probabilidad y estadística para ingeniería y ciencias* (bibliografía oficial del Anexo 8)

## Convención de nombre de archivo

`Apellido_Año_TituloCorto.pdf` (ej. `Wasserman_2004_AllOfStatistics.pdf`) — facilita que `StatsTutorAgent` (o cualquier script de indexado futuro) pueda referenciar la fuente por nombre de archivo sin depender de metadatos internos del PDF.

## Uso con `StatsTutorAgent`

Esta carpeta **sigue sin indexarse automáticamente** — `StatsTutorAgent._get_markdown_files()` solo lee `lecciones/*.md`, y ningún código de este repo abre ni extrae texto de los PDFs de `bibliografia/`. Indexar estos PDFs (extracción de texto + chunking) sigue siendo una extensión futura fuera de alcance.

**Distinto (y ya implementado desde 2026-08) es el RAG sobre DOIs citados en las lecciones**: `StatsTutorAgent._build_index()` extrae los DOIs en formato `DOI: [10.xxxx/yyyy](url)` de cada `UNIDAD_*.md`, consulta el abstract público de cada uno vía la API de Crossref (`_fetch_abstract`), y lo indexa en ChromaDB como contexto adicional para las respuestas de Gemini — sin necesidad de tener el PDF local. Es el mismo patrón que `TutorAgent` de Programming-Logic. Esto cubre los DOIs citados inline en el texto (una referencia específica por unidad, agregada en 2026-08), no los libros completos de esta carpeta.

## Por qué está gitignored

Los PDFs de libros de texto tienen copyright — mismo criterio que `raw_student_notebooks/` (privacidad) y `docs/legado/` (material institucional): se conservan localmente para uso del curso, nunca se publican en el repo público.
