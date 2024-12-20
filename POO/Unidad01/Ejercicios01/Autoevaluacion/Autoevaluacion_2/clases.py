# Clase Partido
class Partido:
    contador = 0
    def __init__(self, local, visitante, puntos_local, puntos_visitante):
        self.local = local
        self.visitante = visitante
        self.puntos_local = puntos_local
        self.puntos_visitante = puntos_visitante
        Partido.contador += 1   
    
    def __str__(self):
        return f'{self.local} {self.puntos_local} - {self.puntos_visitante} {self.visitante}'   
    
    @classmethod
    def get_contador(cls):
        return cls.contador