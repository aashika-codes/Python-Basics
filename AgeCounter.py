try:
    age=int(input("Enter your age"))
    print("The age entered by the user is", age)
except ValueError:
    print("age entered is not valid")
