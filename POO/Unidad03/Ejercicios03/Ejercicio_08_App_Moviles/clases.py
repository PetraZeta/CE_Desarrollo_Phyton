import os, csv
from collections import defaultdict

class TratarCsv:
    
    @staticmethod
    def obtener_csv_por_dispositivo(archivo_csv_entrada, dispositivo):        
        '''
        Obtener un archivo csv filtrando 
        por tipo de dispositivo, 
        columna “Device Model”. Incluir también las cabeceras.
        '''
        archivo_csv_salida = os.path.join(
            os.path.dirname(__file__),
            dispositivo + '.csv'
        )
        
        try:
            # Abrir archivo de salida
            with open(archivo_csv_salida, 'w', encoding='utf8') as salida:
                csv_writer = csv.writer(salida, delimiter=',', lineterminator='\n')

                # Abrir archivo de entrada
                with open(archivo_csv_entrada, 'r', encoding='utf8') as entrada:
                    csv_reader = csv.reader(entrada)
                    cabeceras = next(csv_reader) # coger la primera fila del csv -> cabeceras
                    # escribir las cabeceras en el csv de salida
                    csv_writer.writerow(cabeceras)

                    datos = list(csv_reader)
                    # Escribir contenido en el csv de salida
                    
                    for fila in datos:        
                        if fila[1] == dispositivo:
                            csv_writer.writerow(fila)

        except IOError:
            return False
        else:
            return True

    @staticmethod
    def obtener_dicc_so(archivo_csv_entrada):

        try:
            with open(archivo_csv_entrada, 'r', encoding='utf8') as entrada:
                csv_reader = csv.reader(entrada)
                cabeceras = next(csv_reader)

                datos = list(csv_reader)
                
                dicc = defaultdict(int)
                
                for linea in datos:
                    so = linea[2]
                    dicc[so] += 1
                
            return dicc
        except IOError:
            return -1
    
    @staticmethod
    def obtener_csv_time_gender(archivo_csv_entrada):

        try:
            with open(archivo_csv_entrada, 'r', encoding='utf8') as entrada:
                lector = csv.DictReader(entrada)

                archivo_csv_salida = os.path.join(
                    os.path.dirname(__file__),
                    'Time_Gender.csv'
                )

                with open(archivo_csv_salida, 'w', encoding='utf8') as salida:

                    csv_writer = csv.writer(salida)
                    # Escribir cabeceras
                    csv_writer.writerow(['App Usage Time' , 'Gender'])
                    
                    for linea in lector:
                        # Escribir datos                    
                        csv_writer.writerow([
                            linea['App Usage Time (min/day)'], 
                            linea['Gender']
                        ])
                        
        except IOError:
            return False
        else:
            return True