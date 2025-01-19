class iostring():
    def __init__(self):
        self.str1=""
    def get_input(self):
        self.str1=input("enter string-")
    def print_upp(self):
        print("String in uppercase is-", self.str1.upper())
str1= iostring()
str1.get_input()
str1.print_upp()
