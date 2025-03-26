import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Actaulizar salario de empleado

id_empleado = input("Introduce el id de empleado: ")

try:
    empleado_buscado = Empleado.objects.get(id=id_empleado)
    nuevo_salario = float(input("Introduce el nuevo salario: "))
    empleado_buscado.salario = nuevo_salario
    empleado_buscado.save()
    print("Salario actualizado")
except Exception as e:
    print(f"Empleado no encontado")
