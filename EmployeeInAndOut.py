class employee:
    def __init__(self):
        print("Employee is created..")
    def __del__(self):
        print("Destructor called")
def create_obj():
        print("making object")
        obj=employee()
        print("function ends..")
print("Calling create_obj() function..")
obj=create_obj()
print("Program end")
