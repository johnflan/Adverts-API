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

ad0 = advert.get_ad_panel()[0].url
print(ad0)
advert.login(username, password)
# advert.place_offer(ad0, '260')
advert.full_ad_info('https://www.adverts.ie/office-desks/free-office-desk/22274979')
advert.logout()