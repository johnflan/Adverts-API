import bs4 as bs
import requests
# import mechanize          ## FOR LOGINS
# import http.cookiejar     ## FOR LOGINS

class Adverts:
    def __init__(self, category=None, county=None, min_price=0, max_price=0, view='grid_view', keywords=None):
        super().__init__()
        self.category = category
        self.county = county
        self.min_price = min_price
        self.max_price = max_price
        self.view = view
        self.keywords = keywords
        self.url = 'https://google.com'
        self.generateUrl()
    # def get_items(self):

    def get(self):
        return requests.get(self.url).text


    def generateUrl(self):
        print(f"https://www.adverts.ie/for-sale/{f'{self.category}/' if self.category != None else ''}{f'{self.county}/' if self.county != None else ''}{f''}{self.view}/page-1/")


'''
categories:
    Antiques-Collectables
    Art-Crafts
    Baby-Nursery
    Books-Magazines
    Business-Office
    Cars-Motorbikes-Boats
    Clothes-Shoes-Accessories
    Computers
    Consoles-Games
    Crazy-Random-Stuff
    DIY-Renovation
    DVD-CD-Movies
    Electronics
    Farming
    Health-Beauty
    Home-Garden
    Jewellery-Watches
    Jobs
    Mobile-Phones-Accessories
    Music-Instruments-Equipment
    Pets
    Photography
    Services
    Sports-Fitness
    Tickets
    Toys-Games
    Wedding
'''