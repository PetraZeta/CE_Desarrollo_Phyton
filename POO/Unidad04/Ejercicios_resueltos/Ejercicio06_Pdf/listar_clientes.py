import os
import pymysql
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table,TableStyle,colors


try:
    with pymysql.connect(host='localhost', user='user', password='robocop', \
        port=3309, database='almacen') as conexion:
        
        with conexion.cursor() as cursor:
            sql = 'SELECT numerocliente, concat(apellido, ", ", nombre), telefono, correo FROM clientes '\
                'order by apellido, nombre'
           
            # Ruta absoluta del archivo PDF           
            archivo_pdf = os.path.join(os.path.dirname(__file__), 'listado_clientes.pdf')   
            
            # Crear el objeto PDF
            pdf = SimpleDocTemplate(archivo_pdf, pagesize=A4)
            
            # Crear la lista de datos
            my_data = []
            # Añadimos encabezados
            my_data.append(['Nº', 'Nombre', 'Telefono', 'Correo'])
            
            # Ejecutar la consulta
            numero_clientes=cursor.execute(sql)
            # Añadir los datos del cursor al listado
            for cliente in cursor.fetchall():
                my_data.append(cliente)
            
            # Establecer el número y ancho de las columnas
            c_width = [2*cm, 6*cm, 4*cm, 6*cm]
            
            # Crear la tabla con los datos
            t = Table(my_data, rowHeights=0.6*cm, colWidths=c_width)
            
            # Establecer el estilo de la tabla
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightgrey),
                ('FONTSIZE',(0,0),(-1,-1),14)]))
            
            # Elementos a incluir en el PDF
            elements = []
            
            # Añadir el título
            c_width = [18*cm]
            t_titulo = Table([['Listado de Clientes'], []], rowHeights= 0.9* cm, colWidths=c_width)
            t_titulo.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightblue),
                ('FONTSIZE',(0,0),(-1,-1),15)]))
            elements.append(t_titulo)
                                  
            # Añadir la tabla de datos a los elementos
            elements.append(t)
            # Generar el PDF
            pdf.build(elements)         
           

except  pymysql.MySQLError as error:
    print(f'Error de MySQL: {error}')