import turtle

t = turtle.Turtle()
t.width(3)
t.shape('turtle')
while True:
    command = input('명령을 입력하시오: ')
    if command == 'l':
        t.left(90)
        t.forward(100)
    if command == 'r':
        t.right(90)
        t.forward(100)
