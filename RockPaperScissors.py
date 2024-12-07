import random
while True:
    User_Input=input(print("Choose an option:(Rock , paper , scissor)"))
    Possible_actions=["Rock" , "Paper" , "Scissors"]
    Computer_choice=random.choice(Possible_actions)
    print(f"\n you chose {User_Input},computer chose {Computer_choice}\n")
    if User_Input==Computer_choice:
        print("Both players selected {User_Input}. It is a tie.")
    elif User_Input=="Rock":
      if Computer_choice=="Scissors":
        print("Rock smashed the scissors, you win!")
      else:
        print("Paper covers rock so you lose!")
    elif User_Input=="Paper":
      if Computer_choice=="Scissors":
        print("Scissors cut the paper so you lose!")
      else:
        print("Rock smashed the scissors, you win!")
    elif User_Input=="Paper":
      if Computer_choice=="Rock":
        print("Paper covered the rock so you win!")
      else:
        print("Scissors cut the paper so you lose!")
    Play_Again=input("Play again? (Y/N)")
    if Play_Again != "Y":
        break
    