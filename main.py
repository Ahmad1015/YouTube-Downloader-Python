# Import necessary libraries
from pytube import YouTube
from tkinter import *

# Create a Tkinter window
root = Tk()
root.geometry("650x400")

# Create a label for the application title
Label(root, text="Python Youtube downloader", font="Arial 12 bold", foreground='blue').grid(row=0, column=0)

# Create a label for instructions
message = Label(root, text="       Enter Youtube Link Below", foreground='red')
Youtube_Link = Label(root, text='Youtube Link', font="ar 10 bold")

message.grid(row=0, column=1)
Youtube_Link.grid(row=2, column=0)

# Create a variable to store the entered YouTube link
LinkValue = StringVar()

# Create an entry field for the user to input the YouTube link
LinkEntry = Entry(root, textvariable=LinkValue, width=30, font='ar 12 bold')

LinkEntry.grid(row=2, column=1, pady=15)

# Function to clear the entry field and display a cleared message
def ClearRecord():
    global message
    LinkValue.set("")
    message.grid_forget()
    message = Label(root, text="Cleared", foreground='Green', font='20')
    message.grid(row=0, column=1)

# Function to search and download the highest resolution stream of the provided YouTube link
def SearchRecord():
    youtubeObject = YouTube(LinkValue.get())
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Invalid Youtube Link")
    print("Download is completed successfully")

# Create buttons for clearing and searching
Button(text="CLEAR", command=ClearRecord, background='gray', foreground='blue', font='ar 10 bold').grid(row=7, column=0)
Button(text="SEARCH", command=SearchRecord, background='gray', foreground='blue', font='ar 10 bold').grid(row=11,
                                                                                                          column=2)
# Start the Tkinter main loop
root.mainloop()
