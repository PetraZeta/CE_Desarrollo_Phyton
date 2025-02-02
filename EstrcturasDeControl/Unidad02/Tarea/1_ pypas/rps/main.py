def run(player1: str, player2: str) -> int:
    player1 = player1.lower()
    player2 = player2.lower()

    if player1 == player2:
        winner = 0
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "scissors" and player2 == "paper"):
        winner = 1
    else:
        winner = 2
    return winner


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
