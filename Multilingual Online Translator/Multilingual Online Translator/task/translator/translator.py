import requests, sys
from requests import exceptions
from bs4 import BeautifulSoup


class Translator():
    def __init__(self):
        self.language = {0: "all", 1: "arabic", 2: "german", 3: "english", 4: "spanish", 5: "french", 6: "hebrew",
                         7: "japanese", 8: "dutch", 9: "polish", 10: "portuguese", 11: "romanian", 12: "russian",
                         13: "turkish"}
        self.response, self.url = '', ''
        self.translation, self.examples, self.choice = [], [], []

    def main(self):
        '''print("Hello, welcome to the translator. Translator supports:")
        for key, item in self.language.items():
            print(f"{key}. {item.capitalize()}")
        self.choice = [self.language[int(input("Type the number of your language:"))],
                       self.language.get(int(input("Type the number of a language you want to translate to or '0' to "
                                                   " translate to all languages:"))),
                       input("Type the word you want to translate:")]'''
        try:
            self.choice = [sys.argv[1], sys.argv[2], sys.argv[3]]
            self.check_input()
        except IndexError:
            print("Seems like you forgot to input the word to translate")

    def check_input(self):
        if self.choice[0] not in self.language.values():
            print(f"Sorry, the program doesn't support {self.choice[0]}")
        elif self.choice[1] not in self.language.values():
            print(f"Sorry, the program doesn't support {self.choice[1]}")
        elif self.choice[1] == self.language[0]:
            self.print_file()
        else:
            self.set_url()
            if self.get_request():
                print(f"Sorry, unable to find {self.choice[2]}")
            else:
                self.format_list()
                self.print_list()

    def set_url(self):
        if self.choice[1] in self.language.values():
            self.url = f"https://context.reverso.net/translation/{self.choice[0]}-{self.choice[1]}/{self.choice[2]}"

    def get_request(self):
        try:
            self.response = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        except (requests.ConnectionError, requests.Timeout, exceptions):
            print("Something wrong with your internet connection")

        if self.response.status_code == 404:
            return True

    def format_list(self, max_=5):
        self.translation.clear()
        self.examples.clear()
        soup = BeautifulSoup(self.response.content, features='html.parser')
        a_tags = soup.select("*.translation.dict")
        div_tags = soup.select("*.example")
        for tag in a_tags:
            self.translation.append(tag.text.strip())
            if len(self.translation) == max_:
                break
        for div in div_tags:
            src_trg = div.select("*.text")
            self.examples.append([src_trg[0].text.strip(), src_trg[1].text.strip()])
            if len(self.examples) == max_:
                break

    def print_list(self):
        print("\nContext examples:\n")
        print(f"{self.choice[1].capitalize()} Translations:")
        print(*self.translation, sep='\n')
        print(f"\n{self.choice[1].capitalize()} Examples:")
        for i in range(5):
            print(f"{self.examples[i][0]}\n{self.examples[i][1]}\n")

    def print_file(self):
        try:
            with open(f"{self.choice[2]}.txt", "r", encoding="utf-8") as f:
                for line in f:
                    print(line, end='')
        except FileNotFoundError:
            print(f"Sorry, unable to find the file {self.choice[2]}.txt")

    def write_file(self):
        with open(f"{self.choice[2]}.txt", "w", encoding='UTF-8') as f:
            for i in range(1, len(self.language)):
                if self.choice[0] == self.language[i]:
                    continue
                self.choice[1] = self.language[i]
                self.set_url()
                self.get_request()
                self.format_list(1)
                print(f"{self.choice[1].capitalize()} Translations:\n{self.translation[0]}\n", file=f)
                print(f"{self.choice[1].capitalize()} Translations:\n{self.translation[0]}\n")
                print(f"{self.choice[1].capitalize()} Examples:", file=f)
                print(f"{self.examples[0][0]}:\n{self.examples[0][1]}\n\n", file=f)
                print(f"{self.choice[1].capitalize()} Examples:")
                print(f"{self.examples[0][0]}:\n{self.examples[0][1]}\n\n")


if __name__ == '__main__':
    translator = Translator()
    translator.main()