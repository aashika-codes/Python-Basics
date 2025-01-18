class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("Blue",22)
woo=parrot("Woo",13)
print("Blue is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))