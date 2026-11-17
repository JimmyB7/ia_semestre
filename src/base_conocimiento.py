import sqlite3
import os

RUTA_DB = "data/base_conocimiento.db"

def conectar(ruta=RUTA_DB):
    conexion = sqlite3.connect(ruta)
    conexion.execute("PRAGMA foreign_keys = ON;")
    return conexion

def buscar_articulos(dominio, ruta=RUTA_DB):
    consulta = '''
      SELECT a.titulo, p.nombre AS responsable, a.fuente, a.estado
      FROM articulo a
      JOIN dominio d ON d.id = a.dominio_id
      JOIN experto p ON p.id = a.experto_id
      WHERE d.nombre = ? AND a.estado = 'VALIDADO'
    '''
    with conectar(ruta) as conexion:
        return conexion.execute(consulta, (dominio,)).fetchall()

def validar_articulo(articulo_id, ruta=RUTA_DB):
    consulta = "UPDATE articulo SET estado = 'VALIDADO' WHERE id = ?"
    with conectar(ruta) as conexion:
        conexion.execute(consulta, (articulo_id,))
        conexion.commit()