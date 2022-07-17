import turtle

t = turtle.Turtle()


def square(length):
    for i in range(4):
        t.pendown()
        for j in range(4):
            t.forward(length)
            t.right(90)
        t.penup()
        t.forward(length * 2)


square(100)
