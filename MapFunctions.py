num1=[1,2,3]
num2=[8,9,5]
result=map(lambda x, y:x+y, num1, num2)
print("Addition of the two lists are")
print(list(result))
nums=[2,3,4,5,6]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("squares of the numbers in the list are")
print(square)