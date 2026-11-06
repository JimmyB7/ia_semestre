import unicodedata

class RedSemantica:
    def __init__(self):
        # Almacena aristas dirigidas por nodo: { origen: [(relacion, destino), ...] }
        self.aristas = {}

    def normalizar(self, texto: str) -> str:
        """Normaliza texto eliminando tildes y pasando a minúsculas (canónico)."""
        base = unicodedata.normalize("NFD", texto.casefold().strip())
        return "".join(c for c in base if unicodedata.category(c) != "Mn")

    def agregar_hecho(self, sujeto: str, relacion: str, objeto: str):
        s = self.normalizar(sujeto)
        r = self.normalizar(relacion)
        o = self.normalizar(objeto)

        if s not in self.aristas:
            self.aristas[s] = []
        self.aristas[s].append((r, o))

    def es_un(self, origen: str, categoria: str) -> bool:
        """Inferencia de jerarquía transitiva usando la relación 'es_un'."""
        orig = self.normalizar(origen)
        cat = self.normalizar(categoria)

        pendientes = [orig]
        visitados = set()

        while pendientes:
            actual = pendientes.pop()
            if actual == cat:
                return True
            if actual in visitados:
                continue
            visitados.add(actual)

            for relacion, destino in self.aristas.get(actual, []):
                if relacion == "es_un":
                    pendientes.append(destino)
        return False

    def consultar_propiedad(self, origen: str, relacion_buscada: str) -> list:
        """Hereda propiedades de categorías superiores de forma transitiva."""
        orig = self.normalizar(origen)
        rel_busc = self.normalizar(relacion_buscada)

        resultados = set()
        pendientes = [orig]
        visitados = set()

        while pendientes:
            actual = pendientes.pop()
            if actual in visitados:
                continue
            visitados.add(actual)

            # Revisar relaciones directas en el nodo actual
            for relacion, destino in self.aristas.get(actual, []):
                if relacion == rel_busc:
                    resultados.add(destino)
                # Si es un tipo de otra categoría, agregamos para seguir heredando
                if relacion == "es_un":
                    pendientes.append(destino)

        return list(resultados)