class ProductInfo:
    def __init__(self, price, title, area, county, category, url, advert_id):
        super().__init__()
        self.__price = price
        self.__title = title
        self.__area = area
        self.__county = county
        self.__category = category
        self.__url = url
        self.__advert_id = advert_id
    
    @property
    def price(self):
        return self.__price

    @property
    def title(self):
        return self.__title

    @property
    def area(self):
        return self.__area

    @property
    def county(self):
        return self.__county

    @property
    def category(self):
        return self.__category

    @property
    def url(self):
        return self.__url
    
    @property
    def advert_id(self):
        return self.__advert_id