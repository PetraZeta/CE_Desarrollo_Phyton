from archivos_datos.funciones import cargar_plantas


class Plantas:
    def __init__(self):
        self.plantas = cargar_plantas()
