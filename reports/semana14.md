# Reporte Semana 14 - Red Semántica

## Objetivo

Representar conocimiento como relaciones entre conceptos e implementar consultas sobre categorías y propiedades heredadas.

## Implementación

En `src/red_semantica.py` se creó la clase `RedSemantica`, que almacena hechos como aristas dirigidas de la forma sujeto-relación-objeto. Antes de guardar o consultar, normaliza los textos: elimina espacios al inicio y al final, convierte a minúsculas y quita tildes.

Se implementaron dos consultas:

- `es_un` recorre las relaciones `es_un` para determinar si una categoría pertenece, directa o transitivamente, a otra.
- `consultar_propiedad` busca una relación en el nodo consultado y en sus categorías superiores, heredando así propiedades de forma transitiva.

El ejemplo de prueba organiza los conceptos `perro`, `mamifero` y `animal` con relaciones `es_un`, y asigna a `animal` la propiedad `necesita agua`. También se incluye `gato` como otro tipo de mamífero.

## Pruebas y resultados

Las pruebas de `src/test_red_semantica.py` comprueban que:

- `perro` pertenece transitivamente a la categoría `animal`.
- `perro` no pertenece a la categoría `ave`.
- La consulta de la propiedad `necesita` para `perro` hereda el resultado `agua` desde `animal`.

**Resultado:** las 3 pruebas de la red semántica finalizaron correctamente.

## Resultado del trabajo

Se construyó una representación de conocimiento consultable con relaciones explícitas, recorridos transitivos de jerarquías y herencia de propiedades. La normalización facilita consultas aun cuando varíen las mayúsculas o se usen tildes.
