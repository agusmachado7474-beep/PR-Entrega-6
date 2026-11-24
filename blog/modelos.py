class Autor:
    def __init__(self, nombre, bio, especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            nombre=datos["nombre"],
            bio=datos["bio"],
            especialidad=datos.get("especialidad", ""),
            redes_sociales=datos.get("redes_sociales", [])
        )


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def desde_diccionario(cls, datos):
        autor = Autor.desde_diccionario(datos["autor"])

        return cls(
            id=datos["id"],
            titulo=datos["titulo"],
            contenido=datos["contenido"],
            autor=autor,
            tags=datos["tags"],
            estado=datos["estado"]
        )


class Blog:
    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def listar_posts(self):
        for post in self.posts:
            print(f"Título: {post.titulo}")
            print(f"Autor: {post.autor.nombre}")
            print(f"Estado: {post.estado}")
            print("-" * 30)

    def buscar_por_titulo(self, termino):
        resultados = []

        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag):
        resultados = []

        for post in self.posts:
            if tag.lower() in [t.lower() for t in post.tags]:
                resultados.append(post)

        return resultados

    def crear_post(self, post):
        if self.validar_post(post):
            self.posts.append(post)
            return True

        return False

    def validar_post(self, post):
        return (
            isinstance(post, Post)
            and isinstance(post.autor, Autor)
            and bool(post.titulo.strip())
            and bool(post.contenido.strip())
            and isinstance(post.tags, list)
            and len(post.tags) > 0
            and post.estado in ("borrador", "publicado", "archivado")
        )

    def obtener_posts(self):
        return self.posts

    def a_diccionario(self):
        return [post.a_diccionario() for post in self.posts]

    @classmethod
    def desde_diccionario(cls, datos):
        posts = [Post.desde_diccionario(post) for post in datos]
        return cls(posts)
