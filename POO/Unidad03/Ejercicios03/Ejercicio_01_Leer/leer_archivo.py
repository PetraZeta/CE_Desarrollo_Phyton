import os

ruta_archivo = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_archivo)
archivo = os.path.join(directorio, "operaciones.txt")

try:

    with open(archivo, "r") as file:
        contenido = file.read()
        print(contenido)

except IOError as e:
    print(f"Error: {e}")
