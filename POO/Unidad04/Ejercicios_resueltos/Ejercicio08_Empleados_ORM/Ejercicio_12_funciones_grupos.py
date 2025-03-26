import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from django.db.models import Avg, Count, Max, Min, Sum
from empleados.models import Empleado

# Obtener el maximo salario
max_salario = Empleado.objects.all().aggregate(max_salario = Max('salario'))

# Obtener el minimo salario
min_salario = Empleado.objects.all().aggregate(min_salario = Min('salario'))

# Obtener el salario promedio
avg_salario = Empleado.objects.all().aggregate(avg_salario = Avg('salario'))

# Contar los empleados del departamento de Ventas
count_ventas = Empleado.objects.filter(departamento='Ventas').aggregate(count_ventas = Count('nombre'))

print(f"El salario máximo es: {max_salario['max_salario']}")
print(f"El salario mínimo es: {min_salario['min_salario']}")
print(f"El salario promedio es: {avg_salario['avg_salario']}")
print(f"El número de empleados en el departamento de Ventas es: {count_ventas['count_ventas']}")
