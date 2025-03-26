import os
import django, django.utils.timezone as timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso



cursos = Curso.presenciales.all().count()
total = Curso.objects.all().count()
    
print(f'Total de cursos presenciales: {cursos}')
print(f'Total de cursos: {total}')