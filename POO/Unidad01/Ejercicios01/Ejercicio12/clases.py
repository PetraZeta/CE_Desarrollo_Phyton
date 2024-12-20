# definición de las clases Partido y GestionPartidos
# Importamos la clase datetime
from datetime import datetime

class Partido:
    def __init__(self, equipo_local, equipo_visitante, goles_local, goles_visitante, campeonato, fecha):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
        self.campeonato = campeonato
        self.fecha = fecha
        
    def __str__(self):
        return f"{self.equipo_local} {self.goles_local} " \
            + f"- {self.goles_visitante} {self.equipo_visitante} " \
            + f"- {self.campeonato} - {self.fecha}"

#############################################################################################


class GestionPartidos:
    # Atributo de clase
    partidos = [Partido("Real Madrid", "Barcelona", 2, 1, "Liga", datetime(2021, 10, 20)),
                Partido("Betis", "Sevilla", 1, 1, "Liga", datetime(2021, 10, 21)),
                Partido("Real Madrid", "Sevilla", 3, 0, "Liga", datetime(2021,10,26)),
                Partido("Betis", "Barcelona", 0, 0, "Liga", datetime(2021,10,27)),
                Partido("Real Madrid", "Betis", 2, 2, "Liga", datetime(2021,10,28)),
                Partido("Sevilla", "Barcelona", 1, 0, "Liga", datetime(2022,10,29))]
                

    @classmethod
    def filtrar_por_equipo_local(cls, equipo_local):
        for partido in cls.partidos:
            if partido.equipo_local.lower() == equipo_local.lower():
                print(partido)


    @classmethod
    def ganados_del_equipo(cls, equipo):
        cuenta_ganados = 0
        for partido in cls.partidos:
            if partido.equipo_local == equipo and partido.goles_local > partido.goles_visitante:
                cuenta_ganados += 1
            elif partido.equipo_visitante == equipo and partido.goles_visitante > partido.goles_local:
                cuenta_ganados += 1
        return cuenta_ganados


    @classmethod
    def partidos_anio(cls, anio):
        for partido in cls.partidos:
            if partido.fecha.year == anio:
                print(partido)
                
    
    @classmethod
    def partidos_fecha(cls, fecha):
        for partido in cls.partidos:
            if partido.fecha == fecha:
                print(partido)
                
    
    @classmethod
    def cuenta_partidos(cls):
        # para conocer el nº de partidos simplemente devolvemos la longitud de la lista de partidos
        return len(cls.partidos)
    
    
    @classmethod
    def anadir_partido(cls, partido):
        cls.partidos.append(partido)

    @classmethod
    def anadir_partido_2(cls, local, visitante, goles_local, goles_visitante, camp, fecha):
        nuevo = Partido(local, visitante, goles_local, goles_visitante, camp, fecha)
        cls.partidos.append(nuevo)