import csv, json


def dicc_resultados_pais(archivo, country_code):
    try:
        with open(archivo, 'r', encoding='utf8') as archivo_entrada:

            csv_reader = csv.reader(archivo_entrada)
            cabeceras = next(csv_reader)

            datos = list(csv_reader)
            dicc = {}
            for elemento in datos:
                if country_code in elemento:
                    dicc[int(elemento[0])] = [
                        int(elemento[5]),
                        int(elemento[6]),
                        int(elemento[7])
                    ]
        return dicc
    except IOError:
        return False

def crear_json_medallas_pais(archivo_csv, archivo_json, country_code):

    try:
        
        diccionario_medallas = dicc_resultados_pais(archivo_csv, country_code)
        if diccionario_medallas:
            with open(archivo_json, 'w', encoding='utf8') as json_file:
                json.dump(diccionario_medallas, json_file)

    except IOError:
        return False
    else:
        return True