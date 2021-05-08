import sys
from typing import Union
from random import shuffle, choice
from player import User, Computer


class Game:
    def __init__(self) -> None:
        self.pieces = [[i, j] for i in range(7) for j in range(i, 7)]
        self.user, self.computer = None, None
        self.snake, self.stock = [], []
        self.current_player = "user"
        self.bad_pieces = False

    def start_game(self) -> None:
        self.shuffle_pieces()
        self.slice_pieces()
        self.make_first_move()

        while True:
            self.print_game()

            if self.bad_pieces and self.get_stock_length() != 0:
                self.pass_turn()
            else:
                self.make_move()

    def shuffle_pieces(self) -> None:
        shuffle(self.pieces)

    def slice_pieces(self) -> None:
        self.computer = Computer(self.pieces[-14:][7:])
        self.user = User(self.pieces[:14][7:])
        self.stock = [*self.pieces[:14][:7], *self.pieces[-14:][:7]]

    def make_first_move(self) -> None:
        self.snake.append(choice(self.computer.pieces))
        self.computer.remove_piece(*self.snake)

    def print_game(self) -> None:
        print("=" * 70)
        print(f"Stock size: {self.get_stock_length()}")
        print(f"Computer pieces: {self.computer.get_pieces_length()}\n")

        self.print_snake_pieces()

        print(f"\nYour pieces: ")
        self.user.print_pieces()

        self.check_winner()
        self.check_tie()

        if "computer" in self.current_player:
            _ = input("\nStatus: Computer is about to make a move. Press Enter to continue...\n")

            start, end = self.get_snake_edges()
            if self.computer.can_make_move(start, end):
                self.bad_pieces = True
        else:
            self.get_user_index("\nStatus: It's your turn to make a move. Enter your command.\n")

    def get_user_index(self, msg: str) -> Union[str, None]:
        try:
            user_input = int(input(msg))
            if user_input == 0:
                self.bad_pieces = True
                return None

            self.user.set_index(user_input)
            if self.user.get_index() > self.user.get_pieces_length() - 1:
                raise ValueError

            start, end = self.get_snake_edges()
            if not self.bad_pieces and not self.user.can_make_move(start, end):
                return self.get_user_index("Illegal move. Please try again.\n")

            return None
        except ValueError:
            return self.get_user_index("Invalid input. Please try again.\n")

    def make_move(self) -> None:
        if "user" in self.current_player:
            piece_to_remove = self.user.get_piece()
            self.user.remove_piece(piece_to_remove)
            self.current_player = "computer"
        else:
            piece_to_remove = self.computer.pieces_counter(self.snake)
            self.computer.remove_piece(piece_to_remove)
            self.current_player = "user"

        piece_to_add = self.check_piece_to_add(piece_to_remove)
        self.add_to_snake(piece_to_add)

    def check_piece_to_add(self, piece: list) -> dict:
        start, end = self.get_snake_edges()

        if start in piece:
            return self.reverse_piece(piece, 0, start, "start")
        elif end in piece:
            return self.reverse_piece(piece, 1, end, "end")

    @staticmethod
    def reverse_piece(piece: list, index: int, snake_side: int, string: str) -> dict:
        if piece[index] == snake_side:
            piece.reverse()
        return {string: piece}

    def add_to_snake(self, piece_to_add) -> None:
        if piece_to_add.get("end"):
            self.snake.append(piece_to_add["end"])
        else:
            self.snake.insert(0, piece_to_add["start"])

    def pass_turn(self) -> None:
        piece_taken = choice(self.stock)
        self.stock.remove(piece_taken)

        if self.current_player == "user":
            self.user.add_piece(piece_taken)
            self.current_player = "computer"
        else:
            self.computer.add_piece(piece_taken)
            self.current_player = "user"

        self.bad_pieces = False

    def check_winner(self) -> None:
        if self.user.get_pieces_length() == 0:
            print("\nStatus: The game is over. You won!")
            self.exit_game()
        elif self.computer.get_pieces_length() == 0:
            print("\nStatus: The game is over. The computer won!")
            self.exit_game()

    def check_tie(self) -> None:
        start, end = self.get_snake_edges()
        if start == end:
            counter = sum(p.count(start) for p in self.snake)

            if counter == 8:
                print("Status: The game is over. It's a draw!")
                self.exit_game()

    def get_stock_length(self) -> int:
        return len(self.stock)

    def print_snake_pieces(self) -> None:
        if len(self.snake) < 6:
            print(*self.snake, sep="")
        else:
            print(*self.snake[:3], "...", *self.snake[-3:], sep="")

    def get_snake_edges(self) -> tuple:
        return self.snake[0][0], self.snake[-1][-1]

    @staticmethod
    def exit_game() -> None:
        sys.exit()


if __name__ == "__main__":
    Game().start_game()
