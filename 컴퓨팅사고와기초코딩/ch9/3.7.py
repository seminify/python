from tkinter import *


def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imageLable.config(image=img)
    imageLable.image = img


window = Tk()
photo = PhotoImage(file='minari.gif')
imageLable = Label(window, image=photo)
imageLable.pack()
inputBox = Entry(window)
inputBox.pack()
button = Button(window, text='그림읽기', command=change_img)
button.pack()
window.mainloop()
