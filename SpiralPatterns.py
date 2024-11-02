import turtle
s= turtle.Screen()
t=turtle.Turtle()
s.bgcolor("blue")
t.pencolor("green")
t.pensize(5)
t.shape("turtle")
a=0
for i in range(100):
    t.fd(a)
    t.rt(90)
    a=a+10
turtle.done()