from tkinter import *

root = Tk()


def my_func():
    print("Main ek bahut hi natkat aur shaitaan function hoon")

def new_file():
    print("Creating a new file")

def open_file():
    print("Opening a file")

def undo_last_action():
    print("Undoing last action")

def redo_last_action():
    print("redoing last action")

def cut_text():
    print("Text has been cut and placed on clipboard")

def copy_text():
    print("Text has been copied and placed on clipboard")

def paste_text():
    print("Pasting the text...")

def find_text():
    print("Finding the text specified...")
root.geometry("733x466")

root.title("Pycharm")

# Creating a menu widget

# We can create a non dropdown menu in tkinter like this
# my_menu = Menu(root)

# my_menu.add_command(label="File",command=my_func)
# my_menu.add_command(label="Quit",command=quit)

# root.config(menu=my_menu)

soft_menu_bar = Menu(root)
m1 = Menu(soft_menu_bar,tearoff=0)

m1.add_command(label="New Project",command=my_func)
m1.add_command(label="New file",command=new_file)
m1.add_separator()
m1.add_command(label="Open file",command=open_file) 

soft_menu_bar.add_cascade(label="File",menu=m1)

root.config(menu=soft_menu_bar)

m2 = Menu(soft_menu_bar,tearoff=0)

m2.add_command(label="Undo",command=undo_last_action)
m2.add_command(label="Redo",command=redo_last_action)
m2.add_separator()
m2.add_command(label="Cut",command=cut_text) 
m2.add_command(label="Copy",command=copy_text) 
m2.add_command(label="Paste",command=paste_text) 
m2.add_command(label="Find",command=find_text)

soft_menu_bar.add_cascade(label="Edit",menu=m2)

root.config(menu=soft_menu_bar)

root.mainloop()