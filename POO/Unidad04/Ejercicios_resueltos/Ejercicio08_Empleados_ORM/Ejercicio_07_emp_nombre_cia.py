import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Listar todos los empleados con 'cía' en el apellido
empleados = Empleado.objects.filter(apellidos__contains="cía")
print("Listar todos los empleados con cía en el apellido")
for empleado in empleados:
    print(empleado)