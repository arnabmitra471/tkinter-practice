import tkinter as tk

root = tk.Tk()

root.geometry("644x434") # Determines the width and height of the window

root.minsize(300,100)
root.maxsize(1100,800)

l1 = tk.Label(text="I am a good boy")
l1.pack()

root.mainloop()