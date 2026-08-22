from dataclasses import dataclass
from pathlib import Path
import csv
import re
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
CSV_FILE = ROOT / "data" / "casos_ia.csv"
REPORT_FILE = ROOT / "reports" / "semana03.md"

@dataclass(frozen=True)
class Category:
    name: str
    keywords: dict[str, int]  # Mejora 1: Diccionario de palabras clave con pesos ponderados

CATEGORIES = [
    Category("Visión por computador", {
        "imagen": 1, "imagenes": 1, "foto": 1, "fotografia": 1, "fotografias": 1, 
        "camara": 1, "rostro": 2, "rostros": 2, "peaton": 2, "peatones": 2, 
        "senal": 1, "senales": 1
    }),
    Category("Procesamiento de lenguaje natural", {
        "texto": 1, "comentario": 1, "comentarios": 1, "correo": 1, "correos": 1, 
        "chatbot": 2, "contrato": 2, "contratos": 2, "nombres": 1, "lenguaje": 1
    }),
    Category("Aprendizaje automático predictivo", {
        "predecir": 2, "probabilidad": 2, "demanda": 1, "fraude": 2, "fraudes": 2, "sensores": 1
    }),
    Category("Sistemas de recomendación", {
        "recomendar": 2, "preferencias": 1, "historial de visualizacion": 2, "sugerir": 1
    }),
    Category("Búsqueda y optimización", {
        "ruta": 2, "rutas": 2, "horario": 1, "horarios": 1, "combinacion optima": 2,
        "optimizar": 2, "capacidad maxima": 2
    }),
    Category("Sistemas expertos", {
        "diagnostico": 2, "diagnosticos": 2, "reglas": 1, "politicas": 1, "solicitud de credito": 2
    }),
    Category("Robótica y sistemas autónomos", {
        "robot": 2, "robots": 2, "dron": 2, "drones": 2, "vehiculo autonomo": 3, "obstaculos": 1
    })
]

# Reglas propias con peso asignado (Mejora 1)
CUSTOM_RULES = {
    "Visión por computador": {"matricula": 2, "matriculas": 2},
    "Procesamiento de lenguaje natural": {"sentimiento": 2},
    "Aprendizaje automático predictivo": {"falla": 2, "fallas": 2},
    "Sistemas expertos": {"sintoma": 2, "sintomas": 2},
    "Robótica y sistemas autónomos": {"trayectoria": 2, "trayectorias": 2},
}

MANUAL_REFERENCE = [
    "Visión por computador", "Procesamiento de lenguaje natural", "Aprendizaje automático predictivo",
    "Búsqueda y optimización", "Sistemas de recomendación", "Aprendizaje automático predictivo",
    "Visión por computador", "Procesamiento de lenguaje natural", "Aprendizaje automático predictivo",
    "Sistemas expertos", "Visión por computador", "Procesamiento de lenguaje natural",
    "Robótica y sistemas autónomos", "Búsqueda y optimización", "Aprendizaje automático predictivo",
    "Procesamiento de lenguaje natural", "Visión por computador", "Sistemas expertos",
    "Robótica y sistemas autónomos", "Búsqueda y optimización"
]

def normalize(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def normalize_header(text: str) -> str:
    return normalize(text).replace(" ", "")

def contains_keyword(text: str, keyword: str) -> bool:
    normalized_text = f" {normalize(text)} "
    normalized_keyword = normalize(keyword)
    return f" {normalized_keyword} " in normalized_text

def build_categories() -> list[Category]:
    result = []
    for category in CATEGORIES:
        merged_keywords = dict(category.keywords)
        extra = CUSTOM_RULES.get(category.name, {})
        for kw, weight in extra.items():
            merged_keywords[kw] = weight
        result.append(Category(category.name, merged_keywords))
    return result

def classify_problem(text: str) -> tuple[str, list[str], dict[str, int]]:
    scores = {}
    for category in build_categories():
        # Mejora 1: Sumatoria ponderada basada en los pesos de los términos clave
        score = sum(weight for kw, weight in category.keywords.items() if contains_keyword(text, kw))
        scores[category.name] = score
    
    matches = [
        (score, index, category.name)
        for index, category in enumerate(build_categories())
        if (score := scores[category.name]) > 0
    ]
    matches.sort(key=lambda item: (-item[0], item[1]))
    detected = [name for _, _, name in matches]
    primary = detected[0] if detected else "Requiere análisis"
    return primary, detected or ["Requiere análisis"], scores

def read_cases() -> list[str]:
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"No existe {CSV_FILE}. Crea data/casos_ia.csv antes de ejecutar la práctica.")
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError("El CSV está vacío o no contiene encabezados.")
        original_headers = list(reader.fieldnames)
        reader.fieldnames = [normalize_header(name) for name in reader.fieldnames]
        if "descripcion" not in reader.fieldnames:
            raise ValueError(f"No se encontró la columna 'descripcion'. Encabezados: {original_headers}")
        cases = []
        for row in reader:
            description = (row.get("descripcion") or "").strip()
            if description:
                cases.append(description)
        if len(cases) < 20:
            raise ValueError(f"La práctica requiere al menos 20 casos y el archivo contiene {len(cases)}.")
        return cases

