import pymysql

def actualizar_unidades_producto(codigo, unidades):
    try:
        with pymysql.connect(host='localhost', user='user', password='robocop', \
            port=3309, database='almacen') as conexion:

            with conexion.cursor() as cursor:
                sql="update productos set unidadesStock = unidadesStock + %(uni)s  \
                    where codigoProducto = %(cod)s"
                print(sql)
                numero = cursor.execute(sql,{
                    'uni': unidades,
                    'cod': codigo
                })
                
            conexion.commit() # Confirmar la actualización
        return numero

    except pymysql.MySQLError as error:
        print(f'Error de MySQL: {error}')
        return None