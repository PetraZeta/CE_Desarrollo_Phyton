# Definición de las clases
# Clase base
class Persona:
    def __init__(self, nombre, apellidos, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        
    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellidos} - Correo: {self.correo}'    

# clase derivada
class Cliente(Persona):
    def __init__(self, nombre, apellidos, correo, num_cliente, numero_cuenta):
        super().__init__(nombre, apellidos, correo)
        self.num_cliente = num_cliente
        self.numero_cuenta = numero_cuenta
        
    def __str__(self):
        return f'{super().__str__()} - {self.num_cliente} - Cuenta: {self.numero_cuenta}'
    
# clase derivada
class Trabajador(Persona):
    def __init__(self, nombre, apellidos, correo, num_trabajador, salario):
        super().__init__(nombre, apellidos, correo)
        self.num_trabajador = num_trabajador
        self.salario = salario
                
    def __str__(self):
        return f'{super().__str__()} - {self.num_trabajador} - Salario: {self.salario}'
     