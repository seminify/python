import turtle

t = turtle.Turtle()
t.shape('turtle')


def square(lenght):
    for i in range(4):
        t.forward(lenght)
        t.left(90)


def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('green')
    square(50)
    t.end_fill()


s = turtle.Screen()
s.onscreenclick(drawit)
