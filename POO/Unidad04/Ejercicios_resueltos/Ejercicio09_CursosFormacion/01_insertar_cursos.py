import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

cursos = [
    Curso(nombre='Python', descripcion='Curso de Python', horas=40, fecha_inicio='2021-01-01', fecha_fin='2021-01-31', precio=100.00),
    Curso(nombre='Django', descripcion='Curso de Django', horas=40, fecha_inicio='2021-02-01', fecha_fin='2021-02-28', precio=150.00),
    Curso(nombre='Flask', descripcion='Curso de Flask', horas=40, fecha_inicio='2021-03-01', fecha_fin='2021-03-31', precio=120.00),
    Curso(nombre='JavaScript', descripcion='Curso de JavaScript', horas=40, fecha_inicio='2021-04-01', fecha_fin='2021-04-30', precio=110.00),
    Curso(nombre='HTML5', descripcion='Curso de HTML5', horas=40, fecha_inicio='2025-05-01', fecha_fin='2025-05-31', precio=90.00),
    Curso(nombre='CSS3', descripcion='Curso de CSS3', horas=40, fecha_inicio='2026-06-01', fecha_fin='2026-06-30', precio=80.00),
    Curso(nombre='Bootstrap', descripcion='Curso de Bootstrap', horas=40, fecha_inicio='2021-07-01', fecha_fin='2021-07-31', precio=70.00),
    Curso(nombre='jQuery', descripcion='Curso de jQuery', horas=40, fecha_inicio='2025-08-01', fecha_fin='2025-08-31', precio=60.00),
    Curso(nombre='SQL', descripcion='Curso de SQL', horas=40, fecha_inicio='2024-09-01', fecha_fin='2024-09-30', precio=50.00),
    Curso(nombre='PostgreSQL', descripcion='Curso de PostgreSQL', horas=40, fecha_inicio='2025-10-01', fecha_fin='2025-10-31', precio=40.00),
    Curso(nombre='MySQL', descripcion='Curso de MySQL', horas=40, fecha_inicio='2022-11-01', fecha_fin='2022-11-30', precio=30.00),
    Curso(nombre='SQLite', descripcion='Curso de SQLite', horas=40, fecha_inicio='2021-12-01', fecha_fin='2021-12-31', precio=20.00),
]

for curso in cursos:
    curso.save()
    print(f'Curso insertado: {curso.nombre}')