num=int(input("Enter the Number\t"))
def f_cube(num):
    c=num**3
    print(f"the cube of {num} is {c}")
def div(num):
    if num%3==0:
        f_cube(num)
    else:
        print("The number is not divisible by 3")
div(num)