import os

ruta_archivo = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_archivo)
archivo_ent = os.path.join(directorio, "operaciones.txt")

try:

    texto_buscado = "delete"
    with open(archivo_ent, "r") as file:
        lista = file.readlines()
        for linea in lista:
            if texto_buscado in linea:
                print(f"Texto encontrado: {linea.strip()}")


except IOError as e:
    print(f"Error: {e}")

finally:
    print("Proceso terminado.")
