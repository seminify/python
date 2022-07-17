import turtle

t = turtle.Turtle()
t.shape('turtle')


def circle_color(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


circle_color(100, 'red')
