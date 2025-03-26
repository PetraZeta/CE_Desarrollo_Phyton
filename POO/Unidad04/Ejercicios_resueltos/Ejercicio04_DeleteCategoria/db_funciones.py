import pymysql

def eliminar_categoria (categoria):
    try:
        with pymysql.connect(host='localhost', user='user', password='robocop', \
            port=3309, database='almacen') as conexion:

            with conexion.cursor() as cursor:
                sql="delete from categoriasproductos where categoria = %(cat)s"
                numero = cursor.execute(sql,{
                    'cat': categoria
                })
                
            conexion.commit() # Confirmar la actualización
        return numero

    except pymysql.MySQLError as error:
        #print(f'Error de MySQL: {error}')
        return -1