# Semana 03 - Taxonomía de Inteligencia Artificial 
## Resultado automático frente a clasificación manual de referencia
| Caso | Categoría automática principal | Categorías detectadas | Manual | Estado |
|---|---|---|---|---|
| 1 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 2 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 3 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 4 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 5 | Sistemas de recomendación | Sistemas de recomendación | Sistemas de recomendación | Coincide |
| 6 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 7 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 8 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 9 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 10 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 11 | Visión por computador | Visión por computador | Visión por computador | Coincide |
| 12 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 13 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 14 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |
| 15 | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Aprendizaje automático predictivo | Coincide |
| 16 | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Procesamiento de lenguaje natural | Coincide |
| 17 | Visión por computador | Visión por computador, Robótica y sistemas autónomos | Visión por computador | Coincide |
| 18 | Sistemas expertos | Sistemas expertos | Sistemas expertos | Coincide |
| 19 | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Robótica y sistemas autónomos | Coincide |
| 20 | Búsqueda y optimización | Búsqueda y optimización | Búsqueda y optimización | Coincide |

Coincidencia con la referencia: **100.00%** (20/20).

## Justificación de Mejoras Técnicas
1. **Ponderación de Términos Clave (Pesos Semánticos):** Se modificó la estructura de palabras clave para incluir pesos enteros (de 1 a 3). Términos específicos y complejos de dominios críticos (como *'vehículo autónomo'* o *'diagnóstico'*) reciben mayor peso que palabras generales, reduciendo ambigüedades en la clasificación principal.
2. **Trazabilidad de Puntuación:** El motor calcula una matriz de puntajes por cada categoría evaluada, permitiendo auditorías internas sobre por qué una categoría secundaria obtiene más o menos relevancia frente al problema planteado.
3. **Ampliación de Reglas Personalizadas (`CUSTOM_RULES`):** Se integraron términos de dominio específicos (matrículas, sentimientos, fallas, síntomas y trayectorias) para garantizar una correspondencia más fina con problemas del entorno real.

## Discrepancias y análisis de ingeniería
En los casos donde la clasificación automática difiere de la referencia manual, se observa que los problemas de ingeniería suelen cruzar múltiples fronteras (por ejemplo, robótica que requiere visión por computador o sistemas expertos basados en reglas de negocio). La ponderación ayuda a mitigar falsos positivos, pero se recomienda complementar este motor simbólico con enfoques basados en embeddings o modelos de lenguaje en fases posteriores del proyecto semestral.

## Cinco reglas propias y ampliación de `CUSTOM_RULES`
Se ampliaron las reglas personalizadas integrando términos específicos por dominio para refinar la detección simbólica:
1. **Visión por computador:** Se añadió el término *"matrícula"* (y *"matrículas"*) para capturar con precisión problemas de reconocimiento vehicular en imágenes de seguridad.
2. **Procesamiento de Lenguaje Natural (PLN):** Se incorporó *"sentimiento"* para clasificar de forma directa análisis de opiniones de clientes.
3. **Aprendizaje Automático Predictivo:** Se agregó *"falla"* (y *"fallas"*) para identificar tareas de mantenimiento predictivo en sensores e industria.
4. **Sistemas Expertos:** Se incluyó *"síntoma"* (y *"síntomas"*) para asociarlo correctamente con la sugerencia de diagnósticos médicos basados en conocimiento experto.
5. **Robótica y Sistemas Autónomos:** Se añadió *"trayectoria"* (y *"trayectorias"*) para definir problemas de desplazamiento y control de drones o vehículos autónomos.

## Justificación y Documentación de Mejoras Técnicas Avanzadas

### 1. ¿Qué se hizo? (Modificación arquitectónica)
Se rediseñó el motor de clasificación pasando de un conteo plano de palabras clave a un **sistema de ponderación semántica basado en pesos enteros (del 1 al 3)** dentro de un diccionario estructurado (`dict[str, int]`). Asimismo, se incorporó una matriz de traza para auditar las puntuaciones de todas las categorías evaluadas por caso.

### 2. ¿Para qué se hizo? (Propósito operacional)
* **Evitar falsos positivos y ambigüedades:** En problemas complejos (como el Caso 17, que involucra tanto visión artificial como vehículos autónomos), un conteo simple puede otorgar la misma importancia a palabras genéricas que a conceptos clave del dominio.
* **Controlar la prioridad principal:** Garantizar que los términos críticos o altamente específicos (ej. *"vehículo autónomo"* o *"diagnóstico"*) pesen más en la decisión de la categoría principal frente a términos de soporte.

### 3. ¿Por qué se hizo? 
* **Robustez frente al lenguaje natural:** Los problemas del mundo real rara vez pertenecen de forma aislada a una sola categoría estricta. Un enfoque puramente cuantitativo sin pesos genera sesgos. 
* **Trazabilidad y explicabilidad:** En sistemas inteligentes híbridos, es una buena práctica de ingeniería justificar algorítmicamente por qué un artefacto toma una decisión y cuáles fueron las variables determinantes (pesos), facilitando futuras integraciones con modelos basados en embeddings o aprendizaje profundo en el proyecto semestral.