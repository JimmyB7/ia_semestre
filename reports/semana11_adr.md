# ADR Semana 11 - Selección de Modelo

## Contexto
Se requiere seleccionar el modelo óptimo de clasificación evaluando exactitud, costo de entrenamiento y mantenibilidad sobre el conjunto de datos de dígitos.

## Opciones Evaluadas
- **Logistic Regression**: Línea base rápida y altamente explicable.
- **Random Forest**: Ensamble no lineal con alta capacidad predictiva.
- **MLPClassifier**: Red neuronal multicapa con representación compleja.

## Evidencia
Los resultados registrados en `artifacts/benchmark.csv` muestran la comparación bajo el mismo protocolo de evaluación.

## Decisión
Se selecciona **Random Forest** (o la opción de mejor desempeño) al ofrecer el balance óptimo entre exactitud (*accuracy*) y tiempo de entrenamiento (*fit_seconds*).

## Consecuencias
- **Ventajas**: Alta precisión sin requerir escalado complejo.
- **Riesgos/Puntos a vigilar**: Mayor consumo de memoria al aumentar el número de árboles.