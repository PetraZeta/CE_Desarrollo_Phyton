import csv, json
from collections import defaultdict


def generar_diccionario_actividades(ruta_archivo):
    try:
        ddata = defaultdict(lambda: [0, 0, 0])
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                actividad = fila["Workout_Type"]
                ddata[actividad][0] += 1  # Total apariciones
                if fila["Gender"] == "Female":
                    ddata[actividad][1] += 1  # Total mujeres
                else:
                    ddata[actividad][2] += 1  # Total hombres
        return dict(ddata)  # Convierte defaultdict a dict estándar
    except FileNotFoundError:
        print("No se encontró el archivo de entrada.")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None


ruta_archivo = "gym_data.csv"
diccionario = generar_diccionario_actividades(ruta_archivo)

if diccionario is not None:
    print("Diccionario generado correctamente:")
    for clave, valores in diccionario.items():
        print(f"{clave}: {valores}")
else:
    print("No se pudo generar el diccionario.")


def guardar_json(diccionario, ruta_json):
    try:
        with open(ruta_json, mode="w", encoding="utf-8") as archivo_json:
            json.dump(diccionario, archivo_json, indent=4, separators=(", ", ": "))
        print(f"Archivo JSON guardado correctamente: {ruta_json}")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")
        return False


ruta_json = "gym_data_summary.json"
if diccionario is not None:
    guardar_json(diccionario, ruta_json)
