class ferrari():
    def abt(self):
        print("ferrari is a high end luxury car brand")
    def capacity(self):
        print("main capacity of ferrari is 2")
    def mileage(self):
        print("ferrari has mileage of 34")
class bmw():
    def abt(self):
        print("bmw is germand and luxury car brand")
    def capacity(self):
        print("max is 4 people")
    def mileage(self):
        print("mileage is 9")
objbmw=bmw()
objferrari=ferrari()
for car in (objbmw,objferrari):
    car.capacity()
    car.abt()
    car.mileage()