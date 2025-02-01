from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I walk and run")
class snake(animal):
    def move(self):
        print("i swiggle")
class dog(animal):
    def move(self):
        print("I walk on my four paws")
class lion(animal):
    def move(self):
        print("i roar and hunt preys")
hu=human()
hu.move()
sn=snake()
sn.move()
d=dog()
d.move()
li=lion()
li.move()