def run(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    isogram = True
    text1 = ""
    for char in text.lower():
        if char in ALPHABET:
            if char in text1:
                isogram = False
        text1 += char
    return isogram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
