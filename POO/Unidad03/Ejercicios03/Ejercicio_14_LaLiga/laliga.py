import os
from clases import Partido, ColeccionPartidos

archivo = os.path.join(os.path.dirname(__file__), 'LaLiga2324.csv')

repo = ColeccionPartidos(archivo)

# for partido in repo.partidos:
#     print(partido.__dict__) 
#     print()

# result = repo.csv_partidos_local('Real Madrid')
# if result:
#     print('Fichero creado')
# else:
#     print('Error al crear el fichero')

# result = repo.json_partidos_equipo('Real Madrid')
# if result:
#     print('Fichero creado')
# else:
#     print('Error al crear el fichero')    

result = repo.csv_clasificacion()
if result:
    print('Archivo creado')
else:
    print('Error al crear el archivo')

