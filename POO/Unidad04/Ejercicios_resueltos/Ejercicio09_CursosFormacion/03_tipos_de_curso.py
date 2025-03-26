import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

# tipos de curso
tipos = Curso.objects.values_list('tipo', flat=True).distinct()
print('Tipos de curso')
for tipo in tipos:
    print(tipo)