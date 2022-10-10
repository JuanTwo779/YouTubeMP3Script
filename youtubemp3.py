from tkinter import * 
from tkinter import *
from tkinter import filedialog

screen = Tk()
title = screen.title('City Pop me up')
canvas = Canvas(screen, width=710, height=400)
canvas.pack()

logo_img = PhotoImage(file='wp7313089.png')

canvas.create_image(355, 200, image=logo_img)
#canvas.create_text(350, 250, text="Hello")

screen.mainloop()