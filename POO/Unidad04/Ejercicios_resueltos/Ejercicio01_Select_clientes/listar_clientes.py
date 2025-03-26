import pymysql

try:
    with pymysql.connect(host='localhost', user='user', password='robocop', \
        port=3309, database='almacen') as conexion:
        with conexion.cursor() as cursor:

            numero_clientes=cursor.execute('SELECT * FROM clientes')
            print(f'Número de clientes: {numero_clientes}')

        for cliente in cursor.fetchall():
            print(cliente)

except  pymysql.MySQLError as error:
    print(f'Error de MySQL: {error}')