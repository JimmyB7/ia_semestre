import unittest
from semana13_motor_inferencia import Regla, inferir

class TestMotorInferencia(unittest.TestCase):
    def setUp(self):
        self.reglas = [
            Regla("R1", frozenset({"identidad_validada", "documentos_recibidos"}), "expediente_completo"),
            Regla("R2", frozenset({"expediente_completo", "prerrequisitos_aprobados"}), "inscripcion_habilitada"),
            Regla("R3", frozenset({"inscripcion_habilitada", "cupo_disponible"}), "matricula_autorizada")
        ]

    def test_caso_a_demostrada(self):
        hechos_iniciales = {"identidad_validada", "documentos_recibidos", "prerrequisitos_aprobados", "cupo_disponible"}
        hechos_finales, trazas = inferir(hechos_iniciales, self.reglas)
        self.assertIn("matricula_autorizada", hechos_finales)
        self.assertEqual(trazas, ["R1", "R2", "R3"])

    def test_caso_b_no_demostrada(self):
        hechos_iniciales = {"identidad_validada", "documentos_recibidos", "prerrequisitos_aprobados"}
        hechos_finales, trazas = inferir(hechos_iniciales, self.reglas)
        self.assertNotIn("matricula_autorizada", hechos_finales)
        self.assertEqual(trazas, ["R1", "R2"])

if __name__ == "__main__":
    unittest.main()