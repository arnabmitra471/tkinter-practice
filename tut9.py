from tkinter import *

root = Tk()
root.geometry("655x333")


def hello():
    print("Hello Tkinter Buttons")

def tell_name():
    print("My name is Arnab")

fr1 = Frame(root,borderwidth=4,relief="sunken",bg="olive")
fr1.pack(side="left",anchor="nw")

btn = Button(fr1,text="Print now",fg="white",bg="salmon",command=hello)
btn.pack(side="left",padx=24)

btn2 = Button(fr1,text="Tell me name now",fg="white",bg="salmon",command=tell_name)
btn2.pack(side="left",padx=24)

btn3 = Button(fr1,text="Click here",fg="white",bg="salmon")
btn3.pack(side="left",padx=24)

btn4 = Button(fr1,text="Click here",fg="white",bg="salmon")
btn4.pack(side="left",padx=24)
root.mainloop()