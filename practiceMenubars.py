from tkinter import *

root = Tk()

root.geometry("634x444")

root.title("Menubars practice")

root.minsize(344,233)

def open_file_menu():
    print("opening file menu")

def open_edit_menu():
    print("Opening edit menu")

def create_new_text_file():
    print("Creating new text file")

def create_new_file():
    print("Creating new file")

def open_new_window():
    print("Opening a new window")

def open_file():
    print("Opening a file")

def open_folder():
    print("Opening a folder")

def undo_last_action():
    print("Undoing last action...")

def redo_last_action():
    print("Redoing last action...")

def cut_text():
    print("The selected text has been cut and placed on clipboard")

def copy_text():
    print("The selected text has been copied and placed on clipboard")

def paste_text():
    print("Pasting the selected text...")

def find_text():
    print("Finding the specified text in the current file")

def replace_text():
    print("Replacing the occurences of the specified text")
# Creating the main menu

main_menu = Menu(root)
file_menu = Menu(main_menu,tearoff=False)

# main_menu.add_command(label="File",command=open_file_menu)
# main_menu.add_command(label="Edit",command=open_edit_menu)

file_menu.add_command(label="New Text File",command=create_new_text_file)
file_menu.add_command(label="New File",command=create_new_file)
file_menu.add_command(label="New Window",command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Open file",command=open_file)
file_menu.add_command(label="Open folder",command=open_folder)


edit_menu = Menu(main_menu,tearoff=False)

# main_menu.add_command(label="File",command=open_file_menu)
# main_menu.add_command(label="Edit",command=open_edit_menu)
edit_menu.add_command(label="Undo",command=undo_last_action)
edit_menu.add_command(label="Redo",command=redo_last_action)
edit_menu.add_separator()
edit_menu.add_command(label="Cut",command=cut_text)
edit_menu.add_command(label="Copy",command=copy_text)
edit_menu.add_command(label="Paste",command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label="Find",command=find_text)
edit_menu.add_command(label="Replace",command=replace_text)

main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)

root.config(menu=main_menu)
root.mainloop()