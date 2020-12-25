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

advert.login(username, password)
ads = advert.search('graphics card')
print(ads[0].price)
advert.logout()