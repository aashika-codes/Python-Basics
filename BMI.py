w=int(input("Enter weight in kgs\t"))
h=int(input("Enter height in m\t"))
BMI=w/(h*h)
if BMI<18.5:
    print("you are underweight")
elif BMI>=18.5 and BMI<25:
    print("You are healthy")
elif BMI>=25 and BMI<=30:
    print("you are overweight")
else:
    print("you are underweight")
