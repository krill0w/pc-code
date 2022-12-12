from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen("https://www.bbc.co.uk/news/")
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

data = [element.text for element in soup.find_all('h3')]
data = set(data)
searchfor = 'lockdown'

for x in data:
  if searchfor in data:
    print('Found')