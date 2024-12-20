import os
from funciones import *

ruta_abs = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_abs)
archivo_csv_entrada = os.path.join(directorio, 'Summer_olympic_Medals.csv')

# diccionario = dicc_resultados_pais(archivo_csv_entrada, 'ESP')
# if diccionario:
#     for k,v in diccionario.items():
#         print(f'{k}: {v}')
# else:
#     print(f'Error al leer el archivo {os.path.basename(archivo_csv_entrada)}')


# Opción crear JSON a partir del diccionario
country_code = 'GER'
archivo_json_salida = os.path.join(os.path.dirname(__file__), country_code + '.json')

result = crear_json_medallas_pais(archivo_csv_entrada, archivo_json_salida, country_code)
if result:
    print('Archivo creado')
else:
    print('Error')