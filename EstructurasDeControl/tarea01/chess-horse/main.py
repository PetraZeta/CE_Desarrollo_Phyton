def run(target_x: int, target_y: int) -> int:
    pos_x = 0
    pos_y = 0
    movements = 0
    while True:
        if pos_x == target_x and pos_y == target_y:
            print(f"Resuelto en {movements} movimientos")
            return movements
        elif pos_x > target_x or pos_y > target_y:
            print("No se puede resolver")
            return -1
        else:
            if target_x - pos_x > target_y - pos_y:
                pos_x = pos_x + 2
                pos_y = pos_y + 1
            else:
                pos_x = pos_x + 1
                pos_y = pos_y + 2
            movements += 1
            

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)
