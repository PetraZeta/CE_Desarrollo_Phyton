import os
import django
from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

# contar cursos por tipo
cuenta = Curso.objects.values_list('tipo').annotate(Count('tipo'))
for tipo, cantidad in cuenta:
    print(f'{tipo}: {cantidad} cursos')
