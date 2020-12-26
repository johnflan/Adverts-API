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

## Available Methods

* Constructor
* login
* get_ad_panel
* place_offer
* withdraw_offer
* full_ad_info
* search_query
* logout

## Constructor

**Default:** category=None, county=None, min_price=0, max_price=0, view='grid_view', search=None

``` python
advert = AdvertsAPI.AdvertsAPI()
```

**Bike in Dublin:** category=Category.SPORTS_FITNESS__BIKES, county='Dublin', min_price=0, max_price=0, view='grid_view', search=None

``` python
advert = AdvertsAPI.AdvertsAPI(category=Category.SPORTS_FITNESS__BIKES, county='Dublin')
```

**Mountain bike in Dublin:** category=Category.SPORTS_FITNESS__BIKES, county='Dublin', min_price=0, max_price=0, view='grid_view', search='mountain'

``` python
advert = AdvertsAPI.AdvertsAPI(category=Category.SPORTS_FITNESS__BIKES, county='Dublin', search='mountain')
```

**ps4 between 100-300 euro:** category=Category.CONSOLES_GAMES, county=None, min_price=100, max_price=300, view='grid_view', search='ps4'

``` python
advert = AdvertsAPI.AdvertsAPI(category=Category.CONSOLES_GAMES, min_price=100, max_price=300, search='ps4')
```

**free items in Dublin:** category=None, county='Dublin', min_price=0, max_price=0, view='grid_view', search=None

``` python
advert = AdvertsAPI.AdvertsAPI(county='Dublin')
```

## login

``` python
adverts = AdvertsAPI.AdvertsAPI()
adverts.login('username', 'password')
```

## get_ad_panel

**NOTE:** given the contructor details, it will produce the url for the search.

``` python
ads = advert.get_ad_panel()
```

However you could also pass in the url of the search and it will compute for you.

``` python
ads = advert.get_ad_panel('https://www.adverts.ie/for-sale/price_0-0/')
```

It will return a list of the top 30 ads for that search. The attributes that can be retreived are: `price`, `title`, `area`, `county`, `category` and `url`

``` python
for ad in ads:
    print(ad.price)
    print(ad.title)
    print(ad.area)
    print(ad.county)
    print(ad.category)
    print(ad.url)
```

## place_offer

This will place an offer given the url of the ad directly.

Below is an example given a url that is static.

``` python
advert.place_offer('ad_url', 100)   
```

Below will place an offer on the first ad of the ads retreieved [above](#get_ad_panel).

``` python
advert.place_offer(ads[0].url, 0)
```

## withdraw_offer

Withdraws an offer to a particular ad, given the url. You must have an active offer to withdraw the ad.

``` python
advert.withdraw_offer('ad_url')    
```

## full_ad_info

This will return all the information of the ad given the url. The attributes that can be retreived are: `title`, `price`, `seller`, `positive`, `negative`, `location` `date_entered`, `ad_views` and `description`.

``` python
advert.full_ad_info('ad_url')
```

``` python
ads = advert.full_ad_info(ads[0].url)
```

You can retreive the data as follows:

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

Search query will use the constructor generated url to search for ads.

``` python
advert.search_query()
```

However you can pass a search query to the method and it will return the search results of the query.

``` python
# search_query (given query)
ads = advert.search_query('mountain bikes')
```

Similar to the [get_ad_panel](#get_ad_panel) method, you can retreive the data as below:

``` python
for ad in ads:
    print(ad.title)
    # ...
    print(ad.url)
```

## logout

Not very necessary as it will discard the cookies as the program stops.

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
