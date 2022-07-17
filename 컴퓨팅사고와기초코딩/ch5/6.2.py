import turtle

t = turtle.Turtle()
t.shape('turtle')
color_list = []
radius = int(input('원의 반지름은 ? '))
i = 0
while i < 4:
    color = input('색상 #%s을 입력하시오: ' % (i + 1))
    color_list.append(color)
    i = i + 1
i = 0
while i < 4:
    t.pendown()
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.forward(radius * 2)
    i = i + 1
