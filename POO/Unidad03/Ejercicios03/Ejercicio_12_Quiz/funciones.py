import json, os, csv

def leer_json_preguntas(archivo_json):
    try:
        with open(archivo_json, 'r') as file:
            preguntas = json.load(file)
            return preguntas
    except IOError:        
        return None

def leer_json_configuracion(archivo_config):
    try:
        with open(archivo_config, 'r') as file:
            dicc_config = json.load(file)
            return dicc_config
    except IOError:        
        return None
        

def check_top3(archivo_top3, usuario, puntos):
    try:
        # Abro top3.json para lectura y leo el dicc.
        with open(archivo_top3, 'r') as file:
            diccionario_top3 = json.load(file)
           
        el_top3 = diccionario_top3['top3']

        # obtener el valor, la lista de puntosç
        # los puntos q llegan superan al tercero
        if puntos > el_top3[2]['puntuacion']:

            # Abro top3.json para escritura.
            with open(archivo_top3, 'w', encoding='utf8') as file:  
                el_top3[2]['nombre'] = usuario
                el_top3[2]['puntuacion'] = puntos
            
                el_top3 = sorted(el_top3, key= lambda x: x['puntuacion'], reverse=True)

                # cambio el valor de la key top3
                diccionario_top3['top3'] = el_top3

                # grabar json
                json.dump(diccionario_top3, file, indent=4)

            return True    # Entra en top3
        return False    # No top3
    except IOError:        
        return None
    

def get_top3(archivo_top3):
    try:
        # Abro top3.json para lectura y leo el dicc.
        with open(archivo_top3, 'r') as file:
            diccionario_top3 = json.load(file)
        return diccionario_top3
    except IOError:
        return None