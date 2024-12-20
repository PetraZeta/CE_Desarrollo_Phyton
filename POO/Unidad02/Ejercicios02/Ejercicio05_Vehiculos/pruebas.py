from clases import *

gestion = GestionVehiculos()
gestion.add_vehiculo(Turismo('1234AVC', 'Seat', 'Ibiza', 5000, 3, 'diesel'))
gestion.add_vehiculo(Turismo('5678BVC', 'Renault', 'Clio', 4000, 5, 'gasolina'))
gestion.add_vehiculo(Turismo('9876CDE', 'Citroen', 'C4', 6000, 5, 'diesel'))
gestion.add_vehiculo(Turismo('5432FGH', 'Ford', 'Focus', 7000, 5, 'gasolina'))
gestion.add_vehiculo(Autobus('1234JKL', 'Mercedes', 'Sprinter', 20000, 50)) 
gestion.add_vehiculo(Autobus('5678MNO', 'Iveco', 'Daily', 30000, 70))
gestion.add_vehiculo(Furgoneta('9876PQR', 'Peugeot', 'Partner', 10000, 1000))
gestion.add_vehiculo(Furgoneta('5432STU', 'Citroen', 'Berlingo', 12000, 1200))

# Buscar vehículo por matrícula
v = gestion.buscar_vehiculo_matricula('1234AVC')
print(v)

# Modificar carga de una furgoneta
result = gestion.modifica_carga_furgoneta('5678MNO', 1500)
print(result)
v = gestion.buscar_vehiculo_matricula('9876PQR')
print(v)

# Mostrar todos los vehículos
gestion.mostrar_vehiculos() 

# Listado de marcas
marcas = gestion.listado_marcas()
print(marcas)

# Vehículos por tipo
t = gestion.vehiculos_por_tipo('Turismo')
print(type(t))
print(*t, sep='\n')