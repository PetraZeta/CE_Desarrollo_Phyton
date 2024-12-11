# definimos la clase Empleado

class Empleado:
    def __init__(self, id, nombre, departamento, salario):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento
        self.__salario = salario
        
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario
        
    def __eq__(self, value):
        # desde dentro de la clase se puede acceder a los atributos privados
        return self.__salario == value.__salario
    
    def __str__(self):
        return self.nombre + "-" + self.apellido + "-" + str(self.salario)