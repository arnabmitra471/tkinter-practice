from tkinter import *

root = Tk()

root.geometry("644x334")

def get_data(event):
    print("The button 1 of the mouse was clicked")
    print("Getting the data")

btn = Button(root,text="Click here !!")

btn.pack()

btn.bind("<Button-1>",get_data)
btn.bind("<Double-1>",quit)


root.mainloop()