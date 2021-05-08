import math
import random
from tictactoe import TicTacToe


class Player:
    def __init__(self, letter: str) -> None:
        self.letter = letter

    def get_move(self, game: TicTacToe) -> None:
        pass


class HumanPlayer(Player):
    def __init__(self, letter: str) -> None:
        super().__init__(letter)

    def get_move(self, game: TicTacToe) -> int:
        valid_square = False
        square = None

        while not valid_square:
            try:
                row, column = [int(n) for n in input("Enter the coordinates: ").split()]
            except ValueError:
                print("You should enter numbers!")
                continue
            if not (1 <= row <= 3 and 1 <= column <= 3):
                print("Coordinates should be from 1 to 3!")
                continue

            square = (((row - 1) * 3) + (column + 2)) - 3
            if square not in game.available_moves():
                print("This cell is occupied! Choose another one!")
                continue

            valid_square = True

        return square


class Skynet(Player):
    def __init__(self, letter: str, dif_level: str) -> None:
        super().__init__(letter)
        self.difficulty = dif_level

    def get_move(self, game: TicTacToe) -> int:
        current_difficulty = self.get_difficulty()

        if current_difficulty == "easy":
            return random.choice(game.available_moves())
        elif len(game.available_moves()) >= 7 and current_difficulty == "medium":
            return random.choice(game.available_moves())
        else:
            return self.minimax(game, self.letter)["position"]

    def get_difficulty(self) -> str:
        return self.difficulty

    def minimax(self, state: TicTacToe, player: str) -> dict:
        max_player = self.letter  # current player
        other_player = "O" if player == "X" else "X"

        if state.current_winner == other_player:
            empty_square = state.num_empty_squares() + 1

            return {
                "position": None,
                "score": 1 * empty_square
                if other_player == max_player
                else -1 * empty_square,
            }

        elif not state.empty_square():  # no empty square
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # each score should maximizes
        else:
            best = {"position": None, "score": math.inf}  # each score should minimizes

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making a move
            sim_score = self.minimax(state, other_player)  # alternate players

            # step 3: undo the moves
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score  # replace best
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score  # replace best

        return best
