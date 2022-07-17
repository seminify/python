import tkinter as tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import pandas as pd

df = None


def open():
    global df
    fname = fd.askopenfilename()
    df = pd.read_excel(fname)


def quit():
    window.quit()


def line_plot():
    global df
    df.plot(kind='line', x='name', y='pets', color='red')
    plt.show()


def bar_plot():
    global df
    df.plot(kind='bar', x='name', y='age')
    plt.show()


def group_plot():
    global df
    df.groupby('city')['name'].nunique().plot(kind='bar')
    plt.show()


window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)
filemenu.add_command(label='열기', command=open)
filemenu.add_command(label='종료', command=quit)
ipmenu.add_command(label='라인차트', command=line_plot)
ipmenu.add_command(label='바차트', command=bar_plot)
ipmenu.add_command(label='그룹핑', command=group_plot)
menubar.add_cascade(label='파일', menu=filemenu)
menubar.add_cascade(label='그래픽 처리', menu=ipmenu)
window.config(menu=menubar)
window.mainloop()
