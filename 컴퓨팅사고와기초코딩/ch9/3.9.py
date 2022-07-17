from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()
im = Image.open('lenna.png')
out = im.rotate(45)
tk_img = ImageTk.PhotoImage(out)
canvas.create_image(250, 250, image=tk_img)
window.mainloop()
