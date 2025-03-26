import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio10_GestionTareas.settings')
django.setup()

from tareas.models import Tarea

completadas = Tarea.objects.filter(completada=True)

for tarea in completadas:
    print(f"Tarea {tarea.titulo} completada correctamente {tarea.fecha_vencimiento}")