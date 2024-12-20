# clase vehículo
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return self.nombre + "-" + self.categoria + "-" \
                + str(self.precio) + "-" + str(self.cantidad)
    