

import json
from pathlib import Path

RUTA_ARCHIVO = Path(__file__).parent / "posts.json"
print("Ruta del archivo:", RUTA_ARCHIVO)
print("¿Existe el archivo?:", RUTA_ARCHIVO.exists())


def cargar_posts():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            posts = json.load(archivo)

            if isinstance(posts, list):
                return posts
            else:
                print("El archivo no contiene una lista de publicaciones.")
                return []

    except FileNotFoundError:
        print("No se encontró el archivo de publicaciones.")
        return []

    except json.JSONDecodeError:
        print("El archivo JSON está vacío o tiene datos inválidos.")
        return []


def guardar_posts(posts):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(posts, archivo, ensure_ascii=False, indent=4)


def listar_posts(lista):
    if not lista:
        print("No hay publicaciones para mostrar.")
        return

    for post in lista:
        print("\n-----------------------------")
        print("ID:", post.get("id"))
        print("Título:", post.get("titulo"))
        print("Contenido:", post.get("contenido"))
        print("Estado:", post.get("estado"))
        print("Tags:", post.get("tags"))


def buscar_por_titulo(lista, termino):
    resultados = []

    for post in lista:
        titulo = post.get("titulo", "")

        if termino.lower() in titulo.lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    resultados = []

    for post in lista:
        etiquetas = post.get("tags", [])

        for etiqueta in etiquetas:
            if etiqueta.lower() == tag.lower():
                resultados.append(post)
                break

    return resultados
