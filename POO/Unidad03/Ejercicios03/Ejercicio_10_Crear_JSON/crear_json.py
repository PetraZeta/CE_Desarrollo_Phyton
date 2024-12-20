import json, os
from collections import defaultdict

# Crear archivo JSON
archivo_json = os.path.join(os.path.dirname(__file__), 'totales_ventas.json')

ventas = [
    ["tomate", 1000, 1.5],
    ["lechuga", 500, 0.5],
    ["cebolla", 300, 0.75],
    ["tomate", 2000, 1.5],
    ["lechuga", 1000, 0.5],
    ["cebolla", 600, 0.75],
    ["pera", 300, 1.75],
    ["manzana", 500, 1.25],
    ["uva", 1000, 2.5],
    ["uva", 2000, 2.5],
]

totales = defaultdict(float)
for venta in ventas:
    producto, kilos, precio = venta
    totales[producto] += kilos * precio   

# print(totales)
with open(archivo_json, 'w', encoding='utf8') as json_file:
    json.dump(totales, json_file, indent=4)
