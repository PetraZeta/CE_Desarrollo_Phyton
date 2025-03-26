import csv

class CsvClientes:
    
    def __init__(self, archivo):
        self.archivo = archivo
        
    def leer_csv(self):
        try:
            with open(self.archivo, 'r', encoding='utf8') as archivo_csv:
                csv_reader = csv.reader(archivo_csv)
                next(csv_reader)
                lista = list(csv_reader)
            return lista
        except Exception as e:
            print(e)
            return False