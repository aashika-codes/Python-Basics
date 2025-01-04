import array as arr
array_num=arr.array('i',[1,4,6,3,8,6,0,6,2,6])
print("original array: " +str(array_num))
print("The number of times the number 6 has occured in the array:" +str(array_num.count(6)))
array_num.reverse()
print("the reversed order is:")
print(array_num)