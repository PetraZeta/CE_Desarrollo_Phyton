import os
from clases import *

ruta_abs = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_abs)
archivo_entrada = os.path.join(directorio, 'user_behavior_dataset.csv')

# Crear archivo csv x dispositivo

# dispositivo = 'Samsung Galaxy S21'
# result = TratarCsv.obtener_csv_por_dispositivo(archivo_entrada, dispositivo)
# if result:
#     print(f'Archivo "{dispositivo}.csv" generado.')
# else:
#     print('Error al crear el archivo.')

# Obtener diccionario con cuenta x sistema operativo
# dicc_result = TratarCsv.obtener_dicc_so(archivo_entrada)
# if dicc_result != -1:
#     print(dicc_result)
# else:
#     print(f'Error al leer el archivo {os.path.basename(archivo_entrada)}.')

# Crear csv con columnas App Usage Time y Gender
result = TratarCsv.obtener_csv_time_gender(archivo_entrada)
if result:
    print(f'Archivo generado.')
else:
    print('Error al crear el archivo.')