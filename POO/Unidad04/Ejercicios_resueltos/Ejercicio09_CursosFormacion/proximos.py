import os
import django
from django.utils import timezone
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table,TableStyle,colors

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio09_CursosFormacion.settings')
django.setup()

from cursos.models import Curso

cursos = Curso.objects.filter(fecha_inicio__gte=timezone.now()).order_by('fecha_inicio')
for curso in cursos:
    print(f'{curso.nombre} - {curso.fecha_inicio} - {curso.fecha_fin}')