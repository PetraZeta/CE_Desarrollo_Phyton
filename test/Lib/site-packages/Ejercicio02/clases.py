# clase producto
class Producto:
    def __init__(self, identificador, nombre_producto, categoria,
                 precio_venta, stock, stock_minimo):
        self.identificador = identificador
        self.nombre_producto = nombre_producto
        self.categoria = categoria
        self.precio_venta = precio_venta
        self.stock = stock
        self.stock_minimo = stock_minimo
    
    def __str__(self):
        return (
            f"Producto {self.identificador} | "
            f"Nombre: {self.nombre_producto} | "
            f"Categoría: {self.categoria} | PVP: {self.precio_venta} | "
            f"stock: {self.stock}"

        )

    def actualizar_stock(self, valor):
        self.stock += valor

    def esta_en_minimos(self):
        if self.stock < self.stock_minimo:
            return True
        else:
            return False

    def __repr__(self):
        return ( 
            f"Producto: {self.identificador}, {self.nombre_producto}, "
            f"{self.stock})"
        )
    
    def __eq__(self, otro_producto):
        return self.identificador == otro_producto.identificador
    

# clase GestionAlmacen
class GestionAlmacen:
    productos = [
        Producto("001", "chaleco", "ropa", 29.99, 6, 2),
        Producto("002", "bolso", "complemento", 19.99, 2, 2)
    ]

# anadir producto
    @classmethod
    def anadir_producto(cls, nuevo_producto):
        if nuevo_producto in cls.productos:
            return False
        else:
            cls.productos.append(nuevo_producto)
            return True
        
# buscar por id
    @classmethod
    def buscar_por_id(cls, id_producto):
        for producto in cls.productos:
            if producto.identificador == id_producto:
                return producto
        return None
    
# lista de productos bajo minimos
    @classmethod
    def bajo_minimos(cls):
        lista_bajo_min = []
        for producto in cls.productos:
            if producto.esta_en_minimos():
                lista_bajo_min.append(producto)
        return lista_bajo_min

# lista de productos 
    @classmethod
    def lista_productos(cls):
        for producto in cls.productos:
            print(producto)