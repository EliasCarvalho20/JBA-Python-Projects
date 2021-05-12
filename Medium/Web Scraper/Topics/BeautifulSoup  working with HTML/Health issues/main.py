import requests

from bs4 import BeautifulSoup

url = input()
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
a = soup.find_all('a')

result = []
for tag in a:
    if tag.text.startswith('S') and len(tag.text) > 1:
        if 'entity' in tag.get('href') or 'topics' in tag.get('href'):
            result.append(tag.text)

print(result)
