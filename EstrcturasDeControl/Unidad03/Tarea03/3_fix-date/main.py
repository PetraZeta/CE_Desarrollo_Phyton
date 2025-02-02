def run(input_date: str, base_year: int) -> str:
    date = input_date.split("/")
    date[0] = date[0].zfill(2)
    date[1] = date[1].zfill(2)
    date[2] = str(int(date[2]) + base_year).zfill(4)
    output_date = "-".join([date[1], date[0], date[2]])
    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
