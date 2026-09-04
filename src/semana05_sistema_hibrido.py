import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

# Rutas del proyecto
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
KB_PATH = DATA_DIR / "base_conocimiento.txt"
REPORTS_DIR = ROOT / "reports"
REPORT_PATH = REPORTS_DIR / "semana05.md"

# 1. Reglas expertas (Sistemas Expertos) con funciones lambda
RULES = [
    (lambda q: "temperatura" in q or "caliente" in q or "ventilador" in q, "revisar_ventilacion"),
    (lambda q: "red" in q or "internet" in q or "dns" in q, "revisar_conectividad"),
    (lambda q: "sesion" in q or "cuenta" in q or "clave" in q or "bloqueada" in q, "revisar_acceso"),
    (lambda q: "lenta" in q or "ram" in q or "cpu" in q or "disco" in q, "revisar_rendimiento"),
    (lambda q: "pantalla azul" in q or "controlador" in q or "ram" in q, "revisar_hardware_critico"),
]

# Data de entrenamiento para el Clasificador (Reconocimiento de Formas / PLN)
# Exigencia del profesor: 15 ejemplos etiquetados
TRAIN_X = [
    "el equipo esta muy caliente y el ventilador hace ruido",
    "temperatura alta en el procesador",
    "el disco duro esta al maximo y la pc esta lenta",
    "internet se cae y aparece error dns",
    "no hay conexion a la red ni wifi",
    "falla la IP y no navega en web",
    "no puedo iniciar sesion en mi cuenta",
    "clave bloqueada y falta de permisos",
    "error de autenticacion al ingresar",
    "pantalla azul al encender el computador",
    "la memoria RAM esta saturada y las apps se congelan",
    "servidor de base de datos no responde en el puerto",
    "conexion inestable a internet por cable de red",
    "usuario bloqueado por varios intentos fallidos",
    "limpieza de ventiladores por sobrecalentamiento"
]

TRAIN_Y = [
    "hardware", "hardware", "hardware",
    "red", "red", "red",
    "seguridad", "seguridad", "seguridad",
    "hardware", "hardware", "red",
    "red", "seguridad", "hardware"
]

def load_documents() -> list[str]:
    """Carga y valida la base de conocimiento textual."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not KB_PATH.exists():
        raise FileNotFoundError(f"No existe {KB_PATH}. Crea el archivo con minimo 8 entradas.")
    
    docs = [line.strip() for line in KB_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(docs) < 8:
        raise ValueError(f"data/base_conocimiento.txt debe contener al menos 8 entradas. Actualmente tiene {len(docs)}.")
    return docs

def build_hybrid_system():
    """Entrena e inicializa los componentes de TF-IDF y Clasificación."""
    docs = load_documents()
    
    # Modelo TF-IDF para Recuperación de Información
    vectorizer = TfidfVectorizer()
    doc_matrix = vectorizer.fit_transform(docs)
    
    # Clasificador de texto
    classifier = make_pipeline(
        TfidfVectorizer(),
        LogisticRegression(max_iter=1000, random_state=42)
    )
    classifier.fit(TRAIN_X, TRAIN_Y)
    
    return docs, vectorizer, doc_matrix, classifier

def answer(query: str, docs, vectorizer, doc_matrix, classifier) -> dict:
    """Procesa una consulta retornando la trazabilidad del sistema híbrido."""
    q = query.lower()
    
    # 1. Evaluar Reglas Expertas
    fired = [name for condition, name in RULES if condition(q)]
    
    # 2. Recuperación por Similitud Coseno (TF-IDF)
    query_vec = vectorizer.transform([q])
    similarities = cosine_similarity(query_vec, doc_matrix)[0]
    best_index = int(similarities.argmax())
    
    # 3. Clasificación de Categoria (PLN / Aprendizaje)
    label = str(classifier.predict([q])[0])
    
    return {
        "reglas": fired,
        "evidencia": docs[best_index],
        "similitud": float(similarities[best_index]),
        "clase": label,
    }

def write_report(rows: list[tuple[str, dict]]) -> None:
    """Genera el reporte Markdown reproducible exigido en reports/semana05.md."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Semana 05 - Sistema Híbrido de Soporte Técnico",
        "",
        "## Resultados de las Consultas de Prueba",
        ""
    ]
    
    for i, (query, result) in enumerate(rows, start=1):
        reglas_str = ", ".join(result["reglas"]) if result["reglas"] else "ninguna"
        lines += [
            f"### Consulta {i}: \"{query}\"",
            f"- **Reglas disparadas:** `{reglas_str}`",
            f"- **Evidencia recuperada:** {result['evidencia']}",
            f"- **Similitud Coseno (TF-IDF):** `{result['similitud']:.3f}`",
            f"- **Clase predicha:** `{result['clase']}`",
            ""
        ]
        
    lines += [
        "## Análisis de Trazabilidad y Limitaciones",
        "- **Explicabilidad:** El sistema no solo arroja una clase categórica, sino que justifica su decisión mediante reglas simbólicas directas y evidencia textual de la base de conocimiento.",
        "- **Limitaciones:** Con pocos ejemplos de entrenamiento (15 frases), la regresión logística puede errar en textos ambiguos. Además, la búsqueda TF-IDF depende de coincidencias léxicas exactas o raíces compartidas, por lo que sinónimos no incluidos en la base documental podrían bajar la puntuación de similitud."
    ]
    
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

def main():
    docs, vectorizer, doc_matrix, classifier = build_hybrid_system()
    
    # Exigencia del profesor: 3 consultas de prueba
    test_queries = [
        "El equipo esta muy caliente y el ventilador hace ruido",
        "Internet se cae continuamente y aparece un fallo DNS en la red",
        "No puedo iniciar sesion con mi cuenta porque olvide la clave"
    ]
    
    rows = []
    print("=" * 80)
    print("SEMANA 05 - SISTEMA HÍBRIDO DE IA")
    print("=" * 80)
    
    for query in test_queries:
        res = answer(query, docs, vectorizer, doc_matrix, classifier)
        rows.append((query, res))
        
        print(f"\nEntrada: {query}")
        print(json.dumps(res, indent=2, ensure_ascii=False))
        
    write_report(rows)
    print("\n" + "=" * 80)
    print(f"Reporte generado exitosamente en: {REPORT_PATH}")
    print("=" * 80)

if __name__ == "__main__":
    main()