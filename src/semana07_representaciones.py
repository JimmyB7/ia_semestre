import numpy as np

def ejecutar_prueba_semana07():
    print("=== SEMANA 07: REPRESENTACIONES DEL RECONOCIMIENTO ===")

    # 1. REPRESENTACIÓN NUMÉRICA
    # [velocidad_kmh, distancia_obstaculo_m, nivel_iluminacion_lux]
    muestra_actual = np.array([55.0, 12.0, 300.0])
    referencia_segura = np.array([50.0, 20.0, 500.0])
    
    distancia = np.linalg.norm(muestra_actual - referencia_segura)
    print(f"\n1. Numérica -> Distancia Euclidiana respecto al estado ideal: {round(float(distance := distancia), 3)}")

    # 2. REPRESENTACIÓN SIMBÓLICA
    hechos_vehicular = {"exceso_velocidad", "distancia_corta", "camara_limpia"}
    print(f"2. Simbólica -> Hechos detectados: {hechos_vehicular}")
    
    if {"exceso_velocidad", "distancia_corta"}.issubset(hechos_vehicular):
        print("   Conclusión Simbólica: ALERTA_Riesgo_Colision (Regla de frenado inmediato activada)")

    # 3. RECONOCIMIENTO MEDIANTE AUTÓMATA (FSM)
    # Reconoce secuencias de eventos de luces de semáforo: '0' (Rojo), '1' (Verde)
    # Patrón a reconocer: Cadena que termine en '01' (Transición de Rojo a Verde)
    def automata_transicion_semaforo(secuencia):
        estado = "q0"
        transiciones = {
            ("q0", "0"): "q1", ("q0", "1"): "q0",
            ("q1", "0"): "q1", ("q1", "1"): "q2",
            ("q2", "0"): "q1", ("q2", "1"): "q0",
        }
        for simbolo in secuencia:
            estado = transiciones.get((estado, simbolo), "q0")
        return estado == "q2"

    print("\n3. Autómata -> Detección de Patrón '01' (Rojo -> Verde):")
    secuencias = ["1101", "1110", "0001"]
    for seq in secuencias:
        aceptada = automata_transicion_semaforo(seq)
        print(f"   Secuencia '{seq}' aceptada para reanudar marcha: {aceptada}")

if __name__ == "__main__":
    ejecutar_prueba_semana07()