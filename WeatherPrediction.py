weather=(0,1,0,1,0,1,0,1,1,0)
sunny=0
rainy=0
for i in range(0,10):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if(sunny>rainy):
    print("weather is good")
else:
    print("weather is bad")