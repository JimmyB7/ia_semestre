from pathlib import Path
from time import perf_counter
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# 1. Crear carpeta de artefactos
Path("artifacts").mkdir(exist_ok=True)

# 2. Cargar dataset y realizar split controlado con semilla fija
X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 3. Definir los tres modelos a comparar
models = {
    "logistic": make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1500)
    ),
    "forest": RandomForestClassifier(
        n_estimators=250, random_state=42, n_jobs=-1
    ),
    "mlp": make_pipeline(
        StandardScaler(),
        MLPClassifier(hidden_layer_sizes=(64,), max_iter=350, random_state=42)
    ),
}

# 4. Ejecutar benchmark, medir tiempo y evaluar exactitud
rows = []
for name, model in models.items():
    start = perf_counter()
    model.fit(X_train, y_train)
    elapsed = perf_counter() - start
    acc = accuracy_score(y_test, model.predict(X_test))
    rows.append({
        "modelo": name,
        "accuracy": acc,
        "fit_seconds": elapsed
    })

# 5. Ordenar, imprimir y guardar evidencia en CSV
df = pd.DataFrame(rows).sort_values("accuracy", ascending=False)
print(df.to_string(index=False))
df.to_csv("artifacts/benchmark.csv", index=False)