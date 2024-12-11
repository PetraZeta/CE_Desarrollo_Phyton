def run(value1: int | float, value2: int | float, value3: int | float) -> \
      int | float:
    if value1 < value2 and value1 < value3:
        min_value = value1
    elif value2 < value1 and value2 < value3:
        min_value = value2
    else:
        min_value = value3
    print(min_value)
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
