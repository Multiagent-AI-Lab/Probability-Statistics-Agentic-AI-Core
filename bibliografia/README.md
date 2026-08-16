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

Esta carpeta NO se indexa automáticamente todavía — `StatsTutorAgent._get_markdown_files()` solo lee `lecciones/*.md`. Indexar PDFs de esta carpeta (extracción de texto + chunking) es una extensión futura, fuera del alcance del plan `docs/superpowers/plans/2026-08-15-uniformizacion-agentes-y-contenido.md` (Task 7 implementa el RAG sobre `lecciones/*.md` únicamente, siguiendo el mismo patrón que `TutorAgent` de Programming-Logic, que tampoco indexa PDFs locales — solo abstracts de DOIs vía Crossref).

## Por qué está gitignored

Los PDFs de libros de texto tienen copyright — mismo criterio que `raw_student_notebooks/` (privacidad) y `docs/legado/` (material institucional): se conservan localmente para uso del curso, nunca se publican en el repo público.
