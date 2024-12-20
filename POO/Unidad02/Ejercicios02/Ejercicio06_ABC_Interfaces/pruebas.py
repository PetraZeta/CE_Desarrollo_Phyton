from clases_interfaces import *

# Pruebas de la clase ListaNumeros
# mi_lista = ListaNumeros([1, 2, 3, 4, 5])
# mi_lista.nuevo_numero(-6)
# mi_lista.ordenar()
# mi_lista.mostrar()
# result = mi_lista.buscar_numero(-3)
# print(f"está el 3? {result}")

# Pruebas de la clase TuplaNumeros
mi_tupla = TuplaNumeros((1, 2, 3, 4, -5))
mi_tupla.nuevo_numero(-6)
mi_tupla.ordenar()
result = mi_tupla.buscar_numero(-3)
print(f"está el -3? {result}")
mi_tupla.mostrar()