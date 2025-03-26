import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

# tipos de curso

no_iniciados = Curso.objects.filter(fecha_inicio__gt=timezone.now())
print('Cursos no iniciados:')
for curso in no_iniciados:
    print(f'{curso.nombre} - {curso.fecha_inicio}')