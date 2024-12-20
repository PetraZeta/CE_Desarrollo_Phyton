from clases import Producto, GestionAlmacen
print("Lista de productos actuales")
# Llama al método “listado” y muestra los productos existentes
productos = GestionAlmacen.lista_productos()

# añade dos productos nuevos
GestionAlmacen.anadir_producto(
    Producto("003", "cartera", "complemento", 9.99, 1, 2)
    )
GestionAlmacen.anadir_producto(
    Producto("003", "cartera", "complemento", 9.99, 0, 2)
    )

print("-------------------------")
print("Lista de productos tras añadir 2 productos con el mismo id")

productos = GestionAlmacen.lista_productos()
print("-------------------------")
print("Lista de productos bajo minimos")

productos_min = GestionAlmacen.bajo_minimos()
for prod in productos_min:
    print(prod)