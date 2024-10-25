num= input("Enter the number")
if(len(num)%2==0):
    evn_l=len(num)//2
    p=int(num[evn_l-1])*int(num[evn_l])
    print(p)
else:
    odd_l= len(num)//2
    p=int(num[odd_l])
    print(p)