# AdvertsAPI

An unofficial API for the community based Irish marketplace, **adverts.ie**.

## Getting Started

### Prerequisites

* Python 3.6 >=

### Installing

``` shell
pip install AdvertsAPI
```

### Dependecies

``` shell
pip install requests
pip install beautifulsoup4 
pip install mechanize
```

### Imports

``` python
import AdvertsAPI
from AdvertsAPI.category import Category
from AdvertsAPI.utils import pretty_json
```

## Available Functions

* Constructor
* login
* get_ad_panel
* place_offer
* withdraw_offer
* full_ad_info
* search_query
* logout

## Constructor

``` python
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
```

## login

``` python
adverts = AdvertsAPI.AdvertsAPI()
adverts.login('username', 'password')
```

## get_ad_panel

``` python
# get_ad_panel
ads = advert.get_ad_panel()    # NOTE: given the contructor details, it will produce the url for the search

# get_ad_panel: (given a search url)
ads = advert.get_ad_panel('https://www.adverts.ie/for-sale/price_0-0/')

```

``` python
# top 30 ads
for ad in ads:
    print(ad.price)
    print(ad.title)
    print(ad.area)
    print(ad.county)
    print(ad.category)
    print(ad.url)
```

## place_offer

Places an offer given the url of the ad or uses the ad url when initiating the class.

``` python
# place_offer 
advert.place_offer('ad_url', 100)   
# NOTE: it will place an offer below the ask if given an offer above the asking price.
```

``` python
# place_offer (from ad_panels)
advert.place_offer(ads[0].url, 0)
```

## withdraw_offer

Withdraws an offer to a particular ad, given the url. Only works if you have places an ad.

``` python
# withdraw_offer
advert.withdraw_offer('ad_url')    
# NOTE: you must have an active offer placed
```

## full_ad_info

``` python
# full_ad_info 
advert.full_ad_info('ad_url')
```

``` python
# full_ad_info (from ad_panels)
ads = advert.full_ad_info(ads[0].url)
```

``` python
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
```

## search_query

``` python
# search_query (using constructor search)
advert.search_query()
```

``` python
# search_query (given query)
ads = advert.search_query('mountain bikes')
```

``` python
for ad in ads:
    print(ad.title)
    # ...
    print(ad.url)
```

## logout

``` python
adverts.logout()
```

## Usage

For documented examples see [examples.py](https://github.com/ahmedhamedaly/Adverts-API/blob/master/examples/examples.py)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Roadmap

See the [open issues](https://github.com/ahmedhamedaly/Adverts-API/issues) for a list of proposed features (and known issues).

## License

Distributed under the [MIT](https://github.com/ahmedhamedaly/Adverts-API/blob/master/LICENSE) License. See `LICENSE` for more information.
