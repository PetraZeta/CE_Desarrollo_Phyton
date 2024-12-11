# Importamos las clases
from clases import Partido, GestionPartidos
from datetime import datetime

# Mostramos los partidos del Real Madrid
print("Partidos del Real Madrid")
GestionPartidos.filtrar_por_equipo_local("Real Madrid")
print()

# Mostramos los partidos ganados por el Real Madrid
numero_partidos_ganados = GestionPartidos.ganados_del_equipo("Real Madrid")
print(f"Ganados por el Real Madrid {numero_partidos_ganados}")
print()

# # Filtrar los partidos por año
year=2022
print(f"Partidos del {year}")
GestionPartidos.partidos_anio(year)
print()

# # Filtrar los partidos por fecha
print("Partidos del 20 de octubre de 2021")
GestionPartidos.partidos_fecha(datetime(2021, 10, 20))
print()

# Mostramos el número de partidos
print(f"Número de partidos: {GestionPartidos.cuenta_partidos()}")
print()

# Añadir un nuevo partido
# Observa como el método recibe un objeto partido como argumento
nuevo_partido = Partido("Betis", "Alavés", 3, 1, "Copa", datetime(2023, 10, 30))
GestionPartidos.anadir_partido(nuevo_partido)

# Añadir partido met. 2
GestionPartidos.anadir_partido_2(local="Zafra", visitante="Medina", goles_local=3, goles_visitante=3, camp="Liga", fecha=datetime(2024, 10, 1))

# Filtrar por año
print("Partidos del 2024")
GestionPartidos.partidos_anio(2024)
