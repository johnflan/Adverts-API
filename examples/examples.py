import json
import sys
sys.path.append('./')

import AdvertsAPI
from AdvertsAPI.category import Category
from AdvertsAPI.utils import pretty_json

with open('secret.json', 'r') as f:
    js = json.load(f)
    username = js['username']
    password = js['password']

# Constructor
## Default: category=None, county=None, min_price=0, max_price=0, view='grid_view', search=None
advert = AdvertsAPI.AdvertsAPI()

## Bike in Dublin: category=Category.SPORTS_FITNESS__BIKES, county='Dublin', min_price=0, max_price=0, view='grid_view', search=None
advert = AdvertsAPI.AdvertsAPI(category=Category.SPORTS_FITNESS__BIKES, county='Dublin')

## Mountain bike in Dublin: category=Category.SPORTS_FITNESS__BIKES, county='Dublin', min_price=0, max_price=0, view='grid_view', search='mountain'
advert = AdvertsAPI.AdvertsAPI(category=Category.SPORTS_FITNESS__BIKES, county='Dublin', search='mountain')

## ps4 between 100-300 euro: category=Category.CONSOLES_GAMES, county=None, min_price=100, max_price=300, view='grid_view', search='ps4'
advert = AdvertsAPI.AdvertsAPI(category=Category.CONSOLES_GAMES, min_price=100, max_price=300, search='ps4')

## free items in Dublin: category=None, county='Dublin', min_price=0, max_price=0, view='grid_view', search=None
advert = AdvertsAPI.AdvertsAPI(county='Dublin')

# login
advert.login(username, password)

# get_ad_panel
ads = advert.get_ad_panel()    # NOTE: given the contructor details, it will produce the url for the search

# get_ad_panel: (given a search url)
ads = advert.get_ad_panel('https://www.adverts.ie/for-sale/price_0-0/')

# top 30 ads
for ad in ads:
    print(ad.price)
    print(ad.title)
    print(ad.area)
    print(ad.county)
    print(ad.category)
    print(ad.url)

# place_offer 
advert.place_offer('ad_url', 100)   # NOTE: it will place an offer below the ask if given an offer above the asking price.

# place_offer (from ad_panels)
advert.place_offer(ads[0].url, 0)

# withdraw_offer
advert.withdraw_offer('ad_url')    # NOTE: you must have an active offer placed

# full_ad_info 
advert.full_ad_info('ad_url')

# full_ad_info (from ad_panels)
ads = advert.full_ad_info(ads[0].url)

for ad in ads:
    print(ad.title)
    print(ad.price)
    print(ad.seller)
    print(ad.positive)
    print(ad.negative)
    print(ad.location)
    print(ad.date_entered)
    print(ad.ad_views)
    print(ad.description)

# search_query (using constructor search)
advert.search_query()

# search_query (given query)
ads = advert.search_query('mountain bikes')

for ad in ads:
    print(ad.title)
    # ...
    print(ad.url)

# logout
advert.logout()