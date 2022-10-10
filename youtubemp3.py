from tkinter import * 
from tkinter import filedialog
from pytube import *

import shutil


#Function to select file path
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

#Function to download file
def download_file():
    #get user path
    get_link = link_field.get()
    user_path = path_label.cget("text")
    #Download
    screen.title('Downloading mp3 file...')
    mp3 = YouTube(get_link).streams.get_audio_only().download()
    shutil.move(mp3, user_path)
    screen.title('Download Complete!')

screen = Tk()
title = screen.title('City Pop Me Up')
canvas = Canvas(screen, width=710, height=400)
canvas.pack()


#image/background
logo_img = PhotoImage(file='wp7313089.png')
canvas.create_image(355, 200, image=logo_img)
#canvas.create_text(350, 250, text="Hello")

#link field
link_field = Entry(screen, width = 30)
link_label = Label(screen, text="Enter URL to Download: ", font=('Arial', 12), bg="white") 
#add to canvas
canvas.create_window(550, 150, window=link_label)
canvas.create_window(550, 180, window=link_field)

#Select Path for saving file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 12), bg="white")
select_btn = Button(screen, text="Select", command=select_path)
#Add to window
canvas.create_window(550, 210, window=path_label)
canvas.create_window(550, 250, window=select_btn)



#download buttons
download_btn = Button(screen, text="Download File", command=download_file)
#add to canvas
canvas.create_window(550, 300, window=download_btn)

screen.mainloop()