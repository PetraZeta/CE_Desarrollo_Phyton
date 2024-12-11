import random 

class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __eq__(self, otra):
        return self.nombre == otra.nombre and \
            self.correo == otra.correo
    
    def __str__(self):
        return f"{self.nombre}"
    

class AmigoInvisible:
    def __init__(self, descripcion, fecha):
        self.descripcion = descripcion
        self.fecha = fecha
        self.participantes = []

    def anadir_persona(self, nombre, correo):
        nuevo_participante = Persona(nombre, correo)  # delegación
        if nuevo_participante not in self.participantes:
            self.participantes.append(nuevo_participante)
            return True
        return False




    def sortear(self):
        # barajar la lista
        random.shuffle(self.participantes)
        numero = len(self.participantes)
        parejas = {}
        for i in range(numero):
            if (i==len(self.participantes)-1):  # estoy en el último elem.
                uno = self.participantes[i].nombre
                otro = self.participantes[0].nombre                
            else:
                uno = self.participantes[i].nombre
                otro = self.participantes[i+1].nombre                
            parejas[uno] = otro    
        return parejas