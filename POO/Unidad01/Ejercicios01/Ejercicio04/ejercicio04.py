# importación de la clase Producto del módulo clases
from clases import Producto

# creación de dos objetos de la clase Producto
pro1 = Producto("tomate", "fruta", 2.3, 100)
pro2 = Producto("papa", "verdura", 1.5, 200)

# mostrar productos antes
print("Productos antes de actualizar cantidad")
print(pro1)
print(pro2)
print()

# actualizar cantidad
pro1.actualizar_cantidad(50)
pro2.actualizar_cantidad(150)

# mostrar productos después
print("Productos después de actualizar cantidad")
print(pro1)
print(pro2)


