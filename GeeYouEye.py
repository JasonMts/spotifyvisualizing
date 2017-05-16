#library imports
from flickrscrape import getnouns, allnouns, getpictures, getbestwords, checknouns
from Spot.py import show_tracks, pause_spot, play_spot, next_spot, previous_spot, playlist_get
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import os
from threading import Timer
import time
top = Tk()

#call function that prepares all possible nouns
getnouns()

#initial allocation setup the 10 is hardcoded to allow up to 10 images
img = [0 for i in range(10)]
imgPanel = [0 for i in range(10)]

#loading default image
imgI = Image.open("default.png")
imgI = ImageTk.PhotoImage(imgI)
imgPanelI = Label(top, image = imgI)
imgPanelI.image = imgI
imgPanelI.grid(row=1, column=1, columnspan=10, rowspan=7)
songBox = Listbox(top)
songBox.grid(row=0, column=0, rowspan=7)
for item in ["Tunnel Vision", "Stairway to Heaven", "Dirt", "Fake Plastic Trees", "Through the Fire and Flames"]:
    songBox.insert(END, item)

#butt stuff, coding for buttons goes in corresponding functions below
def qui():
    top.destroy()
def confSong():
    tkinter.messagebox.showinfo("Song Info", str.lower(songBox.get(songBox.curselection())).replace(" ",""))
    #get pictures for that song
    lyrics = str.lower(songBox.get(songBox.curselection())).replace(" ","")
    getpictures(checknouns(getbestwords(lyrics + ".txt")))

    t1 = Timer(0, timeout0)
    t1.start()

def timeout0():
    #size needs to change based on amount of pictures
    size = 4
    looper = 0
    while (looper < size):
        img[looper] = Image.open("pic" + str(looper + 1) + ".jpg")
        img[looper] = img[looper].resize((200, 200), Image.ANTIALIAS)
        img[looper] = ImageTk.PhotoImage(img[looper])
        imgPanel[looper] = Label(top, image = img[looper])
        imgPanel[looper].image = img[looper]
        looper += 1
    timeout1(0, size)
#recursive function to display the pictures
def timeout1(track, limit):
    if (track != 0):
        imgPanel[track - 1].grid_forget()
    else:
        imgPanelI.grid_forget()
    imgPanel[track].grid(row=1, column=1, columnspan=10, rowspan=7)
    time.sleep(3)#this will need to be changed based on (size)/(song lenth)
    if (track < limit - 1):
        timeout1(track + 1, limit)
    else:
        tkinter.messagebox.showinfo("END", "Song Complete")


# Code to add widgets will go here...
t1 = Timer(0, timeout0)
buttConfirm = tkinter.Button (top, activebackground='green', text = "Confirm", command=confSong)
##################
#buttConfirm = tkinter.Button (top, activebackground='green', text = "Play", command=play_spot)
#buttConfirm = tkinter.Button (top, activebackground='green', text = "Pause", command=pause_spot)
#buttConfirm = tkinter.Button (top, activebackground='green', text = "Next", command=next_spot)
#buttConfirm = tkinter.Button (top, activebackground='green', text = "Previous", command=previous_spot)
#   This group of funcions are for controlling playback on Spotify, however at the current time, these functions do not properly send commands to the Spotify Web API, and are currently broken
#################
buttEXIT = tkinter.Button (top, text = "X", command=qui)
buttEXIT.grid(row=0, column=10)
buttConfirm.grid(row=7, column=0)
top.mainloop()


'''
img3 = Image.open("test2.png")
img3 = img3.resize((200, 200), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(img3)
img = Image.open("test1.png")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel1 = Label(top, image = img)
panel2 = Label(top, image = img4)
panel1.image = img
panel2.image = img4
panel1.grid(row=1, column=1, columnspan=10, rowspan=7)
def song1():
    tkinter.messagebox.showinfo("Song Info", "Playing Song1")
def song2():
    tkinter.messagebox.showinfo("Song Info", "Playing Song2")
def song3():
    tkinter.messagebox.showinfo("Song Info", "Playing Song3")
def song4():
    tkinter.messagebox.showinfo("Song Info", "Playing Song4")
def song5():
    tkinter.messagebox.showinfo("8=SongInfo=D", "Playing Song5")
buttSONG1.grid(row=0, column=0)
buttSONG2.grid(row=1, column=0)
buttSONG3.grid(row=2, column=0)
buttSONG4.grid(row=0, column=1)
buttSONG5.grid(row=1, column=1)
buttSONG1 = tkinter.Button (top, activebackground='red', text = "Enter_Song_1_Here", command=song1)
buttSONG2 = tkinter.Button (top, activebackground='blue', text = "Enter_Song_2_Here", command=song2)
buttSONG3 = tkinter.Button (top, activebackground='green', text = "Enter_Song_3_Here", command=song3)
buttSONG4 = tkinter.Button (top, activebackground='yellow', text = "Enter_Song_4_Here", command=song4)
buttSONG5 = tkinter.Button (top, activebackground='pink', text = "Enter_Song_5_Here", command=song5)
    if (track == 1):
        panel1.grid_forget()
        panel2.grid(row=1, column=1, columnspan=10, rowspan=7)
        track = 0
    else:
        panel2.grid_forget()
        panel1.grid(row=1, column=1, columnspan=10, rowspan=7)
        track = 1
'''
