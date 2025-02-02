from clases import *

# a. sumar objetos cadena
cadena1 = Cadena("Me gusta programar en ")
cadena2 = Cadena("Python")
print(cadena1 + cadena2)

# b. restar objetos cadena
cadena3 = Cadena("El temor de un hombre sabio")
cadena4 = Cadena("tormenta")
print(cadena3 - cadena4)
print(cadena3)

# c. longitud de cadena
cadena5 = Cadena("Leí `La rueda del tiempo`")
print(len(cadena5))

# d. comparar objetos cadena
cadena6 = Cadena("Python")
cadena7 = Cadena("Cobol")
cadena8 = Cadena("Java")

print(cadena6 == cadena7)   
print(cadena7 == cadena8)   

# e. Operador +=
cadena9 = Cadena("Sayonara ")
cadena9 += "baby"
print(cadena9)