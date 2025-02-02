def run(text1: str, text2: str) -> str:
    cartesian = ""
    for char in text1:
        for char2 in text2:
            cartesian += char + char2
    return cartesian


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
