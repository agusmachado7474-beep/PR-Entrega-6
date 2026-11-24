import json 

def guardar_posts(blog):
    with open("posts.json", "w", encoding="utf-8") as archivo:
        json.dump(blog.a_diccionario(), archivo, indent=4, ensure_ascii=False)
