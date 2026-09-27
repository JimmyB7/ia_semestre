from pathlib import Path
import pickle
import sqlite3
import networkx as nx
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def ejecutar_prueba_semana08():
    print("=== SEMANA 08: RED NEURONAL, BASE DE DATOS Y ONTOLOGÍA ===")

    # -------------------------------------------------------------
    # BLOQUE 1/5: Preparación de rutas y dataset
    # -------------------------------------------------------------
    ROOT = Path(__file__).resolve().parent.parent
    ARTIFACTS = ROOT / "artifacts"
    ARTIFACTS.mkdir(parents=True, exist_ok=True)

    X, y = load_digits(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    print("\n[1/5] Dataset 'load_digits' cargado y dividido correctamente.")

    # -------------------------------------------------------------
    # BLOQUE 2/5: Entrenamiento de la Red Neuronal (MLP) y guardado
    # -------------------------------------------------------------
    model = MLPClassifier(
        hidden_layer_sizes=(64,),
        max_iter=400,
        random_state=42
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = round(accuracy_score(y_test, pred), 4)
    print(f"[2/5] Red Neuronal MLP entrenada. Accuracy: {acc}")

    # Guardar modelo serializado (.pkl)
    with (ARTIFACTS / "modelo_mlp.pkl").open("wb") as file:
        pickle.dump(model, file)
    print("      -> Modelo guardado en 'artifacts/modelo_mlp.pkl'")

    # -------------------------------------------------------------
    # BLOQUE 3/5: Registro de evidencias en Base de Datos (SQLite)
    # -------------------------------------------------------------
    with sqlite3.connect(ARTIFACTS / "imagenes.db") as con:
        con.execute(
            "CREATE TABLE IF NOT EXISTS images("
            "id INTEGER PRIMARY KEY, label INTEGER, split TEXT)"
        )
        con.execute("DELETE FROM images")
        con.executemany(
            "INSERT INTO images(id,label,split) VALUES(?,?,?)",
            [(i, int(y[i]), "dataset") for i in range(20)],
        )
        con.commit()
    print("[3/5] Evidencia guardada en 'artifacts/imagenes.db' (Tabla images creada con 20 metadatos).")

    # -------------------------------------------------------------
    # BLOQUE 4/5: Creación y exportación de la Ontología (NetworkX/GraphML)
    # -------------------------------------------------------------
    G = nx.DiGraph()
    G.add_edges_from([
        ("digito", "cero", {"rel": "tiene_clase"}),
        ("digito", "uno", {"rel": "tiene_clase"}),
        ("digito", "dos", {"rel": "tiene_clase"}),
        ("modelo_mlp", "digito", {"rel": "reconoce"}),
        ("imagen", "digito", {"rel": "representa"}),
        ("prediccion", "digito", {"rel": "asigna_clase"}),
        ("modelo_mlp", "prediccion", {"rel": "produce"}),
    ])
    
    # -------------------------------------------------------------
    # BLOQUE 5/5: Enlace directo (Predicción + Evidencia + Ontología)
    # -------------------------------------------------------------
    ejemplo_id = 15
    clase_predicha = int(model.predict([X[ejemplo_id]])[0])
    concepto = f"digito_{clase_predicha}"
    
    G.add_edge("prediccion_15", concepto, rel="asigna_clase")
    G.add_edge("imagen_15", "prediccion_15", rel="genera")

    # Exportar Grafo en formato GraphML
    nx.write_graphml(G, ARTIFACTS / "ontologia.graphml")
    
    print(f"[4/5 & 5/5] Ontología construida y exportada en 'artifacts/ontologia.graphml'.")
    print(f"      -> Total relaciones en el grafo: {G.number_of_edges()}")
    print(f"      -> Ejemplo #15 evaluado: ID={ejemplo_id} | Clase Predicha={clase_predicha} | Concepto='{concepto}'")

if __name__ == "__main__":
    ejecutar_prueba_semana08()