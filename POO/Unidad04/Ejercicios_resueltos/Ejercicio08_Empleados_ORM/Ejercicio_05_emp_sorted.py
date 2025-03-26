import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Listar todos los empleados ordenados por apellidos y nombre
empleados = Empleado.objects.all().order_by('apellidos', 'nombre')
print("Listar todos los empleados")
for empleado in empleados:
    print(empleado)