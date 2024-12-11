# importación de la clase Producto del módulo clases
from clases import Producto

# creación de dos objetos de la clase Producto
pro1 = Producto("tomate", "fruta", 2.3, 100)
pro2 = Producto("papa", "verdura", 1.5, 200)

# comparar los precios
if pro1.precio > pro2.precio:
    print("El producto mas caro es: ", pro1)
else:
    print("El producto mas caro es: ", pro2)
