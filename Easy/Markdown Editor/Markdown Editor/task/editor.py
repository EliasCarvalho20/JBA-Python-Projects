import sys
from itertools import chain


class MarkDown:
    def __init__(self) -> None:
        self.user_input = ""
        self.formatted = []
        self.commands = ["!help", "!done"]
        self.help = [
            "Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line",
            "Special commands: !help !done",
        ]
        self.formatters = {
            "plain": self.plain,
            "bold": self.bold,
            "italic": self.italic,
            "header": self.header,
            "link": self.link,
            "inline-code": self.inline,
            "ordered-list": self.list,
            "unordered-list": self.list,
            "new-line": self.new_line,
        }

    def handle_user_input(self) -> None:
        while "!done" not in (user_input := input("- Choose a formatter: ")):
            self.user_input = user_input

            if self.user_input not in chain(self.commands, self.formatters):
                print("Unknown formatting type or command. Please try again")
                continue
            elif self.user_input == self.commands[0]:
                print(*self.help, sep="\n")
            elif self.user_input in self.formatters:
                self.handle_formatters_call()

        self.save_file()

        self.exit_program()

    def print_formatters(self) -> None:
        print(*self.formatted, sep="")

    def handle_formatters_call(self) -> None:
        self.formatters[self.user_input]()
        self.print_formatters()

    def plain(self) -> None:
        self.formatted.append(input("- Text: "))

    def bold(self) -> None:
        string_formatted = f"**{input('- Text: ')}**"
        self.formatted.append(string_formatted)

    def italic(self) -> None:
        string_formatted = f"*{input('- Text: ')}*"
        self.formatted.append(string_formatted)

    def header(self) -> None:
        header_level = "#" * int(input("- Level: "))
        string_formatted = f"{header_level} {input('- Text: ')}\n"
        self.formatted.append(string_formatted)

    def link(self) -> None:
        label = input("- Label: ")
        url = input("- URL: ")
        string_formatted = f"[{label}]({url})"
        self.formatted.append(string_formatted)

    def inline(self) -> None:
        string_formatted = f"`{input('- Text: ')}`"
        self.formatted.append(string_formatted)

    def list(self) -> None:
        while True:
            try:
                rows = int(input("- Number of rows: "))
                if rows < 1:
                    raise ValueError

            except ValueError:
                print("The number of rows should be greater than zero")
                continue

            is_ordered = self.user_input == "ordered-list"

            for n in range(rows):
                number = n + 1
                text = f"{input(f'- Row #{number}: ')}"
                string_formatted = (
                    f"{number}. {text}\n" if is_ordered else f"* {text}\n"
                )
                self.formatted.append(string_formatted)

            break

    def new_line(self) -> None:
        self.formatted.append("\n")

    def save_file(self):
        with open("output.md", "w") as file:
            file.writelines(self.formatted)

    @staticmethod
    def exit_program() -> None:
        sys.exit()


if __name__ == "__main__":
    md = MarkDown()
    md.handle_user_input()
