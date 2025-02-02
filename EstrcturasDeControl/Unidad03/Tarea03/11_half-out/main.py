def run(values: set) -> set:
    half_out_values = set()
    for value in values:
        half_value = value // 2
        if half_value not in values:
            half_out_values.add(half_value)
    return half_out_values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
