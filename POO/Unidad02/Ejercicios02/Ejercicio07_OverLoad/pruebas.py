from clases import *
from datetime import date

# Pruebas

pedido1 = Pedido(1, date.today(), 'Carlos')
pedido2 = Pedido(2, date.today(), 'Ana')

pedido1 + 'aguacates'

pedido1 + 'plátanos'
pedido1 - 'peras'

print(pedido1)
print(pedido2)

pedido1 += pedido2

print(pedido1)

print(bool(pedido1))