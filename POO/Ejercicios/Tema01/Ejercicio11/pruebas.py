# importamos la clase Empleado
from clases import Empleado

# creamos tres objetos de la clase Empleado
emp1 = Empleado(1, "Juan", "Ventas", 2000)
emp2 = Empleado(2, "Ana", "Informática", 2200)
emp3 = Empleado(3, "Elena", "Marketing", 2000)

# cambiar y mostrar salario
emp2.set_salario(2500)
print(emp2.get_salario())

# comparar dos empleados
print(emp1 == emp2)
print(emp1 == emp3)
