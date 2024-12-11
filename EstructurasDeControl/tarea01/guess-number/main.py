def run(target_number: int) -> None:
    intentos = 0
    while True:
        user_input = input("Introduzca número:")
        numero = int(user_input)
        intentos += 1
        if numero == target_number:
            print(f"Enhorabuena has encontrado el número en {intentos} intentos\n")
            break
        elif numero < target_number:
            print("Mayor")
        else:
            print("Menor")
    

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
