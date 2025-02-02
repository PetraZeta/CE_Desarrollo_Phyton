def run(can_fly: bool, is_human: bool, has_mask: bool) -> str:
    if can_fly is True:
        if is_human is True:
            if has_mask is True:
                character = 'Ironman'
            else:
                character = 'Captain Marvel'
        else:
            if has_mask is True:
                character = 'Ronan Accuser'
            else:
                character = 'Vision'
    else:
        if is_human is True:
            if has_mask is True:
                character = 'Spiderman'
            else:
                character = 'Hulk'
        else:
            if has_mask is True:
                character = 'Black Bolt'
            else:
                character = 'Thanos'
    return character


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
