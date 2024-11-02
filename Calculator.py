def add(a,b):
    print(f"The sum of {a} and {b} is {a+b}")
def sub(a,b):
    print(f"The substraction of {a} and {b} is {a-b}")
def mul(a,b):
    print(f"The multiplication of {a} and {b} is {a*b}")
def div(a,b):
    print(f"The division of {a} and {b} is {a/b}")
print('''Calculator:-
      1.Add
      2.Substract
      3.Multipy
      4.Divide 
      Enter Your Choice''')
ch=input()
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if ch=="1":
    add(a,b)
elif ch=="2":
    sub(a,b)
elif ch=="3":
    mul(a,b)
elif ch=="4":
    div(a,b)
else:
    print("Invalid Choice")