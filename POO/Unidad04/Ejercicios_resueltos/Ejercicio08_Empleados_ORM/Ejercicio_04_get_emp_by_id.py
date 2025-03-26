import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Buscar empleado por id
try:
    id = int(input("Introduce el id del empleado: "))
    empleado= Empleado.objects.get(id=id)
    print(empleado)
except:
    print("Empleado no encontrado")