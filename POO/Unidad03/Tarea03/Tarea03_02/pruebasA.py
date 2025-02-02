import os
from tarea03_02 import recuento_actividades_json

print("2_a. Generar un archivo JSON con las parejas actividad: \
       nombre-actividad: \
       [total_apariciones, total_mujeres, total_hombres]")
print("--------------------------------------")

directorio = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio, "gym_data.csv")
ruta_json = os.path.join(directorio, "gym_data.json")

if recuento_actividades_json(ruta_archivo, ruta_json):
    print("Archivo json creado")
else:
    print("No se pudo crear el archivo")