import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Listar todos los empleados del departamento de Ventas con salario mayor a 2000
empleados = Empleado.objects.all().filter(departamento="Ventas") & \
    Empleado.objects.all().filter(salario__gt=2000)
print("Listar todos los empleados de Ventas con salario mayor a 2000")
for empleado in empleados:
    print(empleado)