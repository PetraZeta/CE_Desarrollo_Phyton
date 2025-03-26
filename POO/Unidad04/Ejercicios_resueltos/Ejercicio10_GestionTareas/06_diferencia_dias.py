import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio10_GestionTareas.settings')
django.setup()

from tareas.models import Tarea

# Calcular la diferencia de días entre la fecha de creación y la fecha de finalización de las tareas completadas

completadas = Tarea.objects.values_list('titulo', 'fecha_creacion', 'fecha_finalizacion').filter(completada=True)

for tarea in completadas:
    diferencia = tarea[2] - tarea[1]
    print(f"Tarea {tarea[0]} - {tarea[1]} - {tarea[2]} - Diferencia de días: {diferencia.days}")

