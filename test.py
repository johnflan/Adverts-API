import bs4 as bs
import requests
from adverts import Adverts as ad

url = 'https://www.adverts.ie/for-sale/county-Dublin/price_0/page-1'
advert = ad(county='Dublin')
response = advert.get()

soup = bs.BeautifulSoup(response, 'html.parser')

print(advert.get_ad_panel())
# print(soup.find_all('div', class_='sr-grid-cell quick-peek-container'))
# [1].findChildren()[1])