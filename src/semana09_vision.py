from pathlib import Path
import matplotlib.pyplot as plt
from skimage import data, feature, filters, measure

# Crear carpeta de evidencias si no existe
Path("artifacts").mkdir(exist_ok=True)

def ejecutar_practica_semana09():
    # 1. Cargar imagen de prueba (monedas) de scikit-image
    image = data.coins()
    
    # 2. Detección de bordes con Canny (normalizando imagen)
    edges = feature.canny(image / 255.0, sigma=2.0)
    
    # 3. Cálculo de umbral con Otsu, máscara binaria y etiquetado de regiones
    threshold = filters.threshold_otsu(image)
    mask = image > threshold
    labels = measure.label(mask)
    
    print("=== SEMANA 09: RECONOCIMIENTO DE IMÁGENES (PRACTICA) ===")
    print(f"Umbral Otsu calculado: {threshold}")
    print(f"Regiones conectadas encontradas: {labels.max()}")
    
    # 4. Generación y guardado de la evidencia visual comparativa
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].imshow(image, cmap="gray")
    axes[0].set_title("Original")
    
    axes[1].imshow(edges, cmap="gray")
    axes[1].set_title("Canny (sigma=2.0)")
    
    axes[2].imshow(mask, cmap="gray")
    axes[2].set_title("Otsu")
    
    for ax in axes:
        ax.axis("off")
        
    fig.tight_layout()
    ruta_salida = "artifacts/semana09_vision.png"
    fig.savefig(ruta_salida, dpi=160)
    plt.close(fig)
    print(f"Evidencia guardada exitosamente en '{ruta_salida}'")

if __name__ == "__main__":
    ejecutar_practica_semana09()