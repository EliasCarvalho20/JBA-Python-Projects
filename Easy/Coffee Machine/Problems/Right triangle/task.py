class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.s = (self.a * self.b) / 2

    def get_area(self):
        return self.c ** 2 == self.a ** 2 + self.b ** 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
my_triangle = RightTriangle(input_c, input_a, input_b)
print(f"{my_triangle.s:.1f}" if my_triangle.get_area() else "Not right")
