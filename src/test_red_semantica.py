import unittest
from red_semantica import RedSemantica

class TestRedSemantica(unittest.TestCase):
    def setUp(self):
        self.red = RedSemantica()
        self.red.agregar_hecho("perro", "es_un", "mamifero")
        self.red.agregar_hecho("mamifero", "es_un", "animal")
        self.red.agregar_hecho("animal", "necesita", "agua")
        self.red.agregar_hecho("gato", "es_un", "mamifero")

    def test_es_un_exitoso(self):
        self.assertTrue(self.red.es_un("perro", "animal"))

    def test_es_un_falso(self):
        self.assertFalse(self.red.es_un("perro", "ave"))

    def test_herencia_propiedad(self):
        necesidades = self.red.consultar_propiedad("perro", "necesita")
        self.assertIn("agua", necesidades)

if __name__ == "__main__":
    unittest.main()