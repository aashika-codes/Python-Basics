valid = False
try:
    n=int(input("Enter a number"))
    while n%2==0:
        print("Bye")
    valid = True
except ValueError:
    print("Invalid")