# calcule el IMC de una persona y clasifique el resultado.
# La altura y el peso serán de tipo float, el IMC = peso/altura
# MASA CORPORAL CLASIFICACIÓN <16.00 Infrapeso: Delgadez Severa
# 16.00 - 16.99 Infrapeso: Delgadez moderada
# 17.00 - 18.49 Infrapeso: Delgadez aceptable
# 18.50 - 24.99 Peso Normal
# 25.00 - 29.99 Sobrepeso
# 30.00 - 34.99 Obeso: Tipo I
# 35.00 - 40.00 Obeso: Tipo II
# >40.00 Obeso: Tipo III

def run(peso: float, altura: float) -> str:
    imc = peso / (altura * altura)
    print(imc)
    if imc < 16:
        result = "Infrapeso: Delgadez Severa"
    elif imc >= 16 and imc < 17:
        result = "Infrapeso: Delgadez moderada"
    elif imc >= 17 and imc < 18.5:
        result = "Infrapeso: Delgadez aceptable"
    elif imc >= 18.5 and imc < 25:
        result = "Peso Normal"
    elif imc >= 25 and imc < 30:
        result = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        result = "Obeso: Tipo I"
    elif imc >= 35 and imc < 40:
        result = "Obeso: Tipo II"
    elif imc >= 40:
        result = "Obeso: Tipo III"
    else:
        result = "No se encuentra el IMC"
    return result


# Probar la función
peso = float(input("Introduce su peso (en kilos): "))
altura = float(input("Introduce su altura (en metros): "))
print(f"Su peso es: {run(peso, altura)}")
