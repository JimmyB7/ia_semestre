if __package__:
    from .semana16_motor_referencia import consultar_referencia
else:
    from semana16_motor_referencia import consultar_referencia


def main():
    print("=== SISTEMA DE REFERENCIA ACADÉMICA (SEMANA 16) ===")
    print("Escribe 'salir' para terminar.\n")

    while True:
        pregunta = input("Tu pregunta: ").strip()
        if pregunta.lower() == "salir":
            break

        resultado = consultar_referencia(pregunta)
        print(f"Estado: {resultado['estado']}")
        print(f"Respuesta: {resultado['respuesta']}")
        if resultado["estado"] == "ENCONTRADA":
            print(f"Fuente: {resultado['id']} - {resultado['fuente']} (Coincidencias: {resultado['puntuacion']})")
        print("-" * 50)


if __name__ == "__main__":
    main()