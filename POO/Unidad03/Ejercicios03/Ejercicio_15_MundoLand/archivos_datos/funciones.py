# Cargar datos de mamíferos
import json
import os


def cargar_mamiferos():
    try:
        archivo = os.path.join(os.path.dirname(__file__), 'mamiferos.json')
        with open(archivo, 'r', encoding='utf8') as file:
            datos_mamiferos = json.load(file)
        return datos_mamiferos
    except:
        return False

def cargar_plantas():
    try:
        archivo = os.path.join(os.path.dirname(__file__), 'plantas.json')
        with open(archivo, 'r', encoding='utf8') as file:
            datos_plantas = json.load(file)        
        return datos_plantas
    except:
        return False
