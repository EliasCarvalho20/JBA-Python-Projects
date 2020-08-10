class CoffeMachine:
    def __init__(self):
        self.on = True
        self.command = "buy", "fill", "take", "remaining", "exit"
        self.supply = [["water", "milk", "coffee beans", "disposable cups", "money"],
                       [400, 540, 120, 9, 550]]
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
        for i in range(5):
            print(f"{self.supply[1][i]} of {self.supply[0][i]}")

    def change_supply(self, i):
        for j in range(len(self.supply[0])):
            self.supply[1][j] += self.coffee[i][j + 1]

    def can_make(self, i):
        for j in range(4):
            if self.supply[1][j] + self.coffee[i][j + 1] < 0:
                print(f"Sorry, no enough {self.supply[0][j]}!")
                return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self):
        choice = input(f"What do you want to buy? 1 - {self.coffee[0][0]}, "
                       f"2 - {self.coffee[1][0]}, 3 - {self.coffee[2][0]}, "
                       f"back - to main menu:\n ")
        if '1' in choice:
            if self.can_make(0):
                self.change_supply(0)
        if '2' in choice:
            if self.can_make(1):
                self.change_supply(1)
        if '3' in choice:
            if self.can_make(2):
                self.change_supply(2)

    def fill(self):
        self.supply[1][0] += int(input(f"Write how many ml of {self.supply[0][0]} do you want to add:\n"))
        self.supply[1][1] += int(input(f"Write how many ml of {self.supply[0][1]} do you want to add:\n "))
        self.supply[1][2] += int(input(f"Write how many grams of {self.supply[0][2]} do you want to add:\n "))
        self.supply[1][3] += int(input(f"Write how many {self.supply[0][3]} of coffee do you want to add:\n "))

    def take(self):
        print(f'I gave you ${self.supply[1][4]}')
        self.supply[1][4] = 0


machine = CoffeMachine()
while machine.on:
    print()
    machine.user_input(input(f"Write action (buy, fill, take, remaining, exit):\n"))
    print()
