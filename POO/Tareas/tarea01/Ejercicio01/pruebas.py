from clases import Producto

# Instancia dos objetos.
productos = [
    Producto("001", "chaleco", "ropa", 29.99, 6, 2),
    Producto("002", "bolso", "complemento", 19.99, 4, 2)
]

# Imprime ambos objetos.
for pro in productos:
    print(pro)
print("-------------------------")

# Actualiza las unidades del primero.
print(productos[0].stock)
print("-------------------------")


# Imprime el primer objeto.
print(productos[0])
print("-------------------------")

# Comprueba si el segundo está en mínimos.
print(Producto.esta_en_minimos(productos[0]))
print("-------------------------")

# Comprueba si son iguales.
print(productos[0] == productos[1])
print("-------------------------")
