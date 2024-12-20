from abc import ABC, abstractmethod

class Vehiculo(ABC):

    def __init__(self, matricula, marca, modelo, precio):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __eq__(self, otro_vehiculo):
        return self.matricula == otro_vehiculo.matricula
    
    def incrementar_precio(self, incremento):
        self.precio += incremento

    @abstractmethod
    def __str__(self):
        pass


class Turismo(Vehiculo):
    def __init__(self, matricula, marca, modelo, precio, puertas, tipo_combustible):
        super().__init__(matricula, marca, modelo, precio)
        self.puertas = puertas
        self.tipo_combustible = tipo_combustible

    def __str__(self):
        return f"Turismo: {self.matricula} - Combustible: {self.tipo_combustible}"
        

class Furgoneta(Vehiculo):
    def __init__(self, matricula, marca, modelo, precio, carga):
        super().__init__(matricula, marca, modelo, precio)
        self.carga = carga

    def __str__(self):
        return f"Furgoneta: {self.matricula}  - Carga: {self.carga}"


class Autobus(Vehiculo):
    def __init__(self, matricula, marca, modelo, precio, asientos):
        super().__init__(matricula, marca, modelo, precio)
        self.asientos = asientos

    def __str__(self):
        return f"Autobus: {self.matricula}  - Asientos: {self.asientos}"


class GestionVehiculos:
    def __init__(self):
        self.vehiculos = {}  # dict

    def add_vehiculo(self, vehiculo):
        if vehiculo.matricula not in self.vehiculos:
            self.vehiculos[vehiculo.matricula] = vehiculo
            return True
        return False

    def buscar_vehiculo_matricula(self, matricula):
        return self.vehiculos.get(matricula, None)

    def modifica_carga_furgoneta(self, matricula, nueva_carga):
        vehiculo = self.buscar_vehiculo_matricula(matricula)
        if vehiculo and isinstance(vehiculo, Furgoneta):
            vehiculo.carga = nueva_carga
            return True
        return False

    def mostrar_vehiculos(self):
        for k, v in self.vehiculos.items():
            print(f"Matricula: {k} - {v}")  # polimorfismo

    def listado_marcas(self):
        return list(set([v.marca for v in self.vehiculos.values()]))
                   
    def vehiculos_por_tipo(self, tipo):
        return tuple(
            v
            for v in self.vehiculos.values()
            if (tipo.lower() == type(v).__name__.lower())
        )




