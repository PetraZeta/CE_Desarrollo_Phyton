def run(limit: int) -> None:
    suma = 0
    multiplos = ""
    for i in range(0, limit, 3):
        multiplos += str(i) + " "
        suma += i
        if suma >= limit:
            break    
    print(multiplos)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
