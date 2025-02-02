def run():
    for i in range(0, 7):
        for j in range(i, 7):
            print(f"{i}|{j}", end=" ")
        print()


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
