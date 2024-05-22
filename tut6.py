# Attributes of label and pack

from tkinter import *

root = Tk()

root.geometry("700x400")
root.title("My GUI with Harry")

'''
Important label options
text - adds the text to a label
bd - background
fg - foreground
font - sets the font
1. font=("comicsansms",20,"bold")
2. font="comicsansms 19 bold"
padx - padding on x axis
pady - padding on y axis

relief - border styling SUNKEN, RAISED, GROOVE and RIDGE
'''

'''
Attributes of pack

anchor = nw
side = top,bottom,left,right
fill
padx
pady

'''


username_label = Label(text="Enter your username",bg="red",fg="white",padx=13,pady=44,font="comicsansms 9 bold",borderwidth=4,relief=RIDGE)
username_label.pack(side="left",fill="y",padx=34,pady=34)
root.mainloop()