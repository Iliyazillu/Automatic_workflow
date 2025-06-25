import requests
from bs4 import BeautifulSoup

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

def fetch_chapter():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.find('div', {'class': 'mw-parser-output'})
    paragraphs = content_div.find_all('p')
    return "\n".join([p.text for p in paragraphs])

if __name__ == "__main__":
    print(fetch_chapter())
