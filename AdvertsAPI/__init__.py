import bs4 as bs
import requests
from AdvertsAPI.product_info import ProductInfo
# import mechanize          ## FOR LOGINS
# import http.cookiejar     ## FOR LOGINS

class AdvertsAPI:
    def __init__(self, category=None, county=None, min_price=0, max_price=0, view='grid_view', keywords=None):
        super().__init__()
        self.category = category
        self.county = county
        self.min_price = min_price
        self.max_price = max_price
        self.view = view
        self.keywords = keywords
        self.url = self.generate_url()
        

    def get_ad_panel(self):
        soup = self.ads()
        panels = soup.find_all('div', class_='sr-grid-cell quick-peek-container')
        ad = []
        
        for panel in panels:
            ad.append(
                ProductInfo(
                    panel.select("div[class='price'] > a")[0].text.strip(),
                    panel.select("div[class='title'] > a")[0].text.strip(), 
                    panel.select("div[class='location'] > a")[0].text.strip(), 
                    panel.select("div[class='location'] > a")[1].text.strip(), 
                    panel.select("div[class='location'] > a")[0]['href'].split('/')[2:-4], 
                    f"""https://adverts.ie{panel.select("div[class='price'] > a")[0]['href']}"""
                            )
                    )
            # ad.append({
            #     'price': panel.select("div[class='price'] > a")[0].text.strip(),
            #     'title': panel.select("div[class='price'] > a")[0].text.strip(),
            #     'area': panel.select("div[class='location'] > a")[0].text.strip(),
            #     'county': panel.select("div[class='location'] > a")[1].text.strip(),
            #     'category': panel.select("div[class='location'] > a")[0]['href'].split('/')[2:-4],
            #     'url': f"""https://adverts.ie{panel.select("div[class='price'] > a")[0]['href']}"""
            # })
                
        return ad
                

    def ads(self):
        return bs.BeautifulSoup(self.get(), 'html.parser')


    def get(self):
        return requests.get(self.url).text


    def generate_url(self):
        return f"https://www.adverts.ie/for-sale/{f'{self.category}/' if self.category != None else ''}{f'county-{self.county}/' if self.county != None else ''}{f'price_{self.min_price}-{self.max_price}/' if self.max_price > self.min_price else f'price_{self.min_price}/'}{self.view}/page-1/"
