# Clases Vehiculo y ListaVehiculos

class Vehiculo:

    def __init__(self, matricula, marca, modelo, color, anio, kms, potencia):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.kms = kms
        self.potencia = potencia
        self.fechas_reparaciones = []

    def __eq__(self, otro):
        return self.matricula == otro.matricula
    
    def __str__(self):
        return f"{self.matricula} - {self.marca} - {self.modelo} - {self.anio} - {self.fechas_reparaciones}"
    
    def agregar_reparacion(self, fecha):
        self.fechas_reparaciones.append(fecha)


class ListaVehiculos:
    # JKL012
    
    lista_vehiculos = [
            Vehiculo("ABC123", "Toyota", "Corolla", "Rojo", 2019, 20000, 150),
            Vehiculo("DEF456", "Nissan", "Sentra", "Azul", 2018, 18000, 140),
            Vehiculo("GHI789", "Chevrolet", "Spark", "Blanco", 2017, 160400, 130),
            Vehiculo("JKL012", "Mazda", "3", "Negro", 2016, 15000, 120),
            Vehiculo("KKL122", "Volkswagen", "Golf", "Blanco", 2020, 230400, 120),
            Vehiculo("MMG122", "Nissan", "Micra", "Azul", 2020, 123000, 86),
            Vehiculo("ZZE123", "Seat", "Ibiza", "Blanco", 2010, 67000, 120),
        
        ]
    
    # Añadir vehículo. No pueden existir varios vehículos con idéntica matrícula. 
    @classmethod
    def anadir_vehiculo(cls, nuevo_vehiculo):
        if nuevo_vehiculo in cls.lista_vehiculos:
            return False
        else:
            cls.lista_vehiculos.append(nuevo_vehiculo)
            return True

    # Buscar vehiculo x matricula
    @classmethod
    def buscar_por_matricula(cls, matricula):
        for vehiculo in cls.lista_vehiculos:
            if vehiculo.matricula.lower() == matricula.lower():
                return vehiculo
        return None

    # Retornar el número de reparaciones de un vehículo, a partir de su matrícula.
    @classmethod
    def numero_reparciones_vehiculo(cls, matricula):
        """Retorno: nº de reparaciones
            -1 si no existe el vehiculo
        """
        vehiculo = cls.buscar_por_matricula(matricula)
        if vehiculo:
            return len(vehiculo.fechas_reparaciones)
        else:
            return -1  # no existe el vehículo

    # Eliminar un vehículo de la lista conociendo su matrícula.
    @classmethod
    def eliminar_vehiculo(cls, matricula):
        for i in range(len(cls.lista_vehiculos)):    # 0 ---- 5
            if cls.lista_vehiculos[i].matricula == matricula:
                del cls.lista_vehiculos[i]
                return True
        return False

    # Ordenar la lista de vehículos por año de compra.
    @classmethod
    def ordenar_por_anio(cls, rever):
        cls.lista_vehiculos.sort(key= lambda v: v.anio, reverse=rever)


    # Añadir rep. a vehiculo
    @classmethod
    def nueva_reparacion(cls, matricula, fecha_reparacion):
        vehiculo = cls.buscar_por_matricula(matricula)
        if vehiculo:    # encontrado
            vehiculo.agregar_reparacion(fecha_reparacion)            
            return True
        return False   # el vehiculo no existe


    # Mostrar todos los vehículos.
    @classmethod
    def mostrar_todos(cls):
        print(*cls.lista_vehiculos, sep="\n")