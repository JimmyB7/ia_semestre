# Semana 4 — Marco tecnológico de la inteligencia artificial

## Práctica guiada: Búsqueda A* y decisión Minimax

### 1. Búsqueda A* (src/semana04_astar.py)

**Formulación como espacio de estados:**

- **Estado:** la posición actual en la cuadrícula, representada como una tupla `(fila, columna)`.
- **Acción:** moverse a una celda vecina libre (arriba, abajo, izquierda o derecha), siempre que no sea un obstáculo (`#`).
- **Meta:** llegar desde el estado inicial `START = (0, 0)` hasta el estado objetivo `GOAL = (4, 4)`.
- **Costo de camino:** cada movimiento entre celdas vecinas cuesta 1. El costo total es la suma de los movimientos realizados.
- **Heurística h(n):** distancia Manhattan entre la celda actual y la meta (`|fila_actual - fila_meta| + |columna_actual - columna_meta|`). Es admisible porque nunca sobreestima el costo real restante, ya que en la cuadrícula solo se permite movimiento en 4 direcciones.
- **Función de prioridad f(n) = g(n) + h(n):** combina el costo acumulado real (`g`) con la estimación heurística (`h`) para decidir qué nodo explorar primero.

**Ejecución obtenida:**
- Ruta: `[(0,0), (0,1), (0,2), (0,3), (0,4), (1,4), (2,4), (3,4), (4,4)]`
- Costo: `8`

El algoritmo bordeó los obstáculos ubicados en la fila 1 y encontró la ruta más corta posible entre el inicio y la meta.

**Prueba de modificación:** se alteraron los obstáculos de `GRID` y se verificó que la ruta se ajustara en consecuencia, o que la función devolviera `None` cuando no existía camino posible.

---

### 2. Decisión Minimax (src/semana04_minimax.py)

**Formulación como juego adversarial:**

- **Estado:** la configuración actual del tablero de tres en línea (una lista de 9 posiciones con `"X"`, `"O"` o `" "`).
- **Acción:** colocar una ficha (`X` u `O`) en una casilla vacía.
- **Meta:** maximizar el resultado para el jugador `X` (agente MAX) y minimizar el resultado para `O` (agente MIN), asumiendo que ambos jugadores juegan de forma óptima.
- **Función de utilidad (valor terminal):** `+1` si gana `X`, `-1` si gana `O`, `0` si hay empate.
- **Heurística:** no se usa una heurística de estimación como en A*, porque el árbol de juego es lo suficientemente pequeño para explorarse por completo (búsqueda exhaustiva). El valor de cada nodo se calcula recursivamente propagando los resultados terminales hacia la raíz.

**Ejecución obtenida:**
- Tablero: `['X', 'O', 'X', 'O', 'X', ' ', ' ', ' ', 'O']`
- Mejor posición para X: `6`

El algoritmo evaluó todas las jugadas disponibles (posiciones 5, 6 y 7) simulando las