import requests
from bs4 import BeautifulSoup as bs

def get_bbc_text(url:str) -> list:
    """Parse bbc article and return text in list of strings"""

    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    body = soup.find(property="articleBody")
    print(body)
    text = [p.text for p in body.find_all("p")]
    return text

get_bbc_text("https://www.bbc.co.uk/news/world-europe-49345912")