
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os

top = Tk()
top.minsize(width=400, height=450)
img = ImageTk.PhotoImage(Image.open("Test.png"))
panel = Label(top, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


#butt stuff, coding for buttons goes in corresponding functions below
def qui():
    top.destroy()

def song1():
    tkinter.messagebox.showinfo("Song Info", "Playing Song1")
def song2():
    tkinter.messagebox.showinfo("Song Info", "Playing Song2")
def song3():
    tkinter.messagebox.showinfo("Song Info", "Playing Song3")
def song4():
    tkinter.messagebox.showinfo("Song Info", "Playing Song4")
def song5():
    tkinter.messagebox.showinfo("8===SongInfo===D", "Playing Song5")
# Code to add widgets will go here...
buttSONG1 = tkinter.Button (top, activebackground='red', text = "Enter_Song_1_Here", command=song1)
buttSONG2 = tkinter.Button (top, activebackground='blue', text = "Enter_Song_2_Here", command=song2)
buttSONG3 = tkinter.Button (top, activebackground='green', text = "Enter_Song_3_Here", command=song3)
buttSONG4 = tkinter.Button (top, activebackground='yellow', text = "Enter_Song_4_Here", command=song4)
buttSONG5 = tkinter.Button (top, activebackground='pink', text = "Enter_Song_5_Here", command=song5)
buttEXIT = tkinter.Button (top, text = "Exit", command=qui)
buttSONG1.pack()
buttSONG2.pack()
buttSONG3.pack()
buttSONG4.pack()
buttSONG5.pack()
buttEXIT.pack()
top.mainloop()
