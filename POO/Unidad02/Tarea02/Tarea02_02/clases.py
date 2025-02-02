class Cadena:
    def __init__(self, cadena):
        self.cadena = cadena
    def __str__(self):
        return self.cadena

    # a. sumar cadenas
    def __add__(self, otra_cadena):
        if type(otra_cadena) is not Cadena:
            raise ValueError("Solo se puede sumar cadenas")
        return (self.cadena + otra_cadena.cadena)

    # b. restar, a la primera cadena, las vocales de la segunda cadena por cadena vacia
    def __sub__(self, otra_cadena):
        if type(otra_cadena) is not Cadena:
            raise ValueError("Solo se puede restar cadenas")
        vocales = "aeiouAEIOU"
        vocales_eliminar = []
        # identificar las vocales en segunda cadena
        for char in otra_cadena.cadena:
            if char in vocales and char not in vocales_eliminar:
                vocales_eliminar.append(char)
        # reemplazar las vocales en la primera cadena
        nueva_cadena = self.cadena
        for vocal in vocales_eliminar:
            nueva_cadena = nueva_cadena.replace(vocal, "")

        self.cadena = nueva_cadena
        
        return Cadena(nueva_cadena)
    # c. longitud de vocales de cadena
    def __len__(self):
        vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
        vocales1 = 0
        for char in self.cadena:
            if char in vocales:
                vocales1 += 1
        return vocales1

    # d. comparar cadenas. si tienen el mismo numero de vocales, retornar True
    def __eq__(self, otra_cadena):
        if type(otra_cadena) is not Cadena:
            raise ValueError("Solo se puede comparar cadenas")

        vocales1 = len(self)
        vocales2 = len(otra_cadena)
        if vocales1 != vocales2:
            return False
        else:
            return True
            
    # e. Operador +=
    def __iadd__(self, otra_cadena):
        nueva_cadena = Cadena(otra_cadena)
        self.cadena += nueva_cadena.cadena
        return self
    
  