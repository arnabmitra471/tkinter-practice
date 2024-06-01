from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Sliders in Tkinter")


def get_dollars():
    tmsg.showinfo("success",f"We have credited {slider2.get()} dollars in your bank account")
    print(f"We have credited {slider2.get()} dollars in your bank account")
# slider1 = Scale(root,from_=0,to=100,bg="Salmon")

# slider1.pack()
l1 = Label(root,fg="teal",bg="cornflower blue",text="How many dollars do you want ??",font=("Lucida",19,"bold"))

l1.pack(side="top",padx=20)
slider2 = Scale(root,from_=0,to=200,bg="grey",orient="horizontal",tickinterval=50)
slider2.set(24)

slider2.pack()

Button(root,text="Get dollars",command=get_dollars,font=("Lucida",19,"bold"),pady=10).pack()

root.mainloop()