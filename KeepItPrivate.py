class myClass:
    __privar= 27;
    def __privatemethod(self):
        print("I am inside class myClass")
    def hello(self):
        print("Private Variable Value:",myClass.__privatemethod)
foo=myClass()
foo.hello()
foo.__privatemethod()