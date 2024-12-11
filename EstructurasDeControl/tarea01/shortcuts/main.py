def run(key1: str, key2: str, key3: str) -> str:
    keys = []
    if key1 != "":
        keys.append(key1)
    if key2 != "":
        keys.append(key2)
    if key3 != "":
        keys.append(key3)
    action = "+".join(keys)

    if action == "CTRL+ALT+T":
        return "Open terminal"
    elif action == "CTRL+ALT+L":
        return "Lock screen"
    elif action == "CTRL+ALT+D":
        return "Show desktop"
    elif action == "ALT+F2":
        return "Run console"
    elif action == "CTRL+Q":
        return "Close window"
    elif action == "CTRL+ALT+DEL":
        return "Log out"
    else:
        return "Undefined"
    return action


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
