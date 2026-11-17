import unittest
from src.semana16_motor_referencia import consultar_referencia, normalizar


REFERENCIAS_DE_PRUEBA = [
    {
        "id": "REF-001",
        "claves": ["inscribir", "asignatura", "matricula", "curso"],
        "respuesta": "Consulta el sistema académico institucional.",
        "fuente": "Referencia de prueba",
        "validada": True,
    },
    {
        "id": "REF-004",
        "claves": ["cambio", "grupo", "horario"],
        "respuesta": "Respuesta de prueba no validada.",
        "fuente": "Referencia de prueba",
        "validada": False,
    },
]


class TestMotorReferencia(unittest.TestCase):
    def test_1_consulta_exitosa(self):
        res = consultar_referencia("Quiero inscribir una asignatura", REFERENCIAS_DE_PRUEBA)
        self.assertEqual(res["estado"], "ENCONTRADA")
        self.assertEqual(res["id"], "REF-001")
        self.assertEqual(res["puntuacion"], 2)

    def test_2_normalizacion_mayusculas_y_tildes(self):
        self.assertEqual(normalizar("MATRÍCULA de Curso"), {"matricula", "de", "curso"})
        res = consultar_referencia("MATRÍCULA", REFERENCIAS_DE_PRUEBA)
        self.assertEqual(res["estado"], "ENCONTRADA")
        self.assertEqual(res["id"], "REF-001")

    def test_3_ignora_no_validada(self):
        res = consultar_referencia("cambio grupo horario", REFERENCIAS_DE_PRUEBA)
        self.assertEqual(res["estado"], "SIN_REFERENCIA")
        self.assertIsNone(res["id"])

    def test_4_fuera_de_cobertura(self):
        res = consultar_referencia("parqueo bicicleta", REFERENCIAS_DE_PRUEBA)
        self.assertEqual(res["estado"], "SIN_REFERENCIA")

    def test_5_entrada_vacia(self):
        res = consultar_referencia("   ???   ", REFERENCIAS_DE_PRUEBA)
        self.assertEqual(res["estado"], "SIN_REFERENCIA")

    def test_6_base_de_produccion_vacia(self):
        res = consultar_referencia("Quiero inscribir una asignatura")
        self.assertEqual(res["estado"], "SIN_REFERENCIA")


if __name__ == "__main__":
    unittest.main()