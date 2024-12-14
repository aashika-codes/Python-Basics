L=[6,3,9,1,4,7,11,10]
print("The original list is", L)
count=0
for i in L:
    count=count+i
average=count/len(L)
print("Sum=",count)
print("Average=",average)
L.sort()
print("Smallest element is",L[0])
print("Largest element is",L[-1])