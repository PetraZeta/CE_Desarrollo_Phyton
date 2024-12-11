# importación de la clase Producto del módulo clases
from clases import Producto

# creación de una lista de productos
productos = [Producto("tomate", "fruta", 2.3, 100),
             Producto("patata", "verdura", 1.5, 200),
             Producto("cebolla", "verdura", 1.8, 150),
             Producto("manzana", "fruta", 3.2, 50),
             Producto("pera", "fruta", 2.7, 75)]


# mostrar solo las verduras
# mediante un bucle for recorremos la lista de productos
# y mostramos solo los productos que sean verduras
for producto in productos:
    if producto.precio >= 1.5 and producto.precio <= 2.5:
        print(producto)