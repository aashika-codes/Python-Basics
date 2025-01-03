test_dict={'codingal':4, 'is':2, 'best':2,'for':2, 'coding':1}
print("the original dictionary is", str(test_dict))
K=2
result=0
for key in test_dict:
    if test_dict[key]==K:
        result=result+1
print("frequency of K is", str(result))