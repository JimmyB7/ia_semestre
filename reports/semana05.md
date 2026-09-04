# Semana 05 - Sistema Híbrido de Soporte Técnico

## Resultados de las Consultas de Prueba

### Consulta 1: "El equipo esta muy caliente y el ventilador hace ruido"
- **Reglas disparadas:** `revisar_ventilacion`
- **Evidencia recuperada:** Si el ventilador del computador hace ruido fuerte limpie el polvo acumulado y verifique que no haya obstrucciones.
- **Similitud Coseno (TF-IDF):** `0.425`
- **Clase predicha:** `hardware`

### Consulta 2: "Internet se cae continuamente y aparece un fallo DNS en la red"
- **Reglas disparadas:** `revisar_conectividad`
- **Evidencia recuperada:** Si la red o internet se caen con frecuencia verifique la configuracion DNS la direccion IP y los cables del router.
- **Similitud Coseno (TF-IDF):** `0.453`
- **Clase predicha:** `red`

### Consulta 3: "No puedo iniciar sesion con mi cuenta porque olvide la clave"
- **Reglas disparadas:** `revisar_acceso`
- **Evidencia recuperada:** Si no puede iniciar sesion o su cuenta esta bloqueada revise los permisos del usuario la clave y la autenticacion.
- **Similitud Coseno (TF-IDF):** `0.579`
- **Clase predicha:** `seguridad`

## Análisis de Trazabilidad y Limitaciones
- **Explicabilidad:** El sistema no solo arroja una clase categórica, sino que justifica su decisión mediante reglas simbólicas directas y evidencia textual de la base de conocimiento.
- **Limitaciones:** Con pocos ejemplos de entrenamiento (15 frases), la regresión logística puede errar en textos ambiguos. Además, la búsqueda TF-IDF depende de coincidencias léxicas exactas o raíces compartidas, por lo que sinónimos no incluidos en la base documental podrían bajar la puntuación de similitud.