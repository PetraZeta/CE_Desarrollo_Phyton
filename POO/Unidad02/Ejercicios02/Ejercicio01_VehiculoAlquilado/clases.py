# Diseñar una aplicación Python que trabaje con objetos de la clase “VehiculoAlguilado”. 
# Cada vehículo alquilado consta de una instancia de “Vehículo”, una instancia de “Cliente”, una fecha de inicio de alquiler 
# y un número de días. 

# Un vehículo tiene una matrícula, marca, modelo, potencia y precio de alquiler.
# De cada cliente se debe guardar un identificador, nombre, apellidos y correo electrónico. 
# Tanto clientes como vehículos tendrán existencia propia. 
# Añade a la clase “VehículoAlquilado” el método “importe_alquiler”. 
# Este método retorna el resultado de multiplicar el precio de alquiler por el número de días de alquiler.

class Cliente:
    def __init__(self, id, nombre, apellidos, correo):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo

class Vehiculo:
    def __init__(self, matricula, marca, modelo, potencia, precio_alquiler):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.precio_alquiler = precio_alquiler

class VehiculoAlquilado:
    def __init__(self, cliente, vehiculo, fecha_alquiler, numero_dias):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha_alquiler = fecha_alquiler
        self.numero_dias = numero_dias

    def importe_alquiler(self):
        return self.numero_dias * self.vehiculo.precio_alquiler

