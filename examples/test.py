import sys 
sys.path.append('./')

import AdvertsAPI as ads
from AdvertsAPI.utils import pretty_json

advert = ads.AdvertsAPI(county='Dublin')

print(pretty_json(advert.get_ad_panel()))