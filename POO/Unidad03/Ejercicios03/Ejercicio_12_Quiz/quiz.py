import os, random
from funciones import *

# Creamos los archivos de preguntas y configuración. rutas absolutas
archivo_json_preguntas = os.path.join(os.path.dirname(__file__), 'questions.json')
archivo_json_config = os.path.join(os.path.dirname(__file__), 'config.json')
archivo_json_top3 = os.path.join(os.path.dirname(__file__), 'top3.json')


preguntas = leer_json_preguntas(archivo_json_preguntas)
dicc_config = leer_json_configuracion(archivo_json_config)

numero_preguntas = dicc_config.get('numero_preguntas', 10)
puntos_por_acierto = dicc_config.get('puntos_por_acierto', 1)

puntos = 0
usuario = input('Introduce tu nombre: ')


for pregunta in random.sample(preguntas, numero_preguntas):

    print(pregunta['question'])
    for letra in 'ABCD':
        print(f'{letra}. {pregunta.get(letra)}')  # pregunta[letra]

    respuesta = input('Introduce respuesta: ')

    if respuesta.upper() == pregunta.get('answer').upper():
        puntos += puntos_por_acierto
        print(f'¡¡¡Correcto, sumas {puntos_por_acierto}. Llevas {puntos} puntos !!!')
    else:
        print(f'No has acertado. Llevas {puntos} puntos.')

print(f'Total puntos: {puntos}')

# retorna si el usuario entre en el top3
es_top3 = check_top3(archivo_json_top3, usuario, puntos)

if es_top3:
    print(f'Felicides {usuario}, has entrado en el top 3.')

dicc_top3 = get_top3(archivo_json_top3)
print(dicc_top3['top3'])





