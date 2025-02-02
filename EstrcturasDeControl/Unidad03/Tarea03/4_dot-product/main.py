def run(u: list, v: list) -> float | None:
    dprod = 0
    while len(u) == len(v):
        for i in range(len(u)):
            dprod += u[i]*v[i]
        return dprod
    else:
        return None


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