def write_report(results: list[dict]) -> None:
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    reference_count = min(len(results), len(MANUAL_REFERENCE))
    matches = sum(1 for i in range(reference_count) if results[i]["primary"] == MANUAL_REFERENCE[i])
    accuracy = 100 * matches / reference_count if reference_count else 0.0

    lines = [
        "# Semana 03 - Taxonomía de Inteligencia Artificial ",
        "## Resultado automático frente a clasificación manual de referencia",
        "| Caso | Categoría automática principal | Categorías detectadas | Manual | Estado |",
        "|---|---|---|---|---|",
    ]
    
    for i, result in enumerate(results, start=1):
        manual = MANUAL_REFERENCE[i - 1] if (i - 1) < len(MANUAL_REFERENCE) else "Pendiente"
        status = "Coincide" if result["primary"] == manual else "Revisar"
        detected = ", ".join(result["detected"])
        lines.append(f"| {i} | {result['primary']} | {detected} | {manual} | {status} |")

    lines += [
        "",
        f"Coincidencia con la referencia: **{accuracy:.2f}%** ({matches}/{reference_count}).",
        "",
        "## Justificación de Mejoras Técnicas",
        "1. **Ponderación de Términos Clave (Pesos Semánticos):** Se modificó la estructura de palabras clave para incluir pesos enteros (de 1 a 3). Términos específicos y complejos de dominios críticos (como *'vehículo autónomo'* o *'diagnóstico'*) reciben mayor peso que palabras generales, reduciendo ambigüedades en la clasificación principal.",
        "2. **Trazabilidad de Puntuación:** El motor calcula una matriz de puntajes por cada categoría evaluada, permitiendo auditorías internas sobre por qué una categoría secundaria obtiene más o menos relevancia frente al problema planteado.",
        "3. **Ampliación de Reglas Personalizadas (`CUSTOM_RULES`):** Se integraron términos de dominio específicos (matrículas, sentimientos, fallas, síntomas y trayectorias) para garantizar una correspondencia más fina con problemas del entorno real.",
        "",
        "## Discrepancias y análisis de ingeniería",
        "En los casos donde la clasificación automática difiere de la referencia manual, se observa que los problemas de ingeniería suelen cruzar múltiples fronteras (por ejemplo, robótica que requiere visión por computador o sistemas expertos basados en reglas de negocio). La ponderación ayuda a mitigar falsos positivos, pero se recomienda complementar este motor simbólico con enfoques basados en embeddings o modelos de lenguaje en fases posteriores del proyecto semestral."
    ]
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    cases = read_cases()
    results = []
    print("=" * 80)
    print("SEMANA 03 - TAXONOMÍA DE INTELIGENCIA ARTIFICIAL")
    print("=" * 80)
    
    for i, case in enumerate(cases, start=1):
        primary, detected, scores = classify_problem(case)
        results.append({
            "description": case,
            "primary": primary,
            "detected": detected,
            "scores": scores,
        })
        print(f"{i:02d}. {case}")
        print(f"   Principal: {primary}")
        print(f"   Áreas detectadas: {', '.join(detected)}")
        
    write_report(results)
    print(f"\nCasos procesados: {len(results)}")
    print(f"Reporte generado: {REPORT_FILE}")

if __name__ == "__main__":
    main()