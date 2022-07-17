from tkinter import *


def open():
    pass


def quit():
    window.quit()


window = Tk()
menubar = Menu(window)
filemenu = Menu(menubar)
menubar.add_cascade(label='파일', menu=filemenu)
filemenu.add_command(label='열기', command=open)
filemenu.add_command(label='종료', command=quit)
window.config(menu=menubar)
window.mainloop()
