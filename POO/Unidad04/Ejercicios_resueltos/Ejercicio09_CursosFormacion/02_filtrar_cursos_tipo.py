import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

#cursos x tipo
tipo_buscado = 'Presencial'
cursos = Curso.objects.filter(tipo=tipo_buscado)
print('Cursos de tipo', tipo_buscado)
for curso in cursos:
    print(curso.nombre, curso.descripcion, curso.horas, curso.tipo, curso.fecha_inicio, curso.fecha_fin, curso.precio)