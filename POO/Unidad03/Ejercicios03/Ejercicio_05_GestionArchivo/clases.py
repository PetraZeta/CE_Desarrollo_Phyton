class GestionArchivo:

    @staticmethod
    def buscar_cadena(cadena, archivo):

        try:
            with open(archivo, 'r', encoding='utf8') as file:
                contenido = file.read()
                return cadena in contenido
            
        except IOError:
            return -1 
        
    @staticmethod
    def contar_repeticiones(cadena, archivo):
        try:
            with open(archivo, 'r', encoding='utf8') as file:
                contenido = file.read()
                return contenido.count(cadena)
            
        except IOError:
            return -1 
    
    @staticmethod
    def donde_aparece(cadena, archivo):
        try:
            
            with open(archivo, 'r', encoding='utf8') as file:                
                result = {}
                num_linea = 1
                for linea in file:
                    if cadena in linea:
                        result[num_linea] = linea.strip()   # 1:update_ddasdfasdf
                    num_linea += 1

                return result              


        except IOError:
            return -1 
    
