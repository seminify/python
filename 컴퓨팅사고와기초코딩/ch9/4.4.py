from tkinter import *
import turtle

t = turtle.Turtle()
t.shape('turtle')


def open():
    pass


def quit():
    window.quit()


def circles():
    t.fillcolor('red')
    t.begin_fill()
    t.circle(50)
    t.end_fill()


window = Tk()
menubar = Menu(window)
filemenu = Menu(menubar)
summenu = Menu(menubar)
menubar.add_cascade(label='파일', menu=filemenu)
filemenu.add_command(label='열가', command=open)
filemenu.add_command(label='종료', command=quit)
menubar.add_cascade(label='도형', menu=summenu)
summenu.add_command(label='원', command=circles)
window.config(menu=menubar)
window.mainloop()
