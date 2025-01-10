list1={4,6,7}
list2={'a','v','g'}
list3=list(zip(list1,list2))
print(list3)
 
l1=[20,60,40,30]
l2=[400,300,200,100]
for x,y in zip(l1,l2[::-1]):
    print(x,y)

stocks=['infosys','tcs','nifty','wipro']
prices=[3466,2967,3211,4367]
newdict={stocks:prices for stocks,prices in zip(stocks,prices)}
print('\n{}'.format(newdict))