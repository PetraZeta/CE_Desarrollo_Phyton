def run(start_code: int, end_code: int) -> None:
    fila = []
    filas = []
    for code in range(start_code, end_code + 1):
        fila.append(f"{str(code).zfill(3)} {chr(code)}")
        if len(fila) == 5:
            print("   ".join(fila))
            fila = []
    if len(fila) > 0:
        filas.append(fila)
    for fila in filas:
        print("\n".join(fila))


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
