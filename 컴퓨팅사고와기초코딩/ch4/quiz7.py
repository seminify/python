import turtle

t = turtle.Turtle()
t.shape('turtle')
s = turtle.textinput('', '도형을 입력하시오:')
if s == '사각형':
    s = turtle.textinput('', '가로')
    w = int(s)
    s = turtle.textinput('', '세로')
    h = int(s)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
elif s == '삼각형':
    s = turtle.textinput('', '한변의 길이:')
    l = int(s)
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
    t.forward(l)
else:
    s = turtle.textinput('', '반지름:')
    l = int(s)
    t.circle(l)
