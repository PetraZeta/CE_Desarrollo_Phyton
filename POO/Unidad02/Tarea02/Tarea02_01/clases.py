# Todos los partidos deben tener como atributos los siguientes: 
# nombres de los dos contrincantes, fecha y competición. 
# Además deben desarrollarse métodos para:
# a. Retornar el ganador del partido.
# b. Retornar el resultado.
# c. Retornar una representación del partido con el formato “ X Vs. Y - fecha - competición”.
from abc import ABC, abstractmethod

class Partido(ABC):
    def __init__(self, nombre1, nombre2, fecha, competicion):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.fecha = fecha
        self.competicion = competicion
        
    @abstractmethod
    def ganador(self):
       pass

    @abstractmethod
    def resultado(self):
        pass

    def __eq__(self, otro_partido):
        return self.nombre1 == otro_partido.nombre1 and self.nombre2 == otro_partido.nombre2
    
    def __str__(self):
        return f"{self.nombre1} vs. {self.nombre2} - {self.fecha} - {self.competicion}"

class Futbol(Partido):
    def __init__(self, nombre1, nombre2, fecha, competicion, goles1=0, goles2=0):
        super().__init__(nombre1, nombre2, fecha, competicion)
        if (type(goles1) is not int or goles1 < 0 ) or (type(goles2) is not int and goles2 < 0) :
            raise ValueError("Los goles deben ser enteros y positivos")
        self.goles1 = goles1
        self.goles2 = goles2

    def ganador(self):
        if self.goles1 > self.goles2:
            return f"Ganador:{self.nombre1}"
        elif self.goles1 < self.goles2:
            return f"Ganador:{self.nombre2}"
        else:
            return "Empate"
 
    def resultado(self):
        if self.goles1 > self.goles2:
            return f"{self.nombre1} {self.goles1} - {self.goles2} {self.nombre2}"
        else:
            return f"{self.nombre2} {self.goles2} - {self.goles1} {self.nombre1}"            
    
class Baloncesto(Partido):
    def __init__(self, nombre1, nombre2, fecha, competicion, puntos1=0, puntos2=0):
        super().__init__(nombre1, nombre2, fecha, competicion)
        self.puntos1 = puntos1
        self.puntos2 = puntos2

        if self.puntos1 == self.puntos2:
            raise ValueError("Los puntos no pueden ser iguales")

    def ganador(self):
        if self.puntos1 > self.puntos2:
            return f"Ganador:{self.nombre1}"
        else:
            return f"Ganador:{self.nombre2}"
            
    def resultado(self):
        if self.puntos1 > self.puntos2:
            return f"{self.puntos1} {self.nombre1} - {self.nombre2} {self.puntos2}"
        else:
            return f"{self.puntos2} {self.nombre2} - {self.nombre1} {self.puntos1}"  


class Tenis(Partido):
    def __init__(self, nombre1, nombre2, fecha, competicion, puntos1, puntos2):
        super().__init__(nombre1, nombre2, fecha, competicion)
        if type(puntos1) is not list or type(puntos2) is not list:
            raise ValueError("Los puntos deben ser listas")
        if len(puntos1) != len(puntos2):
            raise ValueError("Los puntos deben tener la misma cantidad")
        if len(puntos1) not in [3, 5] or len(puntos2) not in [3, 5]:
            raise ValueError("Los sets deben ser 3 o 5")
        self.puntos1 = puntos1
        self.puntos2 = puntos2

    def ganador(self):
        sets_ganados1= 0
        sets_ganados2 = 0
        for i in range(len(self.puntos1)):
            if self.puntos1[i] > self.puntos2[i]:
                sets_ganados1 += 1
            else:
                sets_ganados2 += 1
        if sets_ganados1 > sets_ganados2:
            return f"Ganador:{self.nombre1}"
        else:
            return f"Ganador:{self.nombre2}"

    def resultado(self):
        return f"{self.nombre1} : {self.puntos1}  \n{self.nombre2} : {self.puntos2}"

 