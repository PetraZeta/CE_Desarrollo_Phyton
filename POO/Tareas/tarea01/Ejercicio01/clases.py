# clase producto
# atributos: identificador, nombre del producto, categoría, precio de venta, 
# stock y stock mínimo
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

# metodo actualizar_stock  
    def actualizar_stock(self, valor):
        self.stock += valor

# metodo esta_en_minimos
    def esta_en_minimos(self):
        if self.stock < self.stock_minimo:
            return True
        else:
            return False
        
# mostrar el identificador, nombre y stock del producto
    def __repr__(self):
        return ( 
            f"Producto: {self.identificador}, {self.nombre_producto}, "
            f"{self.stock})"
        )
    
# determinar si dos productos son iguales
    def __eq__(self, otro_producto):
        return self.identificador == otro_producto.identificador