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


def house(xn, yn, length):
    moves(xn, yn + length)
    boxes(length, 'green')
    moves(xn + length / 4, yn + length * 3 / 4)
    boxes(length / 2, 'white')
    moves(xn, yn + length)
    roofs(length, 'blue')


house(0, 0, 100)
house(200, 200, 200)
house(-400, -400, 300)
