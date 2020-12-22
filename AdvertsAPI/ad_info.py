class AdInfo:
    def __init__(self, title, price, seller, positive, negative, location, date_entered, ad_views, description):
        super().__init__()
        self.__title = title
        self.__price = price
        self.__seller = seller
        self.__positive = positive
        self.__negative = negative
        self.__location = location
        self.__date_entered = date_entered
        self.__ad_views = ad_views
        self.__description = description
    
    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @property
    def seller(self):
        return self.__seller

    @property
    def positive(self):
        return self.__positive

    @property
    def negative(self):
        return self.__negative

    @property
    def location(self):
        return self.__location

    @property
    def date_entered(self):
        return self.__date_entered

    @property
    def ad_views(self):
        return self.__ad_views

    @property
    def description(self):
        return self.__description