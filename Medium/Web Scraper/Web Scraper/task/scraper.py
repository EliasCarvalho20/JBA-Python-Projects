import sys
import os
import requests

from bs4 import BeautifulSoup


class Scraper:
    def __init__(self) -> None:
        self.url = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page="
        self.article_category = ""
        self.number_of_pages = 2
        self.articles_link = {}
        self.articles_content = {}
        self.articles_saved = []

    def start_scraper(self) -> None:
        self.get_input()
        self.make_request()
        self.get_articles_content()
        self.save_to_file()

    def get_input(self):
        self.number_of_pages = int(input("Enter the number of pages"))
        self.article_category = input("Enter the article category").lower()

    def make_request(self) -> None:
        if self.number_of_pages != 0:
            for n in range(1, self.number_of_pages + 1):
                r = requests.get(f"{self.url}{n}")
                if r.status_code != 200:
                    print(f"\nThe URL returned {r.status_code}!")
                    self.exit_program()

                self.get_articles_link(BeautifulSoup(r.content, "html.parser"), n)

    def get_articles_link(self, soup: BeautifulSoup, current_page: int) -> None:
        articles = soup.find_all("article", class_="c-card")

        for tags in articles:
            span = tags.find("span", {"data-test": "article.type"}).get_text().strip()

            if span.lower() == self.article_category:
                link = tags.find("a", {"class": "c-card__link"})
                article_url = f'https://www.nature.com{link["href"]}'
                article_title = link.get_text().strip().translate({ord(c): "_" for c in " .-/?:'"})

                if not self.articles_link.get(current_page):
                    self.articles_link.update({current_page: {}})

                self.articles_link[current_page].update({article_title: article_url})

    def get_articles_content(self) -> None:
        pages = self.articles_link.keys()
        for p in pages:
            for k, v in self.articles_link[p].items():
                r = requests.get(v)
                soup = BeautifulSoup(r.content, "html.parser")
                art_content = soup.find("div", class_="article__body") or soup.find("div", class_="article-item__body")

                if art_content:
                    if not self.articles_content.get(p):
                        self.articles_content.update({p: {}})
                    self.articles_content[p].update({k: art_content.get_text().strip()})

    def save_to_file(self) -> None:
        for n in range(1, self.number_of_pages + 1):
            folder_name = os.path.join(os.getcwd(), f"Page_{n}")
            os.mkdir(folder_name)

            if not self.articles_content.get(n):
                continue

            for k, v in self.articles_content[n].items():
                file_name = f"{folder_name}\\{k}.txt"
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
