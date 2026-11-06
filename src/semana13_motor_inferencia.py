from dataclasses import dataclass

@dataclass(frozen=True)
class Regla:
    nombre: str
    premisas: frozenset[str]
    conclusion: str

def inferir(hechos_iniciales, reglas):
    hechos = set(hechos_iniciales)
    trazas = []
    cambios = True
    while cambios:
        cambios = False
        for regla in reglas:
            if regla.premisas.issubset(hechos) \
               and regla.conclusion not in hechos:
                hechos.add(regla.conclusion)
                trazas.append(regla.nombre)
                cambios = True
    return hechos, trazas