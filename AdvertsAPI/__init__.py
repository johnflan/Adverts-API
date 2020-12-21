import http.cookiejar

import bs4 as bs
import mechanize
import requests
import os

from AdvertsAPI.product_info import ProductInfo
from selenium import webdriver
from time import sleep

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
        self.driver = None

    
    def login(self, username, password):
        self.driver = self.__init_browser()

        self.driver.get(self.__login_url)
        privacy_agree_all = self.driver.find_element_by_xpath("//*[@id='js-cookie-modal-level-one']/div/main/div/button[2]")
        privacy_agree_all.click()

        username_input = self.driver.find_element_by_xpath("//*[@id='email']")
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_xpath("//*[@id='password']")
        password_input.send_keys(password)

        submit_login = self.driver.find_element_by_xpath("//*[@id='login_form']/div[4]/input")
        submit_login.click()

        try:
            x = self.driver.find_element_by_xpath("//*[@id='profile_details']/dl/dt[2]")
            self.__loggedIn = True
            print('Successfully logged in')
        except:
            print('Invalid username or password')
    

    def logout(self):
        if self.__loggedIn == True:
            self.driver.get(self.__logout_url)
            self.driver.quit()
            print('logged out')
        else:
            print('you arent logged in')


    def place_offer(self, ad_url, offer):
        if self.__loggedIn is not True:
            print('You need to be logged in to place an offer')
            return
        
        self.driver.get(ad_url)
        offer_input1 = self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div[2]/div[3]/div[2]/span[2]/form/input[1]").send_keys(str(offer))

        self.driver.find_element_by_xpath("//*[@id='new_offer_btn']").click()

        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/form/div[3]/input").click()


    def comment_on_ad(self, ad_url, comment):
        if self.__loggedIn is not True:
            print('You need to be logged in to comment on ad')
            return


    def leave_feedback(self, ad_url, message):
        if self.__loggedIn is not True:
            print('You need to be logged in to leave feedback')
            return

    
    def download_ad_images(self):
        print('void')


    def full_ad_info(self, ad_url):
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
        # options.headless = True
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
