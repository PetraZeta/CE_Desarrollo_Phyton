def run(feeling: str) -> str:
    feeling = feeling.lower()
    if feeling == 'happy':
        emoji = chr(0x1F600)
    elif feeling == 'sad':
        emoji = chr(0x1F614)
    elif feeling == 'angry':
        emoji = chr(0x1F621)
    elif feeling == 'pensive':
        emoji = chr(0x1F914)
    elif feeling == 'surprised':
        emoji = chr(0x1F62E)
    else:
        emoji = None
    return emoji


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
