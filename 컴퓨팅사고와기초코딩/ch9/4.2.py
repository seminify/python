from tkinter import *


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


window = Tk()
menubar = Menu(window)
filemenu = Menu(menubar)
summenu = Menu(menubar)
menubar.add_cascade(label='파일', menu=filemenu)
filemenu.add_command(label='열기', command=open)
filemenu.add_command(label='종료', command=quit)
menubar.add_cascade(label='합/곱', menu=summenu)
summenu.add_command(label='정수합', command=sums)
summenu.add_command(label='펙토리얼')
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
