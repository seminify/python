import turtle

t = turtle.Turtle()


def boxes(length, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()


def roofs(length, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()


def moves(xn, yn):
    t.penup()
    t.goto(xn, yn)
    t.pendown()


moves(0, 100)
boxes(100, 'green')
moves(25, 75)
boxes(50, 'white')
moves(0, 100)
roofs(100, 'blue')
