import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import quote

base_url = "https://sg.carousell.com"
query_url = "https://sg.carousell.com/search/products/?query="


def crawl(query, min_price, max_price):
    min_price = int(min_price)
    max_price = int(max_price)

    query = quote(query)
    url = query_url + query
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, "html5lib")

    for card in soup.findAll('figure', {'class': 'card'}):
        title = card.find('h4', {'id': 'productCardTitle'}).string

        price_string = card.find('span', {'id': 'productCardPrice'}).get('title')
        price = float(price_string[2:].replace(',', ''))

        href = card.find('a', {'id': 'productCardThumbnail'}).get('href')
        href = base_url + href

        if min_price < price < max_price:
            print('{} {} {}'.format(title, price_string, href))


        

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        pass

    query = sys.argv[1]

    if(len(sys.argv) == 2):
        crawl(query, 0, sys.maxsize)
    else:
        crawl(query, sys.argv[2], sys.argv[3])