import http.cookiejar

import bs4 as bs
import mechanize
import requests
import os

from AdvertsAPI.product_info import ProductInfo
from selenium import webdriver

class AdvertsAPI:

    __base_url = 'https://www.adverts.ie/for-sale/'

    __login_url = 'https://www.adverts.ie/login'
    __logout_url = 'https://www.adverts.ie/logout'
    __loggedIn = False

    __price_tag = "div[class='price'] > a"
    __title_tag = "div[class='title'] > a"
    __area_Tag = "div[class='location'] > a"
    __county_tag = "div[class='location'] > a"
    __category_tag = "div[class='location'] > a"
    __url_tag = "div[class='price'] > a"

    def __init__(self, category=None, county=None, min_price=0, max_price=0, view='grid_view', keywords=None):
        super().__init__()
        self.category = category
        self.county = county
        self.min_price = min_price
        self.max_price = max_price
        self.view = view
        self.keywords = keywords
        self.url = self.__generate_url()
        self.cj = http.cookiejar.CookieJar()
        self.br = mechanize.Browser()
        self.driver = self.__init_browser()
        print(os.getcwd())

    
    def login(self, username, password):
        self.br.set_handle_robots(False)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        self.br.set_cookiejar(self.cj)
        self.br.open(self.__login_url)

        self.br.select_form(id="login_form")

        self.br.form['authuser'] = username
        self.br.form['password'] = password
        response = self.br.submit()

        if "        Sorry, we don't recognize that email or password. Please try again!    " in response.read().decode('utf-8'):
            print('unsuccessful')
        else:
            print('successful')
            self.__loggedIn = True
    

    def logout(self):
        if self.__loggedIn == True:
            self.br.open(self.__logout_url)
            self.driver.close()
            print('logged out')
        else:
            print('you arent logged in')


    def place_offer(self, ad_url, offer):
        if self.__loggedIn is not True:
            print('You need to be logged in to place an offer')
            return

        self.br.open(ad_url)

        self.br.select_form(predicate=lambda f: f.attrs.get('id', None) == 'make_offer_form')
       
        self.br.form['offer'] = offer
        resz = self.br.submit()
        print(resz.read().decode('utf-8'))

        print('complete')


    def comment_on_ad(self):
        print('void')


    def leave_feedback(self):
        print('void')

    
    def download_ad_images(self):
        print('void')


    def full_ad_info(self):
        print('void')


    def newest_ad(self):
        print('void')


    def get_ad_panel(self):
        soup = self.__bsoup()
        panels = soup.find_all('div', class_='sr-grid-cell quick-peek-container')
        ad = []
        
        for panel in panels:
            ad.append(
                ProductInfo(
                    panel.select(self.__price_tag)[0].text.strip(),
                    panel.select(self.__title_tag)[0].text.strip(), 
                    panel.select(self.__area_Tag)[0].text.strip(), 
                    panel.select(self.__county_tag)[1].text.strip(), 
                    panel.select(self.__category_tag)[0]['href'].split('/')[2:-4], 
                    f"""https://adverts.ie{panel.select(self.__url_tag)[0]['href']}"""
                            )
                    )

        return ad

    
    def __init_browser(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        return webdriver.Chrome(executable_path="./AdvertsAPI/chromedriver.exe", options=options)


    def __bsoup(self):
        return bs.BeautifulSoup(self.__get(), 'html.parser')


    def __get(self, url=None):
        if url is None:
            url = self.url
            
        return requests.get(url).text


    def __generate_url(self):
        return f"{self.__base_url}{f'{self.category}/' if self.category != None else ''}{f'county-{self.county}/' if self.county != None else ''}{f'price_{self.min_price}-{self.max_price}/' if self.max_price > self.min_price else f'price_{self.min_price}/'}{self.view}/page-1/"
