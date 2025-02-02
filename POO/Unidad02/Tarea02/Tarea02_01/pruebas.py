from clases import *
from datetime import date

partido1 = Futbol("R.Madrid", "Benganitas", date(2020, 6, 2), "Liga", 1 , 3)
partido2 = Baloncesto("Estudiantes", "Cacereño", date.today(), "Liga", 91 , 103)
partido3 = Tenis("Rafa Nadal", "Roger Federer" , date(2020, 6, 2), "Roland Garros",
[6, 5, 7, 3, 7], [3, 7, 6, 6, 6])

print(partido1)  
print(partido1.resultado()) 
print(partido1.ganador()) 

print(partido2)  
print(partido2.resultado()) 
print(partido2.ganador()) 

print(partido3) 
print(partido3.resultado()) 
print(partido3.ganador())