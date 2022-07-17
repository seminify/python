import turtle

t = turtle.Turtle()
t.shape('turtle')
color_list = ['yellow', 'red', 'blue', 'green']
for i in color_list:
    t.fillcolor(i)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.forward(50)
