from tkinter import *

root = Tk()
root.geometry("655x333")

f1 = Frame(root,bg="firebrick",borderwidth=6,relief="groove",padx=26,pady=26)

f2 = Frame(root,borderwidth=9,bg="salmon",relief="sunken",)

l1 = Label(f1,text="Welcome to Tkinter Project")
l1.pack(pady=42,padx=24)

l2 = Label(f2,text="Welcome to sublime text",font="Helvetica 16 bold",fg="orange",pady=30,bg="navyblue")

l2.pack(pady=34)

f1.pack(side="left",fill=Y)
f2.pack(side="top",fill="x")
root.mainloop()