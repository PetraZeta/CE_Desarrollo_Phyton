from django.db import models
from django.utils import timezone

class Curso(models.Model):
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horas = models.IntegerField()
    tipo = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'cursos'
        


    