import re
import unicodedata

REFERENCIAS: list[dict] = []


def normalizar(texto: str) -> set[str]:
    descompuesto = unicodedata.normalize("NFD", texto.casefold())
    sin_tildes = "".join(
        c for c in descompuesto if unicodedata.category(c) != "Mn"
    )
    return set(re.findall(r"[a-z0-9]+", sin_tildes))


def consultar_referencia(pregunta: str, base: list[dict] = REFERENCIAS) -> dict:
    palabras = normalizar(pregunta)
    if not palabras:
        return {
            "estado": "SIN_REFERENCIA",
            "respuesta": "No hay evidencia validada; consulta con una persona responsable.",
            "id": None,
            "fuente": None,
            "puntuacion": 0,
        }

    candidatos = []
    for referencia in base:
        if not referencia.get("validada", False):
            continue
        claves_norm = set()
        for c in referencia["claves"]:
            claves_norm.update(normalizar(c))

        coincidencias = palabras.intersection(claves_norm)
        if coincidencias:
            candidatos.append((len(coincidencias), referencia["id"], referencia))

    if not candidatos:
        return {
            "estado": "SIN_REFERENCIA",
            "respuesta": "No hay evidencia validada; consulta con una persona responsable.",
            "id": None,
            "fuente": None,
            "puntuacion": 0,
        }

    # Ordenar por mayor coincidencia y desempatar por ID ascendente
    candidatos.sort(key=lambda x: (-x[0], x[1]))
    mejor_puntaje, _, mejor_ref = candidatos[0]

    return {
        "estado": "ENCONTRADA",
        "respuesta": mejor_ref["respuesta"],
        "id": mejor_ref["id"],
        "fuente": mejor_ref["fuente"],
        "puntuacion": mejor_puntaje,
    }