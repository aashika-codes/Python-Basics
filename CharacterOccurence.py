a=input("Enter the word\t")
char=input("Enter the character you want searched\t")
count=0
for i in a:
    if char==i:
        count=count+1
print(char,"has come", count, "times in", a)