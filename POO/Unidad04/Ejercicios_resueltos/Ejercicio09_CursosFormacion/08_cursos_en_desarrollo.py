import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

# Cursos en desarrollo
cursos = Curso.objects.filter(fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now())
print('Cursos en desarrollo:')
for curso in cursos:
    print(curso.nombre, curso.fecha_inicio, curso.fecha_fin)