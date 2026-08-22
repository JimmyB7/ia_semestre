# IA Semestre - Práctica de Fundamentos y Modelos Predictivos

Repositorio oficial para las prácticas del semestre de Inteligencia Artificial. Contiene la estructura base, entornos virtuales configurados y scripts reproducibles de Machine Learning.

## Módulos Desarrollados y Avances Semanales

### Semana 02: Fundamentos
- Configuración del entorno de desarrollo y estructura inicial del proyecto.
- Definición de la arquitectura base y organización de directorios.

### Semana 03: Taxonomía de Inteligencia Artificial
- **Propósito:** Construcción de un motor clasificador simbólico de requerimientos para categorizar problemas de IA.
- **Implementación:** Script (`src/semana03_taxonomia.py`) capaz de asignar categorías de IA basándose en palabras clave con pesos semánticos ponderados.
- **Resultados y Hallazgos:** 
    - Clasificación automática con **100% de coincidencia** (20/20 casos) respecto a la referencia manual.
    - Implementación de un sistema de pesos enteros (1 a 3) en las reglas personalizadas (`CUSTOM_RULES`) para mitigar ambigüedades en problemas complejos.
    - Generación automática del informe técnico de auditoría en `reports/semana03.md`.

---


## Arquitectura del Proyecto

Proyecto estructurado para garantizar la modularidad, reproducibilidad y escalabilidad de modelos de IA.

## 🛠 Stack Tecnológico

### Lenguaje y Entorno
- **Python 3.13** - Lenguaje principal.
- **venv** - Gestión de entornos virtuales aislados.

### Ciencia de Datos
- **NumPy** - Procesamiento numérico.
- **Pandas** - Manipulación de datos.
- **Scikit-learn** - Modelos de Machine Learning.
- **Matplotlib** - Visualización de datos.

### Desarrollo y Control de Versiones
- **Git** - Control de versiones.
- **VS Code** - Entorno de desarrollo.

## Instalación

### Pre-requisitos
- Node.js >= 18.x (opcional para herramientas web).
- Python 3.13+.
- Git.

### Clonar el repositorio
```bash
git clone [https://github.com/DanielDaza2901/ia_semestre.git](https://github.com/DanielDaza2901/ia_semestre.git)
cd ia_semestre
Configurar Entorno
Bash
# Crear entorno virtual
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Instalar dependencias
python -m pip install -r requirements.txt

---

## Estructura del Proyecto
Plaintext
## Estructura del Repositorio
ia_semestre/
├── .venv/            # Entorno virtual
├── artifacts/        # Modelos serializados (.pkl, .joblib)
├── data/             # Datasets (CSV, JSON, etc.)
├── notebooks/        # Experimentación interactiva (Jupyter)
├── reports/          # Informes técnicos (.md, .pdf)
├── src/              # Código fuente (scripts de entrenamiento)
│   └── semana02/     # Actividades semanales
├── tests/            # Pruebas unitarias
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación principal

---

Autor
- Estudiante: Daniel Eduardo Daza Cuello
- Institución: ETITC - 10º Semestre

