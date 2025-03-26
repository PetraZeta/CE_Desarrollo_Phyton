import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio10_GestionTareas.settings')
django.setup()

from tareas.models import Tarea
from django.db.models import Count
# Contar tareas por año...

cuenta = Tarea.objects.values_list('fecha_creacion__year').annotate(total_tareas=Count('id'))

for pareja in cuenta:
    print(f"Año: {pareja[0]} - Tareas: {pareja[1]}")