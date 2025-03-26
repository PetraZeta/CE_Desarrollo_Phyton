import pymysql

def productos_por_categoria(categoria):
    try:
        with pymysql.connect(host='localhost', user='user', password='robocop',\
        port=3309,database='almacen') as conexion:

            with conexion.cursor() as cursor:
                sql='SELECT * FROM productos WHERE categoriaProducto = %(cat)s'
                cursor.execute(sql,{
                    'cat':categoria
                })

        return cursor.fetchall()

    except pymysql.MySQLError as error:
        print(f'Error de MySQL: {error}')
        return None