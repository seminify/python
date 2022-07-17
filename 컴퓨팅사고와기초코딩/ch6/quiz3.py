import turtle

t = turtle.Turtle()


def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)


square(100)
