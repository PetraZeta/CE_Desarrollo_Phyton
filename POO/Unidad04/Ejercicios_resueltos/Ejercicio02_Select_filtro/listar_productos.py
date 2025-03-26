from db_funciones import *


productos = productos_por_categoria('classic cars')

if productos:
    for producto in productos:
        print(producto[0],producto[1])
elif productos == []:
    print('No se han encontrado productos')
else:
    print('Error')