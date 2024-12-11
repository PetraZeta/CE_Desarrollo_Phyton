# importación de la clase Vehiculo del módulo clases
from clases import Vehiculo

# creación de dos objetos de la clase Vehiculo	
v1 = Vehiculo("Toyota", "Corolla", 2015, 10000)
v2 = Vehiculo("Seat", "Ibiza", 2018, 8000)

# probando el método nombre_completo
print(v1.nombre_completo())
print(v2.nombre_completo())
