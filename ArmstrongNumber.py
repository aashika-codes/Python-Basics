n=153
print("hi")
q=n
sum=0
while q>=0:
    r=q%10
    f=r*r*r
    sum=sum+f
    q=q//10
print(sum)