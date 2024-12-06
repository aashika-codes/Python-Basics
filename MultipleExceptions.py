try:
    num1 , num2= eval(input("Enter two numbers seperated by a comma"))
    print("the two numbers are" , num1, num2)
    result= num1 / num2 
    print("the result is" , result)
except ZeroDivisionError:
    print("The division by zero is an error")
except SyntaxError:
    print("Comma is missing")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("execute the code no matter what")