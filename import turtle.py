import turtle

def mid_top():
    t.home()
    t.penup()
    t.left(90)
    t.forward(200)
    t.pendown()

def left_shield():
    mid_top()
    t.left(215)
    t.circle(150, 90)

def right_shield():
    t.penup()
    mid_top()
    t.right(215)
    t.pendown()
    t.circle(-150, 90)


def sheild():
    left_shield()
    right_shield()



screan = turtle.Screen()
t = turtle.Turtle()

sheild()
turtle.done()
