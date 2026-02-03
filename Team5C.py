import turtle

def draw_book_rectangle(t):
    for i in range(2):
        t.forward(350)
        t.left(90)
        t.forward(300)
        t.left(90)

def draw_small_rectangle(t):
    for i in range(2):
        t.forward(240)
        t.right(90)
        t.forward(90)
        t.right(90)

def draw_b(t):
    t.forward(50)
    t.left(90)
    for i in range (3):
        t.forward(25)
        t.left(90)
    t.penup()
    t.forward(25)
    t.left(90)
    t.forward(40)
    t.pendown()

def draw_o(t):
    for i in range(4):
        t.forward(25)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()




t = turtle.Turtle()
t.right(180)
t.penup()
t.forward(200)
t.right(90)
t.forward(150)
t.right(180)
t.pendown()
draw_book_rectangle(t)
t.penup()
t.right(270)
t.forward(30)
t.right(90)
t.forward(30)
t.left(90)
t.pendown()
draw_small_rectangle(t)
t.penup()
t.forward(20)
t.right(90)
t.forward(10)
t.pendown()
draw_b(t)
draw_o(t)
draw_o(t)
turtle.done()


