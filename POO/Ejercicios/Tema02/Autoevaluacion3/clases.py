# clase Trayecto

class Trayecto:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
    
    def __str__(self):
        return f'{self.origen} - {self.destino} - {self.distancia} km'
    
    def __add__(self, otro):
        return self.distancia + otro.distancia
    
    def __sub__(self, otro):
        return self.distancia - otro.distancia
    
    def __gt__(self, otro):
        return self.distancia > otro.distancia
    
    