import csv, os

try:
    directorio = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio, 'departaments.csv')
    
    with open(ruta_archivo, "r") as archivo:
        lector = csv.reader(archivo)

        # La función next() retorna el siguiente elemento de un iterador.
        # En este caso, retorna la primera fila del archivo CSV.
        cabeceras = next(lector)  # obtener la primera fila del archivo. Cabeceras.

        for linea in lector:
            print(linea)

        # print(f"Cabeceras: {cabeceras}")
        print(
            f"Total de registros: {lector.line_num - 1}"
        )  # restar 1 para no contar las cabeceras

except FileNotFoundError:
    print("El archivo no existe")
