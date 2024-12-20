from clases import *
from datetime import date

# Agregación. Clientes y vehículos se crean
# fuera de VehiculoAlquilado.

cliente1 = Cliente(1, 'Gema', 'López', 'gema@gmail.com')
cliente2 = Cliente(2, 'Luis', 'Salas', 'luis@gmail.com')
vehiculo1 = Vehiculo('abc123', 'Seat', 'Ibiza', 120, 30)
vehiculo2 = Vehiculo('xyz123', 'Seat', 'León', 140, 60)

alquilado1 = VehiculoAlquilado(cliente1, vehiculo1, date(2024, 10,10), 10)
print(alquilado1.importe_alquiler())
del alquilado1

alquilado2 = VehiculoAlquilado(cliente2, vehiculo2, date(2024, 10,10), 10)
print(alquilado2.importe_alquiler())

