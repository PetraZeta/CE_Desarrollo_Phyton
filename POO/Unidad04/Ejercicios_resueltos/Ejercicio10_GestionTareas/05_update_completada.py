import os
import django
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio10_GestionTareas.settings')
django.setup()

from tareas.models import Tarea

# Actualizar tareas completadas todas las de 2024

completadas = Tarea.objects.filter(completada=True)
for tarea in completadas:
    tarea.fecha_finalizacion = tarea.fecha_vencimiento - timedelta(days=2)
    tarea.save()


