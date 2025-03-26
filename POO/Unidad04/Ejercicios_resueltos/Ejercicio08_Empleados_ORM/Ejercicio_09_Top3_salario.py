import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Listar top 3 salario
empleados = Empleado.objects.all().order_by('-salario')[:3]
print("Empleados Top 3 salario")
for empleado in empleados:
    print(empleado)