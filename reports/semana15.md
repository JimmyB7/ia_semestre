# Reporte Semana 15 - Base de Conocimiento en SQLite

## Objetivo

Implementar funciones básicas para consultar y actualizar una base de conocimiento almacenada en SQLite, asociando artículos con sus dominios y expertos responsables.

## Implementación

En `src/base_conocimiento.py` se agregó una interfaz sencilla sobre SQLite para trabajar con la base de datos `data/base_conocimiento.db`.

La función `conectar` crea una conexión con SQLite y activa `PRAGMA foreign_keys = ON`, de modo que se respeten las relaciones declaradas entre las tablas.

La función `buscar_articulos` recibe el nombre de un dominio y ejecuta una consulta que une las tablas `articulo`, `dominio` y `experto`. El resultado incluye el título del artículo, el nombre del experto responsable, la fuente y el estado. La consulta devuelve únicamente los artículos cuyo dominio coincida con el valor solicitado y cuyo estado sea `VALIDADO`.

La función `validar_articulo` recibe el identificador de un artículo y actualiza su estado a `VALIDADO`. Tanto la búsqueda como la actualización utilizan parámetros enlazados en las consultas y admiten una ruta alternativa a la base de datos para facilitar pruebas o distintos escenarios.

## Operaciones disponibles

- Conectarse a la base de conocimiento y habilitar las claves foráneas.
- Buscar artículos validados pertenecientes a un dominio específico.
- Obtener por cada artículo su título, responsable, fuente y estado.
- Cambiar el estado de un artículo a `VALIDADO`.

## Resultado del trabajo

Se obtuvo un módulo reutilizable para acceder a una base de conocimiento relacional y mantener su proceso de validación. La separación de responsabilidades permite consultar contenido validado sin mezclarlo con artículos pendientes y actualizar el estado de un artículo mediante su identificador.
