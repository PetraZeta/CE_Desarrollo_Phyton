# programa que pida el número de un mes del año (1-12)
# e imprima la estación del año aproximada a la que pertenece.
# Se debe utilizar la sentencia “match-case” y patrones de comparación
# los cambios de estacion son en marzo, junio, septiembre y diciembre

def run(month: int) -> str:
    match month:
        case 12 | 1 | 2:
            print("La estación aproximada es Invierno")
        case 3 | 4 | 5:
            print("La estación aproximada es Primavera")
        case 6 | 7 | 8:
            print("La estación aproximada es Verano")
        case 9 | 10 | 11:
            print("La estación aproximada es Otoño")
        case _:
            print("Escriba un mes del año válido. Numero entre 1 y 12")
        

# Probar la función
mes = int(input("Introduce el mes del año: "))
run(mes)
