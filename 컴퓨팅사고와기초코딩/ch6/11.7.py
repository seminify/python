import turtle

t = turtle.Turtle()
t.shape('turtle')


def circle_color(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def moves(xn, yn):
    t.penup()
    t.goto(xn, yn)
    t.pendown()


circle_color(100, 'red')
moves(200, 0)
circle_color(100, 'green')
