from adverts import Adverts as ad

url = 'https://www.adverts.ie/for-sale/county-Dublin/price_0/page-1'
advert = ad(county='Dublin', min_price=2)

print(advert.get_ad_panel())
