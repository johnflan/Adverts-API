import sys
sys.path.append('./')

import json

import advertsapi as ads
from advertsapi import category
from advertsapi.utils import pretty_json

advert = ads.AdvertsAPI(county='Dublin')

with open('secret.json', 'r') as f:
    js = json.load(f)
    username = js['username']
    password = js['password']

advert.login(username, password)
ads = advert.search_query('graphics card')
advert.logout()