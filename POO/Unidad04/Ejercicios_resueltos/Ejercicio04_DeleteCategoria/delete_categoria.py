import os
from db_funciones import eliminar_categoria


# Categoria a eliminar
categoria = 'Classic cars'
numero = eliminar_categoria(categoria)
if numero > 0:
    print(f'Se han eliminado la categoría {categoria}')
elif numero == 0:
    print(f'No existe la categoría {categoria}')
else:
    print(f'Error al eliminar la categoría {categoria}')


