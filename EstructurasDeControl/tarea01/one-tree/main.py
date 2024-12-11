def run():
    n = 9
    for i in range(1, n + 1):
        ascendente = ""
        for j in range(1, i + 1):
            ascendente += str(j)
        descendente = ""
        for j in range(i - 1, 0, -1):
            descendente += str(j)
        print(ascendente+descendente)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
