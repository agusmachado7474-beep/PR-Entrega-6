## Sistema de Blog en Python

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de blog interactivo por consola, realizado en Python.

El objetivo de esta entrega es aplicar los conceptos de Programación Orientada a Objetos (POO), organizando el código mediante clases y módulos, e incorporando persistencia de datos utilizando archivos JSON.

El sistema permite administrar publicaciones, crear nuevos posts, realizar búsquedas, filtrar por etiquetas, validar información y guardar los datos para conservarlos entre ejecuciones.

## Estructura del proyecto

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

## Programación Orientada a Objetos

El proyecto utiliza tres clases principales:

### Clase Autor

Representa al autor de una publicación.

Atributos:
- `nombre`: nombre del autor.
- `bio`: descripción del autor.
- `especialidad`: área de especialización.
- `redes_sociales`: redes sociales del autor.

Incluye métodos para convertir sus atributos en un diccionario y reconstruir un objeto a partir de un diccionario.

### Clase Post

Representa una publicación del blog.

Atributos:
- `id`: identificador único de la publicación.
- `titulo`: título del post.
- `contenido`: contenido de la publicación.
- `autor`: objeto de la clase Autor.
- `tags`: lista de etiquetas.
- `estado`: estado de la publicación.

Los estados disponibles son:
- `borrador`
- `publicado`
- `archivado`

Incluye métodos para convertir el objeto en un diccionario y reconstruirlo a partir de los datos almacenados.

### Clase Blog

Administra las publicaciones del sistema.

Se encarga de centralizar las operaciones sobre los posts, permitiendo:
- Listar publicaciones.
- Buscar publicaciones por título.
- Filtrar publicaciones por etiqueta.
- Crear nuevos posts.
- Validar publicaciones.
- Obtener y administrar la lista de publicaciones.

## Persistencia de datos con JSON

El sistema utiliza el archivo `posts.json` para almacenar las publicaciones.

Se implementan funciones para:

- **Cargar datos:** recuperar las publicaciones almacenadas al iniciar el programa.
- **Guardar datos:** convertir los objetos en diccionarios y almacenarlos en formato JSON.
- **Reconstruir objetos:** transformar los datos recuperados del archivo en instancias de las clases correspondientes.

También se contempla el manejo de errores ante situaciones como:
- Archivo inexistente.
- Archivo vacío.
- Contenido JSON inválido.
- Datos incompletos o incorrectos.

## Funcionalidades

El sistema cuenta con un menú interactivo por consola que permite realizar las siguientes operaciones:

1. Listar todas las publicaciones.
2. Buscar publicaciones por título.
3. Filtrar publicaciones por etiqueta.
4. Crear una nueva publicación.
5. Validar publicaciones.
6. Guardar los datos en formato JSON.
7. Salir del programa.

Las búsquedas por título y los filtros por etiquetas no distinguen entre mayúsculas y minúsculas.

Durante la creación de publicaciones, el sistema solicita los datos necesarios y valida que la información ingresada sea correcta.

## Tecnologías utilizadas

- **Python 3:** lenguaje de programación.
- **JSON:** formato para almacenar y recuperar información.
- **POO:** utilización de clases, objetos, atributos y métodos.
- **Git y GitHub:** control de versiones y almacenamiento del proyecto.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/agusmachado7474-beep/PR-Entrega-6.git
```

### 2. Ingresar a la carpeta del proyecto

```bash
cd PR-Entrega-6
```

### 3. Ejecutar el programa

```bash
python main.py
```

## Objetivos de aprendizaje

Con esta entrega se busca aplicar y reforzar los siguientes conceptos:

- Creación y utilización de clases y objetos en Python.
- Uso de constructores mediante `__init__`.
- Implementación de métodos y atributos.
- Relación entre objetos de distintas clases.
- Modularización del código mediante paquetes e importaciones.
- Conversión de objetos a diccionarios y viceversa.
- Lectura y escritura de archivos JSON.
- Manejo de excepciones.
- Organización y mantenimiento de proyectos de software.

## Autor

**Agustín Machado**

Proyecto desarrollado como parte de las actividades de aprendizaje de Python.
