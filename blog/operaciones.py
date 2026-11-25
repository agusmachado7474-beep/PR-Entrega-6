
import json


def cargar_posts():
    try:
        with open("posts.json", "r", encoding="utf-8") as archivo:
            posts = json.load(archivo)

            if not isinstance(posts, list):
                print("El archivo no contiene una lista de publicaciones.")
                return []

            return posts

    except FileNotFoundError:
        print("No se encontró el archivo posts.json.")
        return []

    except json.JSONDecodeError:
        print("El archivo JSON está vacío o contiene datos inválidos.")
        return []


def guardar_posts(posts):
    try:
        with open("posts.json", "w", encoding="utf-8") as archivo:
            json.dump(posts, archivo, ensure_ascii=False, indent=4)

        print("Publicaciones guardadas correctamente.")

    except (TypeError, OSError):
        print("No se pudieron guardar las publicaciones.")


def listar_posts(lista):
    if not lista:
        print("No hay publicaciones para mostrar.")
        return

    for post in lista:
        print("----------------------")
        print("ID:", post.get("id"))
        print("Título:", post.get("titulo"))
        print("Autor:", post.get("autor", {}).get("nombre"))
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
        for etiqueta in post.get("tags", []):
            if etiqueta.lower() == tag.lower():
                resultados.append(post)
                break

    return resultados

                break

    return resultados
