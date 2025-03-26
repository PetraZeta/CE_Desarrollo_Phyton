import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejercicio10_GestionTareas.settings')
django.setup()

from tareas.models import Tarea

tareas = [
    Tarea(titulo="Comprar pan", descripcion="Ir a la panadería y comprar pan", fecha_creacion="2024-10-10 10:00:00", fecha_vencimiento="2024-11-10 12:00:00", completada=False),
    Tarea(titulo="Estudiar Python", descripcion="Estudiar Python durante 1 hora", fecha_creacion="2025-10-10 10:00:00", fecha_vencimiento="2025-11-10 12:00:00", completada=False),
    Tarea(titulo="Hacer ejercicio", descripcion="Hacer ejercicio durante 30 minutos", fecha_creacion="2026-10-10 10:00:00", fecha_vencimiento="2026-11-10 12:00:00", completada=False),
    Tarea(titulo="Llamar a Juan", descripcion="Llamar a Juan para quedar", fecha_creacion="2027-10-10 10:00:00", fecha_vencimiento="2027-11-10 12:00:00", completada=False),
    Tarea(titulo="Enviar email", descripcion="Enviar email a Juan", fecha_creacion="2028-10-10 10:00:00", fecha_vencimiento="2028-11-10 12:00:00", completada=False),
    Tarea(titulo="Comprar regalo", descripcion="Comprar regalo para el cumpleaños de Juan", fecha_creacion="2024-10-10 10:00:00", fecha_vencimiento="2024-11-10 12:00:00", completada=False),
    Tarea(titulo="Hacer la compra", descripcion="Hacer la compra semanal", fecha_creacion="2025-10-10 10:00:00", fecha_vencimiento="2025-11-10 12:00:00", completada=False),
    Tarea(titulo="Estudiar inglés", descripcion="Estudiar inglés durante 1 hora", fecha_creacion="2026-10-10 10:00:00", fecha_vencimiento="2026-11-10 12:00:00", completada=False),
    Tarea(titulo="Estudiar Python", descripcion="Estudiar Python durante 1 hora", fecha_creacion="2025-10-10 10:00:00", fecha_vencimiento="2025-11-10 12:00:00", completada=False),
    Tarea(titulo="Hacer ejercicio", descripcion="Hacer ejercicio durante 30 minutos", fecha_creacion="2025-10-11 10:00:00", fecha_vencimiento="2025-11-11 12:00:00", completada=False),
    Tarea(titulo="Llamar a Juan", descripcion="Llamar a Juan para quedar", fecha_creacion="2025-10-12 10:00:00", fecha_vencimiento="2025-11-12 12:00:00", completada=False),
    Tarea(titulo="Enviar email", descripcion="Enviar email a Juan", fecha_creacion="2025-10-13 10:00:00", fecha_vencimiento="2025-11-13 12:00:00", completada=False),
    Tarea(titulo="Comprar regalo", descripcion="Comprar regalo para el cumpleaños de Juan", fecha_creacion="2024-10-10 10:00:00", fecha_vencimiento="2024-11-10 12:00:00", completada=False),
    Tarea(titulo="Hacer la compra", descripcion="Hacer la compra semanal", fecha_creacion="2025-10-10 10:00:00", fecha_vencimiento="2025-11-10 12:00:00", completada=False),
    Tarea(titulo="Estudiar inglés", descripcion="Estudiar inglés durante 1 hora", fecha_creacion="2026-10-10 10:00:00", fecha_vencimiento="2026-11-10 12:00:00", completada=False),
]  
    
    
for tarea in tareas:
    tarea.save()
    print(f"Tarea {tarea.titulo} guardada correctamente")