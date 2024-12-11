def run(text1: str, text2: str) -> int:
    dhamming = 0
    if len(text1) != len(text2):
        return -1
    else:
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                dhamming += 1     
        return dhamming


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
