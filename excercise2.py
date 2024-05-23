import tkinter as tk

root = tk.Tk()

root.geometry("720x310")

root.minsize(300,200)

def good_morning():
    print("A very warm good morning to all of you present here")

def good_afternoon():
    print("Good afternoon folks")

def good_evening():
    print("Good evening folks")

def good_night():
    print("Let's call off the day folks")
    print("Good night")


fr1 = tk.Frame(root,bg="salmon",borderwidth=5,relief="sunken")

fr1.pack()

l1 = tk.Label(fr1,text="Click buttons below to print a message in the console",bg="purple",fg="white",font="comicsansms 19 underline")
l1.pack(padx=24,pady=24)

fr2 = tk.Frame(root,bg="#17a589",borderwidth=5,relief="sunken")
fr2.pack(side="top",padx=21,pady=21)

btn1 = tk.Button(fr2,text="Say Good Morning",bg="#28b463",command=good_morning,cursor="mouse")
btn1.pack(padx=15,pady=15)

btn2 = tk.Button(fr2,text="Say Good Afternoon",bg="#28b463",command=good_afternoon,cursor="mouse")
btn2.pack(padx=15,pady=15)

btn3 = tk.Button(fr2,text="Say Good Evening",bg="#28b463",command=good_evening,cursor="mouse")
btn3.pack(padx=15,pady=15)

btn4 = tk.Button(fr2,text="Say Good Night",bg="#28b463",command=good_night,cursor="mouse")
btn4.pack(padx=15,pady=15)

root.mainloop()