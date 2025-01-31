class comp:
    def __init__(self):
        self.__maxprice=230
    def sell(self):
        print("Selling price is-",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
c=comp()
c.sell()
c.__maxprice=344
c.sell()
c.setmaxprice(344)
c.sell()