# Clase que se encarga de la conexión a la base de datos mediante el patrón Singleton
import pymysql

class ConectarBd:
    
    __conexion = None
    
    @classmethod
    def get_conexion(cls):
        try:
            if ConectarBd.__conexion == None:
                ConectarBd.__conexion = pymysql.connect(host='localhost', user='user', 
                                            port=3309, passwd='robocop', database='almacen')
            return ConectarBd.__conexion
        except Exception:
            return False
    
    @classmethod
    def close_conexion(cls):
        try:
            if ConectarBd.__conexion != None:
                ConectarBd.__conexion.close()
                ConectarBd.__conexion = None
        except Exception:
            return False

class OperacionesBd:
    
    def __init__(self):
        self.__conexion = ConectarBd.get_conexion()
                
    def productos(self, categoria):
        try:
            if self.__conexion == False:
                return None
            
            sql = 'select codigoProducto, nombreProducto, precioCompra from ' \
                    'productos where categoriaproducto = %s'
            with self.__conexion.cursor() as cursor:
                cursor.execute(sql, (categoria))
                return list(cursor.fetchall())
        except Exception as e:            
            return None
        
    def actualizar_precio(self, categoria, porcentaje):
        try:
            if self.__conexion == False:
                return None
            
            sql = 'update productos set preciocompra = preciocompra + (preciocompra * %(porcentaje)s / 100) '\
                'where categoriaproducto = %(categoria)s'
            with self.__conexion.cursor() as cursor:
                num_filas = cursor.execute(sql, {
                                    'porcentaje': porcentaje,
                                    'categoria': categoria
                                })
                self.__conexion.commit()
                return num_filas
        except Exception as e:
            return None