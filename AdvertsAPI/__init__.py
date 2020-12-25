import http.cookiejar

import bs4 as bs
import mechanize
import requests
import os

from AdvertsAPI.product_info import ProductInfo
from AdvertsAPI.ad_info import AdInfo

class AdvertsAPI:

    __adverts_url = 'https://www.adverts.ie/'
    __base_url = 'https://www.adverts.ie/for-sale/'
    __base_offer_url = 'https://www.adverts.ie/offer.php?'
    __base_withdraw_url = 'https://www.adverts.ie/withdrawoffer.php?action=withdraw'
    __query_url = 'https://www.adverts.ie/for-sale/q_'

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
        self.driver = None

    
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
            print('logged out')
        else:
            print('you arent logged in')


    def place_offer(self, ad_url, offer):
        if self.__loggedIn is not True:
            print('You need to be logged in to place an offer')
            return
        
        offer_url = self.__generate_offer_url(ad_url, offer)
        self.br.open(offer_url)

        self.br.select_form(nr=0)
        self.br.submit()
    

    def withdraw_offer(self, ad_url):
        if self.__loggedIn is not True:
            print('You need to be logged in to withdraw an offer')
            return
        
        myurl = self.__generate_withdraw_url(ad_url)

        self.br.open(ad_url)

        try:
            self.br.submit()
        except:
            print('You dont have any offers')


    def search(self, query):
       return self.get_ad_panel(f"""{self.__query_url}{query.replace(' ', '+')}""")
        

    def full_ad_info(self, ad_url):
        info = self.__bsoup(ad_url)
        
        return AdInfo(
            info.findAll("h1", {"class": "page_heading"})[0].text.strip(),
            info.findAll("span", {"class": "ad_view_info_cell"})[0].text.strip(),
            info.findAll("a", {"class": "inverted sellername"})[0].text.strip(),
            info.findAll("span", {"class": "positive"})[0].text.strip(),
            info.findAll("span", {"class": "negative"})[0].text.strip(),
            info.findAll("dd", {"class": "ad_view_info_cell"})[2].text.strip(),
            info.findAll("dd", {"class": "ad_view_info_cell"})[3].text.strip(),
            info.findAll("dd", {"class": "ad_view_info_cell"})[4].text.strip(),
            info.findAll("div", {"class": "main-description"})[0].text.strip()
        )


    def get_ad_panel(self, url=None):
        if url is None:
            soup = self.__bsoup()
        else:
            soup = self.__bsoup(url)
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

    
    def __generate_withdraw_url(self, ad_url):
        self.br.open(ad_url)
        s = bs.BeautifulSoup(self.br.response().read(), 'html.parser')

        try:
            comment_id = s.findAll("span", {"class": "sprite-btn withdraw-btn offer"})[0].attrs['data-comment-id']
        except:
            comment_id = None

        return f"""{self.__base_withdraw_url}&comment_id={comment_id}&modal_parent_uri={'%2F'.join(ad_url.replace(self.__adverts_url, '').split('/')[:-1])}"""
    

    def __generate_offer_url(self, ad_url, offer):
        return f"""{self.__base_offer_url}item_id={ad_url.split('/').pop()}&offer={str(offer)}&modal_parent_uri={'%2F'.join(ad_url.replace(self.__adverts_url, '').split('/')[:-1])}"""


    def __bsoup(self, soup_url=None):
        return bs.BeautifulSoup(self.__get(soup_url), 'html.parser')


    def __get(self, url=None):
        if url is None:
            url = self.url
            
        return requests.get(url).text


    def __generate_url(self):
        return f"{self.__base_url}{f'{self.category}/' if self.category != None else ''}{f'county-{self.county}/' if self.county != None else ''}{f'price_{self.min_price}-{self.max_price}/' if self.max_price > self.min_price else f'price_{self.min_price}/'}{self.view}/page-1/"
