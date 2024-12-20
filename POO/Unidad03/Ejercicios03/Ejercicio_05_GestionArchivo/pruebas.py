import os
from clases import GestionArchivo

ruta_absoluta = os.path.abspath(__file__)
directorio = os.path.dirname(ruta_absoluta)
archivo = os.path.join(directorio, 'operaciones.txt')

# Método 1. Cadena está en archivo
cadena_buscada = 'update'
result = GestionArchivo.buscar_cadena(cadena_buscada, archivo)
if result == -1:
    print(f'Se ha producido algún error con el archivo')
elif result:  #True
    print(f'Cadena {cadena_buscada} encontrada en el archivo {os.path.basename(archivo)}.')
else:
    print(f'Cadena {cadena_buscada} no encontrada en el archivo {os.path.basename(archivo)}.')



# Método 2. Contar repeticiones.
cadena_buscada = 'delete'
result = GestionArchivo.contar_repeticiones(cadena_buscada, archivo)
if result == -1:
    print(f'Se ha producido algún error con el archivo')
else: 
    print(f'La cadena {cadena_buscada} aparece {result} veces en el archivo {os.path.basename(archivo)}.')



# Método 3. Líneas donde aparece la cadena
cadena_buscada = 'update'
result = GestionArchivo.donde_aparece(cadena_buscada, archivo)
if result == -1:
    print(f'Se ha producido algún error con el archivo')
elif len(result)>0: 
    print(f'La cadena {cadena_buscada} aparece en el archivo {os.path.basename(archivo)} en...')
    for k,v in result.items():
        print(f'Línea {k}: {v}')
else:
    print(f'La cadena {cadena_buscada} no aparece en el archivo {os.path.basename(archivo)}')    
