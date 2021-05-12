import requests
import sys

from bs4 import BeautifulSoup


class Scraper:
    def __init__(self) -> None:
        self.url = "https://www.nature.com/nature/articles"
        self.articles_link = {}
        self.articles_content = {}
        self.articles_saved = []

    def start_scraper(self) -> None:
        self.make_request()
        self.get_articles_content()
        self.save_to_file()

    def make_request(self) -> None:
        r = requests.get(self.url)
        if r.status_code != 200:
            print(f"\nThe URL returned {r.status_code}!")
            self.exit_program()

        self.get_articles_link(BeautifulSoup(r.content, "html.parser"))

    def get_articles_link(self, soup: BeautifulSoup) -> None:
        articles = soup.find_all("article", class_="c-card")

        for tags in articles:
            span = tags.find("span", {"data-test": "article.type"}).get_text().strip()

            if span == "News":
                link = tags.find("a", {"class": "c-card__link"})
                article_url = f'https://www.nature.com{link["href"]}'
                article_title = link.get_text().strip().translate({ord(c): "_" for c in " ./?:'"})

                self.articles_link.update({article_title: article_url})

    def get_articles_content(self) -> None:
        for k, v in self.articles_link.items():
            r = requests.get(v)
            soup = BeautifulSoup(r.content, "html.parser")
            art_content = soup.find("div", class_="article__body")

            if art_content:
                self.articles_content.update({k: art_content.get_text().strip()})

    def save_to_file(self) -> None:
        for k, v in self.articles_content.items():
            file_name = f"{k}.txt"
            self.articles_saved.append(file_name)

            with open(file_name, "wb") as f:
                f.write(v.encode())

        print("\nSaved articles:", self.articles_saved)

    @staticmethod
    def exit_program() -> None:
        sys.exit()


if __name__ == "__main__":
    scraper = Scraper()
    scraper.start_scraper()
