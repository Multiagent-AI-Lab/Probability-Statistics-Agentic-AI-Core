# Bibliografía

## Qué va aquí

Los libros de texto citados en la sección `## Referencias` de las 8 lecciones (`lecciones/UNIDAD_*.md`), ver `RUBRICA_GENERAL.md` y `PROTOCOLO_MAESTRO.md` para el criterio de bibliografía exigido. PDFs actualmente presentes en esta carpeta:

- *Ciencia de Datos* (2018)
- *Foundations of Statistics for Data Scientists: With R and Python* (Chapman & Hall/CRC Texts in Statistical Science)
- *Introduction to Probability for Data Science*
- *Introduction to Statistical Methods, Design of Experiments and Statistical Quality Control*
- *Mathematics for Machine Learning*
- *Numerical Python: Scientific Computing and Data Science Applications with NumPy, SciPy and Matplotlib*
- *Practical Statistics for Data Scientists: 50 Essential Concepts Using R and Python* (Peter Bruce, Andrew Bruce, Peter Gedeck)
- *Probabilistic Machine Learning: An Introduction*
- *Python for Probability, Statistics, and Machine Learning*

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
