import turtle

t = turtle.Turtle()
t.shape('turtle')
color_list = ['yellow', 'red', 'blue', 'green']
for i in color_list:
    t.fillcolor(i)
    t.begin_fill()
    for i in range(6):
        t.forward(100)
        t.right(60)
    t.end_fill()
    t.forward(50)
