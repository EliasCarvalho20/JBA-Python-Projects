def output_board():
    print("---------")
    for n in range(0, len(board), 3):
        print(f"| {' '.join(board[n:n + 3])} |")
    print("---------")


def check_winner():
    return [[board[n] for n in range(0, 9, 3) if board[n] == board[n + 1] == board[n + 2]],
            [board[n] for n in range(0, 3, 1) if board[n] == board[n + 3] == board[n + 6]],
            [board[n] for n in range(4, 0, -2) if board[4 - n] == board[4] == board[4 + n]]]


def check_play():
    winner = check_winner()
    if any(list(map(lambda x: "X" in x, winner))):
        print("X wins")
        return True
    elif any(list(map(lambda x: "O" in x, winner))):
        print("O wins")
        return True


board = [' ' for n in range(0, 9)]
output_board()
plays = 0
while True:
    try:
        row, col = [int(n) for n in input("Enter the coordinates: ").split()]
    except ValueError:
        print("You should enter numbers!")
        continue
    if not (1 <= row <= 3 and 1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = ((3 - col) * 3) + (row - 1)
    if 'X' in board[index] or 'O' in board[index]:
        print("This cell is occupied! Choose another one!")
        continue

    plays += 1
    board[index] = 'O' if plays % 2 == 0 else 'X'
    output_board()

    if check_play():
        break
    elif plays == 9:
        print("Drawn")
        break
