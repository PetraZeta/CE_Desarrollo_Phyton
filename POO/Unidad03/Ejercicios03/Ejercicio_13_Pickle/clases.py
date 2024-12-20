import os, pickle


class ProgramingLanguage:
    def __init__(self, nombre, extension, descripcion):
        self.nombre = nombre
        self.extension = extension
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre} ({self.extension}): {self.descripcion}"
    
    def __repr__(self):
        return f"({self.nombre} ({self.extension})"
    
    def __eq__(self, other):
        return self.nombre == other.nombre and self.extension == other.extension

#############################################################    

class RepoLanguage:
    
    def __init__(self):
        self.lista = self.__cargar_datos()        
        
    def __cargar_datos(self):
        archivo = os.path.join(os.path.dirname(__file__), 'lenguajes.pkl')
        try:
            with open(archivo, 'rb') as pkl_file:
                return pickle.load(pkl_file)
        except:
            return []



    def add_language(self, nombre, extension, descripcion):
        lenguaje = ProgramingLanguage(nombre, extension, descripcion)
        if lenguaje not in self.lista:
            self.lista.append(lenguaje)
            return True
        return False
    
    def remove_language(self, nombre):
        for lenguaje in self.lista:
            if lenguaje.nombre == nombre:
                self.lista.remove(lenguaje)
                return True
        return False
    
    def count_language(self):
        return len(self.lista)
    
    def show_languages(self):
        return self.lista
    
    def save(self):
        archivo = os.path.join(os.path.dirname(__file__), 'lenguajes.pkl')
        try:
            with open(archivo, 'wb') as pkl_file:
                pickle.dump(self.lista, pkl_file)
            return True
        except:
            return False
        
class Menu:

    def __init__(self, opciones):
        self.opciones = opciones

    def show_menu(self):
        for opcion in self.opciones:
            print(f'{opcion}')
        print()
        return input('Elige una opción: ')
    