from django.db import models

# Create your models here.

# nombre, categoría, dirección, teléfono, correo electrónico, año de creación y número de habitaciones


class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    year = models.IntegerField()
    num_habitaciones = models.IntegerField()

# El método __str__ debe retornar nombre del hotel, categoría, año de creación y número de habitaciones.
    def __str__(self):
        return f"{self.nombre}, {self.categoria}, {self.year},\
                {self.num_habitaciones}"