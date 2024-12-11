from abc import ABC, abstractmethod

class IGestionNumeros(ABC):

    @abstractmethod
    def nuevo_numero(self, numero):
        pass

    @abstractmethod
    def buscar_numero(self, numero):
        pass

    @abstractmethod
    def ordenar(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass

class ListaNumeros(IGestionNumeros):

    def __init__(self, lista):
        if type(lista) is not list:
            raise ValueError("El argumento debe ser una lista")
        self.lista = lista

    def nuevo_numero(self, numero):
        self.lista.append(numero)

    def buscar_numero(self, numero):
        return numero in self.lista
    
    def ordenar(self):
        self.lista.sort()

    def mostrar(self):
        print(*self.lista, sep=" ")

class TuplaNumeros(IGestionNumeros):

    def __init__(self, tupla):
        if type(tupla) is not tuple:
            raise ValueError("El argumento debe ser una tupla")
        self.tupla = tupla

    def nuevo_numero(self, numero):
        lista = list(self.tupla)
        lista.append(numero)
        self.tupla = tuple(lista)

    def buscar_numero(self, numero):
        return numero in self.tupla
    
    def ordenar(self):
        self.tupla = tuple(sorted(self.tupla))

    def mostrar(self):
        print(*self.tupla, sep=" ")


##################################################
if __name__ == "__main__":
    t = (1, 2, 3, 4, -5)
    tupla = TuplaNumeros(t)
    tupla.nuevo_numero(54)
    print(tupla.buscar_numero(54))
    tupla.ordenar()
    tupla.mostrar()


