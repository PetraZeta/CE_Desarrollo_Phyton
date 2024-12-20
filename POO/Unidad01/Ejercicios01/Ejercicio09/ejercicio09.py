# importación de la clase Producto del módulo clases
from clases import Producto

# creación de una lista de productos
productos = [
    Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50),
    Producto("pera", "fruta", 2.7, 75),
    Producto("plátano", "fruta", 12.7, 75),
]     
# Calcular media de precios
suma_precios = 0
for pro in productos:
    suma_precios += pro.precio

media = suma_precios / len(productos)

print(f"La media de precios es {media}")

