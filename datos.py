
import json
from pathlib import Path
from .modelos import Blog, Post

RUTA_ARCHIVO = Path(__file__).resolve().parent.parent / "posts.json"


def cargar_posts():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            print("Error: el archivo JSON debe contener una lista de publicaciones.")
            return Blog()

        posts = []

        for dato in datos:
            try:
                post = Post.desde_diccionario(dato)
                posts.append(post)
            except (KeyError, TypeError, ValueError, AttributeError):
                print("Se encontró una publicación con datos incorrectos.")

        return Blog(posts)

    except FileNotFoundError:
        print("No existe el archivo posts.json. Se iniciará un blog vacío.")
        return Blog()

    except json.JSONDecodeError:
        print("El archivo posts.json está vacío o contiene JSON inválido.")
        return Blog()

    except OSError as error:
        print(f"Error al leer el archivo: {error}")
        return Blog()


def guardar_posts(blog):
    try:
        datos = blog.a_diccionario()

        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

        print("Publicaciones guardadas correctamente.")
