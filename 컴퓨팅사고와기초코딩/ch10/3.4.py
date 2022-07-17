import random
import tkinter as tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import pandas as pd

infile = open('hangman.txt', 'r')
df = pd.read_excel('행맨.xlsx')


def quit():
    infile.close()
    window.quit()


def hangmantest():
    global df
    lines = infile.readlines()
    word = random.choice(lines).rstrip()
    solution = list(word)
    result = list('_' * len(word))
    print(result)
    turns = 10
    while turns > 0:
        guess = input('단어를 추측하세요: ')
        turns -= 1
        i = 0
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        print(result)
        if result == solution:
            print('성공입니다.')
            row = [{'단어': word, '성공실패': 1, '성공횟수': 10 - turns}]
            df = df.append(row, 'sort=False')
            writer = pd.ExcelWriter('행맨.xlsx', engine='openpyxl')
            df.to_excel(writer, index=False)
            writer.save()
            break
        print(turns, '번의 기회가 남았습니다\n')
        if turns <= 0:
            print('실패하였습니다.')
            row = [{'단어': word, '성공실패': 0, '성공횟수': 0}]
            df = df.append(row, 'sort=False')
            writer = pd.ExcelWriter('행맨.xlsx', engine='openpyxl')
            df.to_excel(writer, index=False)
            writer.save()
            break


def bar_plot():
    global df
    df.plot(kind='bar', x='단어', y='성공횟수')
    plt.show()


def group_plot():
    global df
    df.groupby('성공실패')['단어'].nunique().plot(kind='bar')
    plt.show()


window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)
filemenu.add_command(label='종료', command=quit)
ipmenu.add_command(label='수행', command=hangmantest)
ipmenu.add_command(label='바챠트', command=bar_plot)
ipmenu.add_command(label='성공실패', command=group_plot)
menubar.add_cascade(label='파일', menu=filemenu)
menubar.add_cascade(label='행맨수행결과', menu=ipmenu)
window.config(menu=menubar)
window.mainloop()
