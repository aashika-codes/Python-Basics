num= int(input("enter the number\t"))
def fact(num):
    if num>=1:
        return num * fact(num-1)
    else:
        return 1
answer=fact(num)
print(answer)