def run(precio: float) -> float:
    if precio < 100:
        descuento = precio * 0.05
    elif precio <= 500:
        descuento = precio * 0.1
    else:
        descuento = precio * 0.15
    return precio - descuento


# Probar la función
precio = float(input("Introduce el precio: "))
print(f"El precio con descuento es: {run(precio)}")
