class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "ob1 and ob2 are equal"
        else:
            return "ob1 and ob2 are not equal"
ob1=A(99)
ob2=A(43)
print("Passed Values is:-",ob1.a,ob2.a)
print(ob1<ob2)