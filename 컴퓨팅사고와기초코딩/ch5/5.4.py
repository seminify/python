import turtle

t = turtle.Turtle()
for count in range(6):
    t.circle(100 + 10 * count)
    t.left(360 / 6)
