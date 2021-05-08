from random import choice


class RPS():
    def __init__(self):
        self.names = {n: int(i) for n, i in [s.rstrip().split() for s in open("rating.txt", 'r')]}
        self.user, self.commands, self.options = '', ["!exit", "!rating"], ['rock', 'paper', 'scissors']
        self.play = True

    def main(self):
        while self.play:
            if not self.user:
                self.update_user()
                print("Okay, let's start")
            string = input()
            self.is_command(string)

    def update_user(self):
        self.user = input("Enter your name: ")
        print(f"Hello, {self.user}")
        if self.user not in self.names:
            self.names.update({self.user: 0})
        a = dict()
        a.values()

        options_line = input()
        if options_line:
            self.options = options_line.split(',')

    def is_command(self, string):
        if string in self.commands[0]:
            print("Bye!")
            self.play = False
        elif string in self.commands[1]:
            print(f"Your rating: {self.get_score()}")
        elif string in self.options:
            self.start(string)
        else:
            print('Invalid input')

    def start(self, string):
        # algorithm to cut the option that the user chose
        cut = len(self.options) // 2
        index = 1 + self.options.index(string)
        if index > cut:
            lose = self.options[index:] + self.options[:index - cut - 1]
        else:
            lose = self.options[index:index + cut]

        computer = choice(self.options)
        if string == computer:
            self.names[self.user] += 50
            print(f"There is a draw ({computer})")
        elif computer in lose:
            print(f"Sorry, but computer chose {computer}")
        else:
            self.names[self.user] += 100
            print(f"Well done. Computer chose {computer} and failed")

    def get_score(self):
        if self.user in self.names.keys():
            return self.names[self.user]


if __name__ == '__main__':
    game = RPS()
    game.main()
