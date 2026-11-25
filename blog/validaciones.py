from blog.datos import estados_post, etiquetas_blog


def validar_post(post):

    if not isinstance(post, dict):
        return False, "No es un diccionario"

    claves = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    for clave in claves:
        if clave not in post:
            return False, f"Falta la clave {clave}"

    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "Título vacío o inválido"

    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "Contenido vacío o inválido"

    if post["estado"] not in estados_post:
        return False, "Estado inválido"

    if not isinstance(post["autor"], dict):
        return False, "Autor inválido"

    if not post["autor"].get("nombre") or not post["autor"].get("bio"):
        return False, "Faltan datos del autor"

    if not isinstance(post["tags"], list) or not post["tags"]:
        return False, "Tags inválidos"

    for tag in post["tags"]:
        if not isinstance(tag, str) or tag not in etiquetas_blog:
            return False, f"Tag inválido: {tag}"

    return True, "Correcto"
