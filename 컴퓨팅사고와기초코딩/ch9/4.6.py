from tkinter import *
import turtle

t = turtle.Turtle()
t.shape('turtle')


def open():
    pass


def quit():
    window.quit()


def sums():
    value = int(e1.get())
    hap = 0
    for i in range(1, value + 1):
        hap += i
    e2.insert(0, str(hap))


def factorials():
    value = int(e1.get())
    result = 1
    for i in range(1, value + 1):
        result *= i
    e2.insert(0, str(result))


def circles():
    t.fillcolor('red')
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def quadrilateral():
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


def triangles():
    t.fillcolor('green')
    t.begin_fill()
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()


window = Tk()
menubar = Menu(window)
filemenu = Menu(menubar)
summenu = Menu(menubar)
summenu2 = Menu(menubar)
menubar.add_cascade(label='파일', menu=filemenu)
filemenu.add_command(label='열가', command=open)
filemenu.add_command(label='종료', command=quit)
menubar.add_cascade(label='합/곱', menu=summenu)
summenu.add_command(label='정수합', command=sums)
summenu.add_command(label='펙토리얼', command=factorials)
menubar.add_cascade(label='도형', menu=summenu2)
summenu2.add_command(label='원', command=circles)
summenu2.add_command(label='네모', command=quadrilateral)
summenu2.add_command(label='세모', command=triangles)
l1 = Label(window, text='값')
l2 = Label(window, text='결과')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
window.config(menu=menubar)
window.mainloop()
