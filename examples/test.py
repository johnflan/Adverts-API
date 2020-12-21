import sys
sys.path.append('./')

import json

import AdvertsAPI as ads
from AdvertsAPI.utils import pretty_json

advert = ads.AdvertsAPI(county='Dublin')

with open('secret.json', 'r') as f:
    js = json.load(f)
    username = js['username']
    password = js['password']

ad0 = advert.get_ad_panel()[0]
advert.login(username, password)
advert.place_offer('https://www.adverts.ie/laptops/hp-pavilion/22443298', '260')
advert.logout()