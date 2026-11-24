 
class Autor:
    def __init__(self, nombre, bio, especialidad):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad 

    
    def a_diccionario(self):
        return { 
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad}
    
    


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
            "estado": self.estado }   
    