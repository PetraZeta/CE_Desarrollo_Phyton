import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio06_Empleados_ORM.settings')
django.setup()

from empleados.models import Empleado

# Añadir varios empleados

try:
            
    empleados = [
        Empleado(nombre="Luis", apellidos="García", salario=2000, departamento="Ventas"),
        Empleado(nombre="Carmen", apellidos="López", salario=2500, departamento="Ventas"),
        Empleado(nombre="Pedro", apellidos="Martínez", salario=1800, departamento="Ventas"),
        Empleado(nombre="María", apellidos="González", salario=2100, departamento="Informática"),
        Empleado(nombre="Luis", apellidos="Gómez", salario=1900, departamento="Informática"),
        Empleado(nombre="Carmen", apellidos="Sánchez", salario=2200, departamento="RRHH"),
        Empleado(nombre="Pedro", apellidos="Fernández", salario=2300, departamento="RRHH"),
        Empleado(nombre="María", apellidos="García", salario=2400, departamento="I+D"),
        Empleado(nombre="Luis", apellidos="López", salario=2600, departamento="I+D"),
    ]
    for empleado in empleados:
        empleado.save()
        
except Exception as e:
    print("Error:", e)
