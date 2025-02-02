import os
from tarea03_02 import actividad_genero_csv

print("2_b. Generar un archivo CSV con las columnas edad, género, \
      horas y actividad,")
print("--------------------------------------")

directorio = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio, "gym_data.csv")
ruta_csv = os.path.join(directorio, "gym_data_new.csv")

if actividad_genero_csv(ruta_archivo, ruta_csv, "Female", "HIIT"):
    print("Archivo csv creado")
else:
    print("No se pudo crear el archivo")