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

### Logging into your account

``` python
adverts = AdvertsAPI.AdvertsAPI()
adverts.login('username', 'password')
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

## Constructor

## place_offer

Places an offer given the url of the ad or uses the ad url when initiating the class.

``` python
# given url
```

``` python
# not given url
```

## withdraw_offer

Withdraws an offer to a particular ad, given the url. Only works if you have places an ad.

``` python
```

## search_query

``` python
```

## full_ad_info

``` python
```

## get_ad_panel

``` python
```

## Usage

For documented examples see [examples.py](https://github.com/ahmedhamedaly/Adverts-API/blob/master/examples/examples.py)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Roadmap

See the [open issues](https://github.com/ahmedhamedaly/Adverts-API/issues) for a list of proposed features (and known issues).

## License

Distributed under the [MIT](https://github.com/ahmedhamedaly/Adverts-API/blob/master/LICENSE) License. See `LICENSE` for more information.
