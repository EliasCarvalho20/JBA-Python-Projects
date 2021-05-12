import requests
import sys


class Scraper:
    def __init__(self) -> None:
        self.url = ""

    def start_scraper(self) -> None:
        self.get_input()
        self.make_request()

    def get_input(self) -> None:
        self.url = input("Input the URL:\n")

    def make_request(self) -> None:
        r = requests.get(self.url)
        if r.status_code != 200:
            print(f"\nThe URL returned {r.status_code}!")
            self.exit_program()

        self.save_to_file(r.content)

    @staticmethod
    def save_to_file(page_content: dict) -> None:
        with open("source.html", "wb") as f:
            f.write(page_content)

        print("\nContent saved.")

    @staticmethod
    def exit_program() -> None:
        sys.exit()


if __name__ == "__main__":
    scraper = Scraper()
    scraper.start_scraper()
