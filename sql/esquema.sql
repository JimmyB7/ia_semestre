CREATE TABLE dominio (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE
);

CREATE TABLE aplicacion (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    dominio_id INTEGER NOT NULL REFERENCES dominio(id)
);

CREATE TABLE experto (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL
);

CREATE TABLE articulo (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    dominio_id INTEGER NOT NULL REFERENCES dominio(id),
    experto_id INTEGER NOT NULL REFERENCES experto(id),
    fuente TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'BORRADOR' CHECK(estado IN ('BORRADOR', 'VALIDADO'))
);