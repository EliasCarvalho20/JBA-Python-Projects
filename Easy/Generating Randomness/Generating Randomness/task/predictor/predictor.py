from random import randint


class Predictor:
    def __init__(self):
        self.max_chars = 100
        self.user_numbers = ""
        self.user_money = 1000
        self.string_size = 0
        self.user_static = {}
        self.profile = {
            "000": [0, 0],
            "001": [0, 0],
            "010": [0, 0],
            "011": [0, 0],
            "100": [0, 0],
            "101": [0, 0],
            "110": [0, 0],
            "111": [0, 0],
        }

    def execute(self):
        self.get_user_input()
        self.slice_string()
        self.set_user_static()
        self.show_message()
        self.make_prediction()

    def get_user_input(self):
        print("Please give AI some data to learn...")

        while len(self.user_numbers) <= 100:
            left = self.max_chars - self.string_size
            print(f"Current data length is {self.string_size}, {left} symbols left\n")
            user_input = input("Print a random string containing 0 or 1:\n")

            self.user_numbers += "".join(c for c in user_input if c in "01")
            self.string_size = len(self.user_numbers)

        print(f"\nFinal data string:\n{self.user_numbers}\n")

    def set_user_static(self):
        for key in self.profile.keys():
            temp = self.profile[key]
            self.user_static.update({key: temp.index(max(temp))})

    def slice_string(self):
        for n in range(self.string_size - 3):
            triad = self.user_numbers[n : n + 3]

            if self.profile.get(triad):
                if self.user_numbers[n + 3] == "0":
                    self.profile[triad][0] += 1
                elif self.user_numbers[n + 3] == "1":
                    self.profile[triad][1] += 1

    def show_message(self):
        print(
            f"You have ${self.user_money}. Every time the system successfully predicts your next press, "
            "you lose $1.\nOtherwise, you earn $1. Print 'enough' to leave the game. Let's go!"
        )

    def make_prediction(self):
        while (user_input := input("\nPrint a random string containing 0 or 1:\n")) != "enough":
            if set(user_input) != {"0", "1"}:
                continue

            prediction = "".join(str(randint(0, 1)) for _ in range(3))
            str_size = len(user_input) - 3
            hits = 0

            for i in range(0, str_size):
                triad = user_input[i: i + 3:]
                number = str(self.user_static[triad])
                prediction += number

                if user_input[i + 3] == number:
                    hits += 1
                    self.user_money -= 1
                else:
                    self.user_money += 1

            print(f"\nPrediction:\n{prediction}")

            percentage = round((hits / str_size) * 100, 2)
            print(f"\nComputer guessed right {hits} out of {str_size} symbols ({percentage} %)")
            print(f"Your capital is now ${self.user_money}")

        print("Game over!")


if __name__ == "__main__":
    predict = Predictor()
    predict.execute()
