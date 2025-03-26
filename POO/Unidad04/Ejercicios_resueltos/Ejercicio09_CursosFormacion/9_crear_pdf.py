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

try:

    # Ruta absoluta del archivo PDF           
    archivo_pdf = os.path.join(os.path.dirname(__file__), 'cursos_proximos.pdf')   

    # Crear el objeto PDF
    pdf = SimpleDocTemplate(archivo_pdf, pagesize=A4)

    # Crear la lista de datos
    my_data = []
    # Añadimos encabezados
    my_data.append(['Nombre', 'Tipo', 'Precio', 'Horas', 'Fecha inicio', 'Fecha fin'])

    # Cursos próximo
    cursos = Curso.objects.filter(fecha_inicio__gte=timezone.now()).order_by('fecha_inicio')
    for curso in cursos:
        my_data.append([curso.nombre, curso.tipo, curso.precio, curso.horas, curso.fecha_inicio, curso.fecha_fin])
        
    # Establecer el número y ancho de las columnas
    c_width = [3*cm, 4*cm, 2*cm, 2*cm, 3*cm, 3*cm]

    # Crear la tabla con los datos
    t = Table(my_data, rowHeights=0.6*cm, colWidths=c_width)

    # Establecer el estilo de la tabla
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgrey),
        ('FONTSIZE',(0,0),(-1,-1),14)]))

    # Elementos a incluir en el PDF
    elements = []

    # Añadir el título
    c_width = [18*cm]
    t_titulo = Table([['Próximos cursos'], []], rowHeights= 0.9* cm, colWidths=c_width)
    t_titulo.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightblue),
        ('FONTSIZE',(0,0),(-1,-1),15)]))
    elements.append(t_titulo)
                            
    # Añadir la tabla de datos a los elementos
    elements.append(t)
    # Generar el PDF
    pdf.build(elements)         

except django.db.utils.DatabaseError as error:
    print(f'Error de base de datos: {error}')