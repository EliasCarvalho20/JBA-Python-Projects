from typing import Union


class TicTacToe:
    def __init__(self, winner: Union[str, None]) -> None:
        self.board = [" " for _ in range(9)]  # list that represents 3x3 board
        self.current_winner = winner  # stores the current winner

    def print_board(self) -> None:
        # it just print the board
        print("---------")
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " ".join(row) + " |")
        print("---------")

    def make_move(self, square: int, letter: str) -> bool:
        # return True if it's a valid move, False otherwise
        if self.board[square].isspace():
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True

        return False

    def winner(self, square: int, letter: str) -> bool:
        # check row
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all(spot == letter for spot in row):
            return True

        # check column
        column_index = square % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False

    def available_moves(self) -> list:
        return [i for i, spot in enumerate(self.board) if spot.isspace()]

    def empty_square(self) -> bool:
        return " " in self.board

    def num_empty_squares(self) -> int:
        return self.board.count(" ")
