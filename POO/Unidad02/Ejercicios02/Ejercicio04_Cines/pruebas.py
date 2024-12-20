# Probar las clases
from clases import *

nuevo_cine = Cine(5, 'DeVerano', 'Sol, 40', '924003311', 'deverano@cines.es')
nuevo_cine.agregar_sala(4, 200, True)
nuevo_cine.agregar_sala(5, 100, False)
nuevo_cine.agregar_sala(5, 200, True)  # No se añadirá
CinesListado.agregar_cine(nuevo_cine)


# nombres de los cines
lista_cines = CinesListado.lista_nombres_cines()
print(*lista_cines, sep="\n")

# dicc cine:telefono
dicc = CinesListado.dicc_cine_telefono()
print(dicc)

# dicc. cine:num_salas
dicc = CinesListado.dicc_cine_num_salas()
print(dicc)

# capacidad total cine 
capacidad_total = CinesListado.capacidad_total_cine(5)
print(capacidad_total)