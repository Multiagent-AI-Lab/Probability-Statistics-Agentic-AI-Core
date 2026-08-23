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

Desde 2026-08, `StatsTutorAgent` indexa estos PDFs automáticamente en una
colección ChromaDB separada (`bibliografia_pdfs`), distinta de la colección
de lecciones (`lecciones_probabilidad`). La indexación ocurre la primera
vez que se instancia el agente (`collection.count() > 0` evita reprocesar
en instancias siguientes) y usa `pdf_indexer.py` (extracción con `pypdf`,
chunking por página).

`_search_local_docs` combina 2 resultados de lecciones + 1 de bibliografía
en cada consulta, para que el contexto de las lecciones del curso nunca
quede ahogado por el volumen de los libros completos (ver
`docs/superpowers/specs/2026-08-21-indexacion-bibliografia-pdfs-design.md`
para el razonamiento completo).

Un PDF escaneado (sin texto seleccionable) o corrupto se omite sin
detener la indexación de los demás — se loguea como warning/error.

Esto es distinto del RAG de DOIs citados inline en las lecciones (ver
sección anterior): aquél indexa abstracts de Crossref por DOI citado, este
indexa el texto completo de los libros de esta carpeta.

## Por qué está gitignored

Los PDFs de libros de texto tienen copyright — mismo criterio que `raw_student_notebooks/` (privacidad) y `docs/legado/` (material institucional): se conservan localmente para uso del curso, nunca se publican en el repo público.
