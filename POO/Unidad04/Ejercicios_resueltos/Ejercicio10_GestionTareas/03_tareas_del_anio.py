import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio10_GestionTareas.settings')
django.setup()

from tareas.models import Tarea

# Tareas del año...
anio = 2025
tareas = Tarea.objects.filter(fecha_creacion__year=anio)
print(f"Tareas del año {anio}")
for tarea in tareas:
    print(f"Tarea {tarea.titulo}, creada {tarea.fecha_creacion},\
        fecha límite {tarea.fecha_vencimiento}")