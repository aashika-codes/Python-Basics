print("""Choose a ride
      1.Car
      2.Bike""")
ride=int(input("Enter your choice \t"))
if(ride==1):
    print("""Choose a car
          1.Ferrari
          2.Mustang""")
    ch=int(input("Enter your choice\t"))
    if (ch==1):
        print("You have chosen a ferrari!")
    else:
        print("You have chosen a mustang!")
else:
        print("""Choose a bike
          1.Yamaha
          2.Royal Enfield""")
        ch=int(input("Enter your choice\t"))
        if (ch==1):
         print("You have chosen a Yamaha!")
        else:
         print("You have chosen a Royal enfield!")
