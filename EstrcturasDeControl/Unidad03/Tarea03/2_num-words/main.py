def run(text: str) -> int:
    text = text.split()
    num_words = text.__len__()
    return num_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
