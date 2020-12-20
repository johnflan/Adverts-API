import sys 
sys.path.append('./')

import AdvertsAPI as ads
from AdvertsAPI.utils import pretty_json
import json

advert = ads.AdvertsAPI(county='Dublin')

with open('secret.json', 'r') as f:
    js = json.load(f)
    username = js['username']
    password = js['password']

# print(advert.get_ad_panel()[0].url)
advert.login(username, password)