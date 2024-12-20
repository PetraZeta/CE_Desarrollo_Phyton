# importación de la clase Producto del módulo clases
from clases import Producto

# creación de una lista de productos
productos = [Producto("tomate", "fruta", 2.3, 100),
             Producto("patata", "verdura", 1.5, 200),
             Producto("cebolla", "verdura", 1.8, 150),
             Producto("manzana", "fruta", 3.2, 50),
             Producto("pera", "fruta", 2.7, 75)]

# obtener la media de los precios de las verduras
suma_precios = 0
cuenta_verduras = 0
for producto in productos:
    # preguntamos si el producto es una verdura
    # en caso afirmativo sumamos el precio del producto
    # y aumentamos el contador de verduras
    if producto.categoria.lower() == "verdura":
        suma_precios += producto.precio
        cuenta_verduras += 1

# al final del bucle calculamos la media
media = suma_precios / cuenta_verduras
print(f"La media de los precios de las verduras es {media}")
