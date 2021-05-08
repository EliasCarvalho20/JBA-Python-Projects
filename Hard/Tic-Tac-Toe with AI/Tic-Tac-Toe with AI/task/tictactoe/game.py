import sys
import re
from time import sleep

from player import HumanPlayer, Skynet
from tictactoe import TicTacToe
from typing import List, Match


class Game:
    def __init__(self) -> None:
        self.tic_tac = None
        self.x_player = None
        self.o_player = None

    def game_mode(self, commands: List) -> None:
        def check_regex(pattern: str) -> Match:
            string_to_compare = f"{commands[0]} {commands[1]}"
            return re.search(pattern, string_to_compare)

        self.tic_tac = TicTacToe(None)

        if "user" in commands:
            user_vs_user = check_regex(r"^(user\s*){2}$")
            user_vs_ai = check_regex("(easy|medium|hard)")

            if user_vs_user:
                x_player = HumanPlayer("X")
                o_player = HumanPlayer("O")
            elif 5 in user_vs_ai.span():
                # X = HumanPlayer, O = Skynet
                x_player = HumanPlayer("X")
                o_player = Skynet("O", commands[1])
            else:
                # X = Skynet, O = HumanPlayer
                x_player = Skynet("X", commands[0])
                o_player = HumanPlayer("O")

        else:
            # Skynet vs Skynet
            x_player = Skynet("X", commands[0])
            o_player = Skynet("O", commands[1])

        self.x_player = x_player
        self.o_player = o_player
        self.play()

    def play(self) -> None:
        # returns the winner of the game or None for a tie
        self.tic_tac.print_board()
        letter = "X"

        if self.tic_tac.current_winner is None:
            # iterate while the game still has empty squares
            while self.tic_tac.empty_square():
                # get the move from the right player
                if letter == "O":
                    square = self.o_player.get_move(self.tic_tac)
                else:
                    square = self.x_player.get_move(self.tic_tac)

                if self.tic_tac.make_move(square, letter):
                    # check the type of the player
                    if type(self.x_player) == Skynet and self.x_player.letter == letter:
                        print(f'Making move level "{self.x_player.get_difficulty()}"')
                        sleep(1)
                    if type(self.o_player) == Skynet and self.o_player.letter == letter:
                        print(f'Making move level "{self.o_player.get_difficulty()}"')
                        sleep(1)

                    self.tic_tac.print_board()

                    if self.tic_tac.current_winner:
                        print(letter + " wins")
                        print()
                        break

                    letter = "O" if letter == "X" else "X"

            if not self.tic_tac.empty_square() and self.tic_tac.current_winner is None:
                print("Draw")
                print()


def setup_game() -> None:
    print("=" * 50)
    print(
        "Welcome to TicTacToe game!\n"
        "Use one of the following commands to play:\n\n"
        'Use "user" to play it yourself.\n'
        'Use "easy", "medium" or "hard" to set a difficulty for the AI.\n'
        "You can play it against yourself, against the AI\nor make the AI play against itself.\n"
        'e.g.: "user medium", "user user", "hard easy"\n\n'
        "The order of the commands doesn't matter.\n"
        "Don't forget to separate each command with a space."
    )
    print("=" * 50)
    print()

    while "exit" not in (commands := input("Input command: ").split(" ")):
        if len(commands) != 2:
            print("Bad parameters!")
            continue

        pattern = "(user)|(easy|medium|hard)"
        match1 = re.search(pattern, commands[0])
        match2 = re.search(pattern, commands[1])

        if match1 is None or match2 is None:
            print("Invalid commands")
            continue

        if "exit" in commands:
            exit_game()

        Game().game_mode(commands)


def exit_game() -> None:
    sys.exit()


if __name__ == "__main__":
    setup_game()
