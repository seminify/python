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


color_list = []
radius = int(input('원의 반지름은 ? '))
i = 0
while i < 4:
    color = input('색상 #%s을 입력하시오: ' % (i + 1))
    color_list.append(color)
    i = i + 1
i = 0
while i < 4:
    circle_color(radius, color_list[i])
    if i != 3:
        moves(radius * 2 * (i + 1), 0)
    i = i + 1
