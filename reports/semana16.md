# Reporte Semana 16 - Motor de Referencia Académica

## Objetivo

Implementar un motor que consulta respuestas académicas validadas a partir de palabras clave y evita ofrecer información que no tenga respaldo en la base de conocimiento.

## Implementación

En `src/semana16_motor_referencia.py` se creó una función para normalizar las consultas y otra para buscar la referencia más pertinente. La base de producción inicia vacía y el motor devuelve `SIN_REFERENCIA` hasta que se agreguen respuestas con fuentes validadas; los datos de las pruebas son únicamente ejemplos.

La función `normalizar` convierte el texto a minúsculas, elimina las tildes y separa las palabras alfanuméricas. Esto permite comparar consultas sin distinguir mayúsculas, acentos o signos de puntuación.

La función `consultar_referencia` realiza las siguientes acciones:

- Normaliza la pregunta recibida.
- Descarta entradas vacías o compuestas únicamente por signos de puntuación.
- Revisa solamente las referencias marcadas como `validada=True`.
- Calcula el número de coincidencias entre la pregunta y las claves de cada referencia.
- Ordena los candidatos por mayor puntuación y, ante un empate, por identificador ascendente.
- Devuelve una respuesta validada con su identificador, fuente y puntuación.
- Devuelve `SIN_REFERENCIA` cuando no hay coincidencias o la entrada no contiene palabras utilizables.

El sistema incluye un ejemplo interactivo en `src/app.py`. Al ejecutar el programa, el usuario puede realizar consultas desde la consola hasta escribir `salir`.

## Pruebas

Las pruebas de `test/test_motor.py` cubren los siguientes casos:

- Consulta encontrada con coincidencia entre palabras clave y pregunta.
- Normalización de mayúsculas y tildes.
- Exclusión de una referencia no validada.
- Pregunta fuera de la cobertura de la base.
- Entrada vacía o formada únicamente por signos de puntuación.

Las pruebas verifican el estado de la respuesta, el identificador, la puntuación y el resultado `None` cuando no existe una referencia válida.

## Resultado del trabajo

Se implementó un motor de búsqueda por coincidencia léxica sobre referencias validadas. El tratamiento de mayúsculas y tildes mejora la robustez de las consultas, mientras que el manejo de entradas sin evidencia evita presentar respuestas no respaldadas.
