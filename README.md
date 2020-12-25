# AdvertsAPI

An unofficial API for the community based Irish marketplace, **adverts.ie**.

## Getting Started

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

### Logging into your account

``` python
adverts = AdvertsAPI.AdvertsAPI()
adverts.login("username", "password")
```

### Logging out

``` python
adverts.logout()
```

## Available Functions

* login
* logout
* place_offer
* withdraw_offer
* search_query
* full_ad_info
* get_ad_panel

## place_offer

## withdraw_offer

## search_query

## full_ad_info

## get_ad_panel

## Usage

For documented examples see [examples.py](https://github.com/ahmedhamedaly/AdvertsAPI/blob/master/examples/examples.py)
