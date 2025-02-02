import csv, json
from collections import defaultdict


def recuento_actividades(lector):
    ddata = defaultdict(lambda: [0, 0, 0])
    for fila in lector:
        actividad = fila["Workout_Type"]
        ddata[actividad][0] += 1
        if fila["Gender"] == "Female":
            ddata[actividad][1] += 1
        else:
            ddata[actividad][2] += 1
    return ddata


def recuento_actividades_json(ruta_archivo, ruta_json):
    try:
        diccionario = recuento_actividades(ruta_archivo)
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            ddata = recuento_actividades(lector)
            print(ddata)

        with open(ruta_json, "w", encoding="utf-8") as archivo_json:
            json.dump(diccionario, archivo_json, indent=4, separators=(", ", ": "))
        return True
    except FileNotFoundError:
        print("No se encontró el archivo")
        return False
    except Exception as e:
        print(e)
        return False


def actividad_genero_csv(ruta_archivo, ruta_csv, genero, actividad):
    try:
        filas_filtradas = []
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)      
            for fila in lector:
                if fila["Gender"] == genero \
                        and fila["Workout_Type"] == actividad:
                    filas_filtradas.append(
                        {
                            "Age": fila["Age"],
                            "Gender": fila["Gender"],
                            "Hours": fila["Session_Duration (hours)"],
                            "Activity": fila["Workout_Type"]
                        }
                    )
        with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo_csv:
            fieldnames = ["Age", "Gender", "Hours", "Activity"]
            writer = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filas_filtradas)
        return True
    except FileNotFoundError:
        print("No se encontró el archivo")
        return False
    except Exception as e:
        print(e)
        return False