med=input("Do you have any medical issues?(y/n)")
if(med=="y"):
    print("You are allowed")
else:
    attend=input("Is your attendance above 75?(y/n)")
    if(attend=="y"):
        print("You are allowed")
    else:
        print("You are not allowed")