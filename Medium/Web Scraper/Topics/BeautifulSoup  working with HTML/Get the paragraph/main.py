import requests

from bs4 import BeautifulSoup

user = input()
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

p = soup.findAll("p")
for tags in p:
    if user in tags.text:
        print(tags.text)
        break
