import random
class fruitquiz():
    def __init__(self):
        self.fruit={'apple':'red',
                    'peach':'pink',
                    'guava':'green',
                    'banana':'yellow'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruit.items()))
            print("What is the color of {}".format(fruit))
            useranswer=input()
            if(useranswer.lower()==color):
                print("correct answer!")
            else:
                print("wrong answer!")
            option=int(input("enter 0 if you want to play again, otherwise enter 1"))
            if(option):
                break
print("welcome to the fruit quiz!")
fq=fruitquiz()
fq.quiz()