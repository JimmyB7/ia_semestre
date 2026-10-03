# Reporte Semana 09 - Reconocimiento de Imágenes

## 1. Imagen usada
Se utilizó la imagen de prueba `coins` de `scikit-image` para validar el pipeline inicial de procesamiento visual[cite: 1].

## 2. Umbral Otsu
* **Valor generado:** Se calculó automáticamente el umbral óptimo mediante la distribución del histograma[cite: 1].
* **Interpretación:** Separa el fondo oscuro de los objetos de mayor intensidad (monedas)[cite: 1].

## 3. Regiones
* **Cantidad encontrada:** `labels.max()`[cite: 1].
* **Significado:** Representa la cantidad de grupos de píxeles conectados identificados tras aplicar la máscara binaria[cite: 1].

## 4. Sigma
* **Efecto de modificar sigma:** Aumentar `sigma` suaviza la imagen y reduce el ruido, eliminando bordes falsos pero perdiendo detalle fino[cite: 1].

## 5. Limitaciones
La iluminación no uniforme y sombras pueden alterar la máscara de Otsu o fragmentar regiones conectadas[cite: 1].

## 6. Proyecto final
Este procesamiento permite extraer contornos y áreas binarias de señales de tránsito para su análisis previo a la clasificación[cite: 1, 3].