from typing import Union


class PLayer:
    def __init__(self) -> None:
        self.pieces = []

    def add_piece(self, piece: list) -> None:
        self.pieces.append(piece)

    def remove_piece(self, piece: list) -> None:
        self.pieces.remove(piece)

    def get_pieces_length(self) -> int:
        return len(self.pieces)

    def can_make_move(self, start: int, end: int) -> None:
        pass


class User(PLayer):
    def __init__(self, pieces: list) -> None:
        super().__init__()
        self.pieces = pieces
        self.index = None

    def add_piece(self, piece: list) -> None:
        super().add_piece(piece)

    def remove_piece(self, piece: list) -> None:
        super().remove_piece(piece)

    def get_pieces_length(self) -> int:
        return super().get_pieces_length()

    def print_pieces(self) -> None:
        for i, p in enumerate(self.pieces):
            print(f"{i + 1}:{p}")

    def set_index(self, index) -> None:
        self.index = abs(index) - 1

    def get_index(self) -> int:
        return self.index

    def get_piece(self) -> list:
        return self.pieces[self.get_index()]

    def can_make_move(self, start: int, end: int) -> bool:
        piece = self.get_piece()
        return start in piece or end in piece


class Computer(PLayer):
    def __init__(self, pieces: list) -> None:
        super().__init__()
        self.pieces = pieces
        self.good_pieces = []

    def add_piece(self, piece: list) -> None:
        super().add_piece(piece)

    def remove_piece(self, piece: list) -> None:
        super().remove_piece(piece)

    def get_pieces_length(self) -> int:
        return super().get_pieces_length()

    def can_make_move(self, start: int, end: int) -> bool:
        for p in self.pieces:
            if start in p or end in p:
                self.good_pieces.append(p)

        return len(self.good_pieces) == 0

    def pieces_counter(self, snake: list) -> list:
        counter = {}
        pieces_score = {}

        for n in range(7):
            snake_count = sum(p.count(n) for p in snake)
            pieces_count = sum(p.count(n) for p in self.pieces)
            counter.update({n: snake_count + pieces_count})

        for p in self.pieces:
            score_sum = counter[p[0]] + counter[p[1]] if p[0] != p[1] else counter[p[0]]

            if pieces_score.get(score_sum):
                pieces_score[score_sum].append(p)
            else:
                pieces_score.update({score_sum: [p]})

        return self.choose_best_piece(pieces_score)

    def choose_best_piece(self, pieces_score: dict) -> Union[list, dict]:
        max_score = max(pieces_score.keys())
        pieces = pieces_score[max_score]
        best_piece = []

        for p in pieces:
            if p in self.good_pieces:
                best_piece = p
                break

        if len(best_piece) != 0:
            self.good_pieces.clear()
            return best_piece

        pieces_score.pop(max_score)
        return self.choose_best_piece(pieces_score)
