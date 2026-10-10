from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from skimage import data, filters, measure
from skimage.feature import local_binary_pattern

# 1. Configurar rutas y carpetas del proyecto
ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(parents=True, exist_ok=True)

# 2. Cargar imagen de prueba y segmentar por Otsu
image = data.coins()
threshold = filters.threshold_otsu(image)
binary_mask = image > threshold

# 3. Etiquetado de regiones y medición de propiedades
labels = measure.label(binary_mask)
regions = [region for region in measure.regionprops(labels) if region.area > 50]

areas = np.array([region.area for region in regions], dtype=float)
area_mean = float(areas.mean()) if len(areas) else 0.0
area_std = float(areas.std()) if len(areas) else 0.0

# 4. Histograma de intensidades globales (32 bins normalizados)
intensity_hist, _ = np.histogram(image.ravel(), bins=32, range=(0, 256), density=True)

# 5. Descriptor de textura LBP (Local Binary Patterns)
texture_img = data.brick()
radius = 2
points = 8 * radius
lbp = local_binary_pattern(texture_img, points, radius, method="uniform")
lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, points + 3), density=True)

# 6. Construcción del vector final de características
features = np.concatenate([
    [area_mean, area_std, len(regions)],
    intensity_hist,
    lbp_hist
])

# 7. Guardar artefactos
np.save(ARTIFACTS / "semana10_features.npy", features)

plt.figure(figsize=(8, 4))
plt.bar(range(len(features)), features, color='navy')
plt.title("Vector Final de Características (Región + Intensidad + Textura)")
plt.xlabel("Índice de Característica")
plt.ylabel("Valor / Frecuencia")
plt.tight_layout()
plt.savefig(ARTIFACTS / "semana10_histograma.png")
plt.close()

print(f"-> Regiones filtradas (> 50px): {len(regions)}")
print(f"-> Área media: {round(area_mean, 2)}")
print(f"-> Dimensión del vector de características: {len(features)}")
print(f"-> Artefactos guardados en: {ARTIFACTS}")