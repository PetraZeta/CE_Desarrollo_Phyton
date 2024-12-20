from archivos_datos.funciones import cargar_mamiferos


class Mamiferos:
    def __init__(self):
        self.mamiferos = cargar_mamiferos()
