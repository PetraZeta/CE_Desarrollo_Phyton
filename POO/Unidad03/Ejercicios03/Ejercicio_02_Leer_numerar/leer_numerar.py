import os

ruta_archivo = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_archivo)
archivo = os.path.join(directorio, "operaciones.txt")

try:

    with open(archivo, "r") as file:
        lista = file.readlines()
        numero = 0
        for linea in lista:
            print(f"{numero}: {linea.strip()}")
            numero += 1

except IOError as e:
    print(f"Error: {e}")
