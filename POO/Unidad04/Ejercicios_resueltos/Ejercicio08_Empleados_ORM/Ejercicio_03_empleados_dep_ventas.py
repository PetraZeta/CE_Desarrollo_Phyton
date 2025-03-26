import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
    'Ejercicio06_Empleados_ORM.settings')
django.setup()

from empleados.models import Empleado

# Listar todos los empleados del departamento de ventas
empleados = Empleado.objects.filter(departamento="Ventas")
print("Listar todos los empleados")
for empleado in empleados:
    print(empleado)