import csv, os

from clases import *

directorio = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio, 'summer_olympic_medals.csv')
juegos = GestionJuegos(ruta_archivo)

# Prueba de obtener_datos_pais
# print(*juegos.obtener_datos_pais("ESP"), sep="\n")

# # Prueba de total_medallas_pais_juegos
print(f"Total medallas ESP 2020:", juegos.total_medallas_pais_juegos("ESP", 2020))

# Prueba de generar_csv
result = juegos.generar_csv("GER")
print(result)
