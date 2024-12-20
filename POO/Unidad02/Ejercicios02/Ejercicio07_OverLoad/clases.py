

class Pedido:
    def __init__(self, id, fecha, cliente):
        self.id = id
        self.fecha = fecha
        self.cliente = cliente
        self.productos = ['manzanas', 'peras']

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente} \n {self.productos}'

    def __add__(self, producto):
        self.productos.append(producto)
    
    def __sub__(self, producto):
        self.productos.remove(producto)  # Eliminar de la lista
    
    def __len__(self):
        return len(self.productos)
    
    def __iadd__(self, otro_pedido):    # +=
        for p in otro_pedido.productos:
            self.productos.append(p)
        return self

    def __bool__(self):                 # bool()
        return len(self.productos) > 0