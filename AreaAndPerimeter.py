class circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return 2*3.14*self.radius
obj=circle(7)
print(obj.area())
print(obj.perimeter())