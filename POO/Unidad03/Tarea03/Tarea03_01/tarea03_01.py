import csv
import os

print("1. Agregar contenido de un archivo a otro")
print("--------------------------------------")


def agregar_archivo(archivo1, archivo2):
    try:
        with open(archivo1, mode="a", newline="", encoding="utf-8") \
            as archivo_a, open(archivo2, mode="r", encoding="utf-8") \
                as archivo_r:
            reader = csv.reader(archivo_r)
            print(reader)
            writer = csv.writer(archivo_a)
            for row in reader:
                writer.writerow(row)
        return True
    except FileNotFoundError:
        print("No se encontró el archivo")
        return False
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    directorio = os.path.dirname(os.path.abspath(__file__))
    ruta_ciudades = os.path.join(directorio, "ciudades.csv")
    ruta_mas_ciudades = os.path.join(directorio, "mas_ciudades.csv")

    if agregar_archivo(ruta_ciudades, ruta_mas_ciudades):
        print("Archivo ciudades.csv actualizado")
    else:
        print("No se pudo actualizar el archivo")