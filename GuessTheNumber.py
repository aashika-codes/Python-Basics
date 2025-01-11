import time
import random
num=random.randint(1,100)
def intro():
    print("May i ask you for your name?")
    global name
    name=input()
    print(name + ", we will be playing a game. I am thinking of a number between 1 and 100")
    if(num%2==0):
        x="even"
    else:
        x="odd"
    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead, Guess!")
def pick():
    gt=0
    while gt<6:
        time.sleep(.25)
        enter=input("guess:")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                gt=gt+1
                if gt<6:
                    if guess<num:
                        print("The guess of the number you have entered is too low")
                    if guess>num:
                        print("the guess of the number you have entered is too high")
                    if guess!=num:
                        time.sleep(.5)
                        print("try again!")
                    if guess==num:
                        break 
            if guess>100 and guess<1:
                print("That number is not in the range")
                time.sleep(.25)
                print("please enter a number between 1-100")
        except:
            print("I dont think that "+enter+"is a number. Sorry!")
    if guess==num:
        gt=str(gt)
        print("good job, {}! You guessed my number in {} guesses!".format(name,gt))
    if guess!=num:
        print("the number i was thinking was"+str(num))
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    intro()
    pick()
    print("Do you want to play again?")