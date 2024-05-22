from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry("455x244")

image = Image.open("computer.jpg")
photo = ImageTk.PhotoImage(image)
username = Label(image=photo)
username.pack()
root.mainloop()