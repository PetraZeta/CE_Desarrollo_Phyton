def run(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result = result * i**2
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
