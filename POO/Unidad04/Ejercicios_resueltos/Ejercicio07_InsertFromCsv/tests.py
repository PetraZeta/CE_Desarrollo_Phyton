import os
from clases_bd import *
from clases_csv import *


# ruta absoluta del archivo csv
archivo_csv = os.path.join(os.path.dirname(__file__), 'clientes.csv')

# importar los datos del csv
csv = CsvClientes(archivo_csv)
clientes = csv.leer_csv()

# Llamar al método anadir_cliente
numero = OperacionesBd.anadir_clientes(clientes)
print(f"Clientes añadidos correctamente: {numero}")


