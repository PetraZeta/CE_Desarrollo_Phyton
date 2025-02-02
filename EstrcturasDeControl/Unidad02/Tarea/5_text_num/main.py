def run(num: int) -> int:
    match num:
        case 5:
            result = "Cinco"
        case 4:
            result = "Cuatro"
        case 3:
            result = "Tres"
        case 2:
            result = "Dos"
        case 1:
            result = "Uno"
        case _:
            result = None
    return result


# Probar la función
numero = int(input("Introduce un numero del 1 al 5: "))
print(f"Es el número: {run(numero)}")
