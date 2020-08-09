from math import sqrt


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return f"{sqrt(27) * (self.side_length ** 2) / 2:.3f}"
