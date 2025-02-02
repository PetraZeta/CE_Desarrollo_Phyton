def run(a: int, b: int) -> int:
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i
    return gcd_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
