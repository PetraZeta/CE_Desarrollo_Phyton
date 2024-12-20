import json, os

archivo_json = os.path.join(os.path.dirname(__file__), 'people.json')

try:
    with open(archivo_json, 'r', encoding='utf8') as json_file:
        dicc = json.load(json_file)
        
        
        for key in dicc.keys():
            valores = dicc.get('people')
            for diccionario in valores:   # para cada dicc en lista
                print(f'Nombre: {diccionario['firstName']} {diccionario['lastName']}')
                print(f'Edad: {diccionario['age']}')
                print(f'Género: {diccionario['gender']}')
                print()
except IOError as e:
    print(f'{e}')
else:
    print('Proceso finalizado.')
