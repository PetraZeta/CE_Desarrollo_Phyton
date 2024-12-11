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
    
    def actualizar_cantidad(self, valor):
        self.cantidad += valor     # self.cantidad = self.cantidad + valor