# TIC-TAC-TOE USING MINIMAX

board = [" "] * 9


def display_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def winner(player):
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # Columns
        (0, 4, 8), (2, 4, 6)                 # Diagonals
    ]

    for a, b, c in combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def full():
    return " " not in board


# Minimax
def minimax(computer, human, maximizing):
    if winner(computer):
        return 1

    if winner(human):
        return -1

    if full():
        return 0

    if maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = computer
                score = minimax(computer, human, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = human
                score = minimax(computer, human, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move(computer, human):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = computer

            score = minimax(computer, human, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = computer


# -------- MAIN PROGRAM --------

print("TIC-TAC-TOE")
print("Positions:")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")

human = input("\nChoose X or O: ").upper()

while human not in ["X", "O"]:
    human = input("Please choose X or O: ").upper()

computer = "O" if human == "X" else "X"

# X always starts
turn = "human" if human == "X" else "computer"

while True:
    # HUMAN MOVE
    if turn == "human":
        try:
            position = int(input("\nEnter position (1-9): ")) - 1
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if position < 0 or position > 8:
            print("Invalid position!")
            continue

        if board[position] != " ":
            print("Cell already occupied!")
            continue

        board[position] = human
        display_board()

        if winner(human):
            print("Human Wins!")
            break

        if full():
            print("Game Draw!")
            break

        turn = "computer"

    # COMPUTER MOVE
    else:
        print("\nComputer is thinking...")
        computer_move(computer, human)
        display_board()

        if winner(computer):
            print("Computer Wins!")
            break

        if full():
            print("Game Draw!")
            break

        turn = "human"
