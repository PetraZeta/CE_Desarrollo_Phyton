# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Menos de 60: F
def run(calificacion: int) -> int:
    if calificacion <= 100 and calificacion >= 90:
        resultado = 'A'
    elif calificacion <= 89 and calificacion >= 80:
        resultado = 'B'
    elif calificacion <= 79 and calificacion >= 70:
        resultado = 'C'
    elif calificacion <= 69 and calificacion >= 60:
        resultado = 'D'
    else:
        resultado = 'F'
    return resultado


# Probar la función
calificacion_numero = int(input("Introduce la calificación: "))
print(f"La letra que corresponde es: {run(calificacion_numero)}")
