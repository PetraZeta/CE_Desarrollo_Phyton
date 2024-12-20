import os

ruta_archivo = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_archivo)
archivo_ent = os.path.join(directorio, "mas_operaciones.txt")
archivo_sal = os.path.join(directorio, "operaciones.txt")

try:

    with open(archivo_ent, "r") as file_ent:
        with open(archivo_sal, "a") as file_sal:
            for linea in file_ent:
                file_sal.write(linea)

except IOError as e:
    print(f"Error: {e}")

finally:
    print("Proceso terminado.")
