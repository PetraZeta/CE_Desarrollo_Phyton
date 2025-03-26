import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "Ejercicio06_Empleados_ORM.settings")
django.setup()

from empleados.models import Empleado

# Delete empleado

id_empleado = input("Introduce el id del empleado a eliminar: ")

try:
    empleado_buscado = Empleado.objects.get(id=id_empleado)
    resp = input(f"¿Desea eliminar el empleado {empleado_buscado} (s/n)? ")
    if resp.lower() == 's':
        empleado_buscado.delete()
        print("Empleado eliminado")
except Exception as e:
    print(f"Error al eliminar el empleado")
