from datetime import date


class Publicacion:
    def __init__(self, titulo, editorial, fecha, idioma):
        self.titulo = titulo
        self.editorial = editorial
        self.fecha = fecha
        self.idioma = idioma

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"


class Libro(Publicacion):
    def __init__(self, isbn, titulo, editorial, fecha, idioma, autor, genero):
        super().__init__(titulo, editorial, fecha, idioma)
        self.isbn = isbn
        self.autor = autor
        self.genero = genero

    def __str__(self):
        return f"Libro: {self.titulo} - {self.autor} - {self.genero}"


class Revista(Publicacion):
    def __init__(self, titulo, editorial, fecha, idioma, numero, area):
        super().__init__(titulo, editorial, fecha, idioma)
        self.numero = numero
        self.area = area

    def __str__(self):
        return f"Revista: {self.titulo} - {self.area}"


class Periodico(Publicacion):
    def __init__(self, titulo, editorial, fecha, idioma, seccion):
        super().__init__(titulo, editorial, fecha, idioma)
        self.seccion = seccion

    def __str__(self):
        return (
            f"Periodico: {self.titulo} - {self.seccion}"
        )


class ListaPublicaciones:

    publicaciones = [
        Libro(
            "1234",
            "El Quijote",
            "Anaya",
            date(1605, 1, 1),
            "Español",
            "Cervantes",
            "Novela",
        ),
        Libro(
            "5678",
            "El Señor de los Anillos",
            "Minotauro",
            date(1954, 7, 29),
            "Inglés",
            "J.R.R. Tolkien",
            "Fantasía",
        ),
        Revista("Muy Interesante", "G+J", date(1981, 1, 1), "Español", 123, "Ciencia"),
        Revista(
            "National Geographic", "RBA", date(2022, 1, 1), "Inglés", 123, "Naturaleza"
        ),
        Revista("Vogue", "Conde Nast", date(1892, 1, 1), "Inglés", 123, "Moda"),
        Revista("Time", "Time Inc.", date(2024, 1, 1), "Inglés", 123, "Actualidad"),
        Revista("Hola", "Hola S.L.", date(2024, 1, 1), "Español", 123, "Corazón"),
        Periodico("El País", "Prisa", date(1999, 1, 1), "Español", "Internacional"),
        Periodico(
            "The New York Times",
            "The New York Times Company",
            date(1851, 1, 1),
            "Inglés",
            "Internacional",
        ),
        Periodico(
            "The Guardian",
            "Guardian Media Group",
            date(1821, 1, 1),
            "Inglés",
            "Internacional",
        ),
        Periodico(
            "Le Monde", "Groupe Le Monde", date(1944, 1, 1), "Francés", "Internacional"
        ),
        Periodico(
            "La Repubblica",
            "GEDI Gruppo Editoriale",
            date(1976, 1, 1),
            "Italiano",
            "Internacional",
        ),
        Periodico(
            "Bild", "Axel Springer SE", date(1952, 1, 1), "Alemán", "Internacional"
        ),
    ]

    @classmethod
    def mostrar_publicaciones_libro(cls):
        for publicacion in cls.publicaciones:
            if isinstance(publicacion, Libro):     
                print(publicacion)

    @classmethod
    def contar_publicaciones_tipo(cls, tipo):
        return len(
            [   p
                for p in cls.publicaciones
                if isinstance(p, Libro) and tipo.lower() == "libro"
                or isinstance(p, Revista) and tipo.lower() == "revista"
                or isinstance(p, Periodico) and tipo.lower() == "periodico"
            ]
        )

    @classmethod
    def lista_de_revistas(cls):
        return [
            publicacion
            for publicacion in cls.publicaciones
            if isinstance(publicacion, Revista)
        ]

    @classmethod
    def cuenta_por_tipo(cls):
        return {
            "Libro": cls.contar_publicaciones_tipo("Libro"),
            "Revista": cls.contar_publicaciones_tipo("Revista"),
            "Periódico": cls.contar_publicaciones_tipo("Periodico"),
        }
        

    @classmethod
    def tupla_idiomas(cls):
        return tuple(set(publicacion.idioma for publicacion in cls.publicaciones))


if __name__ == "__main__":
    print(f"{ListaPublicaciones.contar_publicaciones_tipo('Libro')} libros")
    print(f"{ListaPublicaciones.contar_publicaciones_tipo('Revista')} revistas")
    print(f"{ListaPublicaciones.contar_publicaciones_tipo('Periodico')} periódicos")
    print(f"{ListaPublicaciones.tupla_idiomas()}")
