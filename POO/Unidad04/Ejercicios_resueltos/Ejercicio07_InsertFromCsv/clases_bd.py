import pymysql

# Clase que se encarga de la conexión a la base de datos
class ConectarBd:
    
    __instance = None
    
    def get_conexion(self):
        try:
            if ConectarBd.__instance == None:
                ConectarBd.__instance = pymysql.connect(host='localhost', user='user', 
                                            port= 3309, passwd='robocop', db='almacen')
            return ConectarBd.__instance
        except Exception as e:
            return False
        
    def close_conexion(self):
        try:
            if ConectarBd.__instance != None:
                ConectarBd.__instance.close()
                ConectarBd.__instance = None
            return True
        except Exception as e:
            return False


# Clase que se encarga de añadir un cliente a la base de datos
class OperacionesBd:
    
    @classmethod
    def anadir_clientes(cls, lista_clientes):
        # Añadimos los clientes a la base de datos
        contador = 0
        for cliente in lista_clientes:
            if cls.anadir(cliente):
                contador += 1
            else:
                print(f"Error al añadir el cliente {cliente}")
        return contador
                
    
    @classmethod
    def anadir(cls, lista_valores):
        # Añadimos el cliente a la base de datos
        try:
            # Obtenemos la conexión a la base de datos
            conexion = ConectarBd().get_conexion()
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO clientes (numerocliente, nombre, apellido, telefono, correo) "\
                    "VALUES (%s, %s, %s, %s, %s)", lista_valores)
                conexion.commit()
            return True
        except Exception as e:
            return False
        