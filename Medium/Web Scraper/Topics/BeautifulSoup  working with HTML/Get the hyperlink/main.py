import requests
from bs4 import BeautifulSoup

user = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

print(soup.find("a", text=f"ACT {user}").get("href"))
