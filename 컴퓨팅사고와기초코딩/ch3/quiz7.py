import turtle

t = turtle.Turtle()
t.shape('turtle')
size = int(input('집의 크기는 얼마로 할까요? '))
lista = []
color = input('벽면 색상을 입력하시오: ')
lista.append(color)
color = input('지붕 색상을 입력하시오: ')
lista.append(color)
color = input('창문 색상을 입력하시오: ')
lista.append(color)
t.fillcolor(lista[0])
t.begin_fill()
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.end_fill()
t.fillcolor(lista[1])
t.begin_fill()
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.end_fill()
t.up()
t.goto(size / 4, -(size / 4))
t.down()
t.fillcolor(lista[2])
t.begin_fill()
t.forward(size / 2)
t.right(90)
t.forward(size / 2)
t.right(90)
t.forward(size / 2)
t.right(90)
t.forward(size / 2)
t.end_fill()
