def run(key1: str, key2: str, key3: str) -> str:
    keys = []
    if key1 != "":
        keys.append(key1)
    if key2 != "":
        keys.append(key2)
    if key3 != "":
        keys.append(key3)
    action = "+".join(keys)
    match action:
        case "CTRL+ALT+T":
            return "Open terminal"
        case "CTRL+ALT+L":
            return "Lock screen"
        case "CTRL+ALT+D":
            return "Show desktop"
        case "ALT+F2":
            return "Run console"
        case "CTRL+Q":
            return "Close window"
        case "CTRL+ALT+DEL":
            return "Log out"
        case _:
            return "Undefined"
    return action


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
