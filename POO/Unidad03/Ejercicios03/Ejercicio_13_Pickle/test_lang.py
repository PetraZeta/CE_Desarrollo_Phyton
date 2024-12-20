from clases import *

opciones = [
    '1. Añadir lenguaje',
    '2. Eliminar lenguaje',
    '3. Contar lenguajes',
    '4. Mostrar lenguajes',
    '5. Salir'    
]
menu = Menu(opciones)

repo = RepoLanguage()

while True:
    opcion = menu.show_menu()
    match opcion:
        case '1':
            print('Añadir lenguaje')
            nombre = input('Nombre: ')
            extension = input('Extension: ')
            descripcion = input('Descripcion: ')
            result = repo.add_language(nombre, extension, descripcion)
            if result:
                print('Lenguaje añadido')
            else:
                print('Lenguaje ya existe')
            print()

        case '2':
            print('Eliminar lenguaje')
            nombre = input('Nombre: ')
            result = repo.remove_language(nombre)
            if result:
                print('Lenguaje eliminado')
            else:
                print('Lenguaje no existe')
            print()
        
        case '3':
            print('Contar lenguajes')
            print(f'Hay {repo.count_language()} lenguajes')
            print()

        case '4':
            print('Mostrar lenguajes')
            for lenguaje in repo.show_languages():
                print(lenguaje)
            print()

        case '5':
            print('Fin')
            result = repo.save()
            if result:
                print('Datos guardados')
            else:
                print('Error al guardar datos')
            break        
        case _:
            print('Opcion no valida')
            print()