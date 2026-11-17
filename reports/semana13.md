# Reporte Semana 13 - Motor de Inferencia

## Objetivo

Implementar un motor de inferencia basado en reglas que derive nuevos hechos a partir de hechos iniciales y permita seguir qué reglas se aplicaron.

## Implementación

En `src/semana13_motor_inferencia.py` se definió la clase inmutable `Regla`, compuesta por un nombre, un conjunto de premisas y una conclusión. La función `inferir` copia los hechos iniciales y recorre las reglas repetidamente. Cuando todas las premisas de una regla están presentes y su conclusión aún no existe, agrega esa conclusión y registra el nombre de la regla aplicada. El proceso termina cuando ya no se derivan hechos nuevos.

Se modeló un flujo de autorización de matrícula:

1. `R1`: identidad validada y documentos recibidos permiten concluir que el expediente está completo.
2. `R2`: expediente completo y prerrequisitos aprobados permiten habilitar la inscripción.
3. `R3`: inscripción habilitada y cupo disponible permiten autorizar la matrícula.

## Pruebas y resultados

Las pruebas de `src/semana13_test_motor_inferencia.py` cubren dos escenarios:

- **Demostración exitosa:** con todos los hechos necesarios, el motor deriva `matricula_autorizada` y registra las reglas `R1`, `R2` y `R3` en orden.
- **Demostración incompleta:** sin el hecho `cupo_disponible`, no autoriza la matrícula y la traza contiene solamente `R1` y `R2`.

**Resultado:** las 2 pruebas del motor de inferencia finalizaron correctamente.

## Resultado del trabajo

Se obtuvo un mecanismo sencillo de encadenamiento hacia adelante que produce conclusiones y conserva una traza de las reglas usadas. El ejemplo muestra cómo representar decisiones encadenadas mediante hechos y reglas explícitas.
