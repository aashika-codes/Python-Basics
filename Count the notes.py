amt=int(input("enter the amount of money"))
num_100=amt//100
rem_100=amt%100
num_50=rem_100//50
rem_50=rem_100%50
num_10=rem_50//10
print("the number of notes of 100 are ",num_100)
print("the number of notes of 50 are ",num_50)
print("the number of notes of 10 are ",num_10)