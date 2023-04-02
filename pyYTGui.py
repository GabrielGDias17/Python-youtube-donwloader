import pytube
from tkinter import Tk
from tkinter import *
import os
import PIL
import subprocess
import threading
from tkinter import messagebox, filedialog
from pytube import YouTube
import tkinter as tk




def widgets():
     label1= Label(text = "Please select one of the options").place(x = 10,y = 10)
     label2= Label(text = "Download-1 = Highest Resolution").place(x = 10,y = 30)
     label3= Label(text = "Download-2 = Lowest Resolution").place(x = 10,y = 50)
     label4= Label(text = "Download-3 = Audio Only").place(x = 10,y = 70)
     label5 = Label(text="Destination: ").place(x=1,y=130)
     label6 = Label(text="Enter  URL: ").place(x=1,y=150)
     # this is the entry box Enter  URL: 
     root.linkText = Entry(root,width=50,textvariable=video_Link).place(x = 100,y = 150)
     root.destinationText = Entry(root,width=50,textvariable=download_Path).place(x=100,y=130)
     #this a button
     button1 = Button(root,command=Download1, text = 'Download-1',relief=GROOVE).place(x = 10,y = 200)
     button3 = Button(root,command=Download2, text = 'Download-2',relief=GROOVE).place(x = 10,y = 250)
     button4 = Button(root,command=Download3, text = 'Download-3',relief=GROOVE).place(x = 10,y = 300)
     button4 = Button(root,command= Browse, text = 'Choose Path',relief=GROOVE).place(x = 140,y = 250)

#


def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)


def Download1():
    #  getting user-input Youtube Link
    Youtube_link = video_Link.get()
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)
    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.get_highest_resolution()
    # Downloading the video to destination
    # directory
    videoStream.download(download_Folder)
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_Folder)
 
def Download2():
    # getting user-input Youtube Link
    Youtube_link = video_Link.get()
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)
    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.get_lowest_resolution()
    # Downloading the video to destination
    # directory
    videoStream.download(download_Folder)
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_Folder)

def Download3():
    #  getting user-input Youtube Link
    Youtube_link = video_Link.get()
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)
    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.get_audio_only()
    # Downloading the video to destination
    # directory
    videoStream.download(download_Folder)
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_Folder) 
 



# this is the main window
root = tk.Tk()
# this is to save a string


#this is the title of the app
root.title("YouTube Downloader")
#getting screen width and height of display
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#this the geometry function that set the size of the window
root.geometry("%dx%d" % (width, height))
# adding back ground picture
bgimg= PhotoImage(file = "202101_Rat.png")
limg= Label(root, i=bgimg)
limg.pack()

video_Link = StringVar()
download_Path = StringVar()
widgets()



root.mainloop()

