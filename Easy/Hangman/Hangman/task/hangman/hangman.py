class CoffeeMachine:
    def __init__(self):
        self.on = True
        self.command = "buy", "fill", "take", "remaining", "exit"
        self.supply = ["water", 400, "milk", 540, "coffee beans", 120, "disposable cups", 9, "money", 550]
        self.coffee = [["espresso", -250, 0, -16, -1, 4], ["latte", -350, -75, -20, -1, 7],
                       ["cappuccino", -200, -100, -12, -1, 6]]

    def user_input(self, string):
        if string in self.command[4]:
            self.on = False
        elif string in self.command[0]:
            self.buy()
        elif string in self.command[1]:
            self.fill()
        elif string in self.command[2]:
            self.take()
        else:
            self.show_supply()

    def show_supply(self):
        print("The coffee machine has:")
        for i in range(1, 10, 2):
            print(f"{self.supply[i]} of ", end="")
            j = i - 1
            print(f"{self.supply[j]}")

    def change_supply(self, i):
        for k, j in enumerate(range(1, 11, 2), start=1):
            self.supply[j] += self.coffee[i][k]

    def can_make(self, i):
        for n, j in enumerate(range(1, 9, 2), start=1):
            if not self.supply[j] + self.coffee[i][n] > 0:
                k = j - 1
                print(f"Sorry, no enough {self.supply[k]}!")
                return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self):
        choice = input(f"What do you want to buy? 1 - {self.coffee[0][0]}, "
                       f"2 - {self.coffee[1][0]}, 3 - {self.coffee[2][0]}, "
                       f"back - to main menu:\n ")
        if '1' in choice and self.can_make(0):
            self.change_supply(0)
        if '2' in choice and self.can_make(1):
            self.change_supply(1)
        if '3' in choice and self.can_make(2):
            self.change_supply(2)

    def fill(self):
        self.supply[1] += int(input(f"Write how many ml of {self.supply[0]} do you want to add:\n"))
        self.supply[3] += int(input(f"Write how many ml of {self.supply[2]} do you want to add:\n "))
        self.supply[5] += int(input(f"Write how many grams of {self.supply[4]} do you want to add:\n "))
        self.supply[7] += int(input(f"Write how many {self.supply[6]} of coffee do you want to add:\n "))

    def take(self):
        print(f'I gave you ${self.supply[9]}')
        self.supply[9] = 0


machine = CooffeMachine()
while machine.on:
    print()
    machine.user_input(input(f"Write action (buy, fill, take, remaining, exit):\n"))
    print()
