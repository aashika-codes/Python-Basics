lower=int(input("Enter the Lower range"))
higher=int(input("Enter the higher range"))
print("The prime numbers between ",lower," and ",higher, "are")
for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:print(num)