from tkinter import *

root = Tk()
root.geometry("655x333")
root.title("Grids in Tkinter with Harry bhai")

def getVals():
    print(f"The value of username is {user_val.get()}")
    print(f"The value of password is {password_val.get()}")

    with open("userdata.txt","a") as f:
        f.write("The user data is as follows \n")
        f.write(f"username: {user_val.get()}\n")
        f.write(f"Password: {password_val.get()}\n")


username = Label(root,text="Enter your username",font="helvetica 19 bold",pady=20)
password = Label(root,text="Enter your password",font="helvetica 19 bold",pady=20)

username.grid()
password.grid(row=1)

# Variable classes in Tkinter

# BooleanVar,StringVar,DoubleVar,IntVar

user_val = StringVar()
password_val = StringVar()

user_entry = Entry(root,textvariable=user_val)

pass_entry = Entry(root,textvariable=password_val)

user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)

Button(text="Submit",command=getVals,pady=10,padx=10).grid(row=2,column=1)
root.mainloop()