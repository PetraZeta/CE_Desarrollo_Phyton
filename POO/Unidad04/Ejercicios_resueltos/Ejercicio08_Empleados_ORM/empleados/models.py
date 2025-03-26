from django.db import models

# Create your models here.



class Empleado(models.Model):
    nombre = models.TextField(max_length=50)
    apellidos = models.TextField(max_length=50)
    salario = models.DecimalField(decimal_places=4, max_digits=12)  
    departamento = models.TextField(max_length=50, blank=True, null=True)
    fecha_contratacion = models.DateField(null=True, blank=True, auto_now_add=True)

    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.salario} - {self.departamento}"