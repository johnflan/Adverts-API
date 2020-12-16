import bs4 as bs
import requests
from adverts import Adverts as ad

url = 'https://www.adverts.ie/for-sale/county-Dublin/price_0/page-1'
xi = ad(county='Dublin')
print(xi.get())

# soup = bs.BeautifulSoup(response.text, 'html.parser')

# print(soup.find_all('div', class_='sr-grid-cell quick-peek-container')[1].findChildren()[1])