# Sistema de Gestión de Blog

## Descripción

Sistema de gestión de publicaciones desarrollado en Python, que permite administrar el contenido de un blog desde una interfaz interactiva por consola.

La aplicación permite crear, consultar, buscar, filtrar y validar publicaciones, organizando la información mediante programación orientada a objetos. Además, incorpora persistencia de datos en archivos JSON, lo que permite conservar las publicaciones entre distintas ejecuciones del programa.

## Funcionalidades

- **Gestión de publicaciones:** creación y administración de posts.
- **Listado de publicaciones:** visualización de los posts registrados, incluyendo título, autor y estado.
- **Búsqueda por título:** localización de publicaciones mediante palabras o fragmentos del título.
- **Filtrado por etiquetas:** búsqueda de publicaciones según sus categorías o tags.
- **Validación de contenido:** comprobación de los datos requeridos para garantizar la integridad de las publicaciones.
- **Persistencia de datos:** almacenamiento y recuperación automática de publicaciones mediante archivos JSON.
- **Manejo de errores:** control de situaciones como archivos inexistentes, vacíos, datos inválidos o entradas incorrectas.

## Arquitectura del sistema

El proyecto está organizado en módulos independientes para separar responsabilidades y facilitar el mantenimiento y la evolución del código.

```text
PR-Entrega-6/
│
├── main.py
├── README.md
├── posts.json
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

### Modelos

El sistema utiliza tres clases principales:

**Autor**

Representa a los autores de las publicaciones. Contiene información como nombre, biografía, especialidad y redes sociales.

**Post**

Representa cada publicación del blog. Incluye identificador, título, contenido, autor, etiquetas y estado. Cada publicación mantiene una relación con una instancia de la clase `Autor`.

**Blog**

Centraliza la administración de las publicaciones y las operaciones disponibles sobre ellas, como búsquedas, filtros, creación y validación de posts.

### Persistencia de datos

La información se almacena en `posts.json`, utilizando el formato JSON para facilitar su lectura, escritura y recuperación.

El sistema contempla dos procesos principales:

- **Carga de información:** al iniciar la aplicación, recupera las publicaciones almacenadas y reconstruye los objetos correspondientes.
- **Guardado de información:** convierte los objetos del sistema a estructuras compatibles con JSON y almacena los cambios realizados.

## Estados de las publicaciones

Cada publicación puede encontrarse en uno de los siguientes estados:

| Estado | Descripción |
|---|---|
| `borrador` | Publicación en preparación. |
| `publicado` | Publicación disponible. |
| `archivado` | Publicación que ya no se encuentra activa. |

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- JSON
- Git
- GitHub

## Instalación y ejecución

### Clonar el repositorio

```bash
git clone https://github.com/agusmachado7474-beep/PR-Entrega-6.git
```

### Acceder al directorio

```bash
cd PR-Entrega-6
```

### Ejecutar la aplicación

```bash
python main.py
```

## Autor

**Agustín Machado**
