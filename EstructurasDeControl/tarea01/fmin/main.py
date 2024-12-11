def run(x1: int, x2: int) -> tuple:
    valores = []
    for x in range(x1, x2+1):
        y = x**2-6*x + 3
        valores.append((x, y))
    xmin = valores[0][0]
    fmin = valores[0][1]
    for x, y in valores:
        if y < fmin:
            xmin = x
            fmin = y
    return xmin, fmin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
