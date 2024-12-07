import random 
playing = True
number=str(random.randint(10,20))
print("I will generate a number for 10 to 20 and you have to guess the number, one digit at a time")
print("The game will end when you get 1 hero!")
while playing:
    guess=input("Give me your best guess")
    if number==guess:
        print("You win the game!")
        print("The number was", number)
    else:
        print("Try again!")