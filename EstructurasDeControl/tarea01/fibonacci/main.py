def run(n: int) -> float:
    fibo = 0
    a = 1
    b = 1
    for i in range(n):
        fibo = a
        c = a + b
        a = b
        b = c
    return fibo


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
