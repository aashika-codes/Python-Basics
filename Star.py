import turtle
t=turtle.Turtle()
s=turtle.Screen()
t.pencolor("green")
s.bgcolor("blue")
t.shape("turtle")
t.pensize(5)
for i in range(3):
    t.fd(200)
    t.lt(120)
t.lt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
for i in range(3):
    t.fd(200)
    t.rt(120)
turtle.done()
