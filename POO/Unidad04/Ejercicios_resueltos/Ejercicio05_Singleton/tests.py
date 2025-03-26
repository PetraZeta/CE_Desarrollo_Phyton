from clases import OperacionesBd

operaciones = OperacionesBd()
otras_operaciones = OperacionesBd()

productos = operaciones.productos('classic cars')
if productos:
    for producto in productos:
        print(producto)
else:
    print('Ha ocurrido algún error')
# filas = operaciones.actualizar_precio('classic cars', -10)
# print('Filas actualizadas:', filas)
    
    