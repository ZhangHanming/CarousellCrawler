import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def crawl(query):
    query = quote(query)
    base_url = "https://sg.carousell.com/search/products/?query="
    url = base_url + query
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, "html5lib")

    for card in soup.findAll('figure', {'class': 'card'}):
        title = card.find('h4', {'id': 'productCardTitle'}).string
        print(title)

crawl("ipad pro")