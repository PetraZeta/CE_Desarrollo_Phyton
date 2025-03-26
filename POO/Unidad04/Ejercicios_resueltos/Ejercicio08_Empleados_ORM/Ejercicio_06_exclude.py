import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Listar todos los empleados que no pertenecen al departamento de ventas
empleados = Empleado.objects.exclude(departamento="Ventas")
print("Listar todos los empleados que no pertenecen al departamento de ventas")
for empleado in empleados:
    print(empleado)