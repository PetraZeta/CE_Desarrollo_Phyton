from db_funciones import actualizar_unidades_producto

codigo = 'S10_1678'
unidades = 10
resultado = actualizar_unidades_producto(codigo, unidades)
if resultado == 1:
    print(f'Se ha actualizado el producto {codigo}')
else:
    print(f'Error al actualizar el producto {codigo}')