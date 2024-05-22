from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry("600x500")
img = Image.open("computer.jpg")
img1 = Image.open("computer1.jpg")
img2 = Image.open("computer2.jpg")


photo1 = ImageTk.PhotoImage(img)
photo2 = ImageTk.PhotoImage(img1)
photo3 = ImageTk.PhotoImage(img2)

l1 = Label(image=photo1)
l2 = Label(image=photo2)
l3 = Label(image=photo3)


l1.pack()
l2.pack()
l3.pack()

root.mainloop()