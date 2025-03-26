import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

# Actualizar precio cursos spresenciales

presenciales = Curso.objects.filter(tipo='Presencial')
# Mostrar antes
print('Antes:')
for curso in presenciales:
    print(f'{curso.nombre}: {curso.precio}')
    
# Actualizar
for curso in presenciales:
    curso.precio += 50
    curso.save()

# Mostrar después
print('Después:')
for curso in presenciales:
    print(f'{curso.nombre}: {curso.precio}')

