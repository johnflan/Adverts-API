class ProductInfo:
    def __init__(self, price, title, area, county, category, url):
        super().__init__()
        self.__price = price
        self.__title = title
        self.__area = area
        self.__county = county
        self.__category = category
        self.__url = url
    
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