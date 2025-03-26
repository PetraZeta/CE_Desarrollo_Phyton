import os
import django
from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

# Cursos con duració entre x e y horas

cursos = Curso.objects.filter(horas__range=(30, 41))

for curso in cursos:
    print(f'{curso.nombre} {curso.horas} horas')