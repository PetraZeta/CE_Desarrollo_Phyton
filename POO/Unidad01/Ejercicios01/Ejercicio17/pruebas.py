from clases import *
from datetime import date

# Añadir vehículo. No pueden existir varios vehículos con idéntica matrícula. 
result = ListaVehiculos.anadir_vehiculo(Vehiculo('ABC1010', 'Seat', 'Toledo', 'Blanco', 2020, 120000, 120))
print(result)
result = ListaVehiculos.anadir_vehiculo(Vehiculo('ABC1010', 'Seat', 'Toledo', 'Blanco', 2020, 120000, 120))
print(result)


# Añadir reparación a vehículo. Recibe matrícula y fecha de reparación.
result = ListaVehiculos.nueva_reparacion('ABC1010', date(2024, 10, 10))
print(result)
result = ListaVehiculos.nueva_reparacion('ABC1010', date(2024, 1, 1))
print(result)

# Retornar el número de reparaciones de un vehículo, a partir de su matrícula.
matricula = 'ABC101066666666'
numero_reparaciones = ListaVehiculos.numero_reparciones_vehiculo(matricula)

print(f"Matrícula: {matricula} - Nº reparaciones: {numero_reparaciones}")



# Eliminar un vehículo de la lista conociendo su matrícula.
print(ListaVehiculos.eliminar_vehiculo('ABC1010'))
print(ListaVehiculos.eliminar_vehiculo('ABC1010'))

# Ordenar la lista de vehículos por año de compra.
ListaVehiculos.ordenar_por_anio(rever=False)

# Mostrar todos los vehículos.
ListaVehiculos.mostrar_todos()
