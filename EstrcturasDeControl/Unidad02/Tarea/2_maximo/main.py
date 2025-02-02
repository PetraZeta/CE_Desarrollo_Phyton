# Dados dos números a y b utiliza la asignación \
# condicional en una única línea para asignar a la \
# variable maximo el mayor de ambos
a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

maximo = a if a >= b else b

print(f"El número mayor es: {maximo}")
