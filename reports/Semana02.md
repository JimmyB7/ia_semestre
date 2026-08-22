# Informe Técnico: Análisis de Clasificación de Datos con Iris (Semana 02)

## 1. Introducción
Este informe detalla el procedimiento técnico realizado durante la **Semana 02** de actividades, enfocado en la implementación de un modelo de aprendizaje automático (Machine Learning) para la clasificación de especies de flores basado en el conjunto de datos *Iris*. El objetivo de esta actividad fue establecer una base reproducible y estructurada para tareas de clasificación supervisada.

## 2. Metodología
El proceso siguió los estándares de ingeniería de software y ciencia de datos, estructurándose en las siguientes fases:
- **Preparación de Datos:** Carga del dataset, división en subconjuntos de entrenamiento y prueba (80/20), y estandarización de características mediante `StandardScaler`.
- **Modelado:** Entrenamiento de un clasificador supervisado implementado en la actividad de la semana.
- **Evaluación:** Cálculo de la exactitud (accuracy) y generación de la matriz de confusión para visualizar el rendimiento predictivo del modelo.

## 3. Configuración del Entorno
Para garantizar la reproducibilidad de los resultados de la semana, se utilizó el entorno virtual configurado previamente con Python 3.13, gestionando las dependencias necesarias (`numpy`, `pandas`, `scikit-learn`, `matplotlib`) mediante el archivo `requirements.txt`.

## 4. Resultados
| Métrica | Descripción |
| :--- | :--- |
| **Accuracy** | Porcentaje de aciertos sobre el total de muestras de prueba. |
| **Matriz de Confusión** | Distribución de aciertos y errores por clase. |

## 5. Conclusiones
La implementación realizada en esta **Semana 02** fue exitosa, permitiendo validar el flujo de trabajo básico. Los resultados obtenidos confirman la eficacia del preprocesamiento para este conjunto de datos, sirviendo como fundamento para las próximas etapas de experimentación.