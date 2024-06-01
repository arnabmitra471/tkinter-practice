from tkinter import *
from tkinter import messagebox as tmsg

root = Tk()
root.geometry("655x433")

root.title("messagebox in Tkinter")


def open_file_menu():
    print("Opening the file menu")

def open_edit_menu():
    print("Opening the edit menu")

def open_view_menu():
    print("Opening the view menu")

def open_help_menu():
    print("Opening the help menu")

def create_new_text_file():
    print("creating a new text file")

def create_new_file():
    print("creating a new code file")

def open_new_window():
    print("Opening a new window")

def open_file():
    print("Opening a file")

def open_folder():
    print("Opening a folder")

def close_folder():
    print("Closing the folder")

def close_editor():
    print("Closing the editor")

def cut_text():
    print("The text has been cut and placed on clipboard")

def copy_text():
    print("The text has been copied and placed on clipboard")

def paste_text():
    print("Pasting the text from clipboard")

def find_text():
    print("The text has been cut and placed on clipboard")

def replace_text():
    print("Replacing the occurences of the text")

def show_status_bar():
    print("Showing the status bar. Uncheck to hide")

def editor_help():
    msg = tmsg.showinfo("Help","Arnab will help you with this GUI")
    print(msg)


def rate():
    rate_msg = tmsg.askquestion("Rate Us","You used this GUI... Was your experience good")
    print(rate_msg)

    if rate_msg == "yes":
        msg = "Great !! Please share with your friends too !!!"
        tmsg.showinfo("Glad to hear from you...",msg)
    else:
        msg = "We apologise for the inconvenience... Please let us know what can we improve to make your experience better ??"
        tmsg.showinfo("Sorry",msg)

def divya():
    ans = tmsg.askretrycancel("Divya se dosti kar lo","Divya nahi banegi aapki dost")
    print(ans)

    if ans:
       response_msg =  tmsg.showerror("Sorry","Retry Karne se bhi kuch nahi hoga")
       print(response_msg)
    else:
        response_msg = tmsg.showinfo("Bahut badhiya","Bahut badhiya bhai... cancel kar diya")
        print(response_msg)


main_menu = Menu(root)
file_submenu = Menu(main_menu,tearoff=False)

# main_menu.add_command(label="File",command=open_file_menu)
# main_menu.add_command(label="Edit",command=open_edit_menu)
# main_menu.add_command(label="View",command=open_view_menu)
# main_menu.add_command(label="Help",command=open_help_menu)


# Adding commands in the file submenu

file_submenu.add_command(label="New text file",command=create_new_text_file)
file_submenu.add_command(label="New file",command=create_new_file)
file_submenu.add_command(label="New window",command=open_new_window)
file_submenu.add_separator()
file_submenu.add_command(label="Open Folder",command=open_folder)
file_submenu.add_command(label="Open File",command=open_file)
file_submenu.add_separator()

file_submenu.add_command(label="Close folder",command=close_folder)
file_submenu.add_command(label="Close Editor",command=close_editor)

main_menu.add_cascade(label="File",menu=file_submenu)

edit_submenu = Menu(main_menu,tearoff=False)
edit_submenu.add_command(label="Cut",command=cut_text)
edit_submenu.add_command(label="Copy",command=copy_text)
edit_submenu.add_command(label="Paste",command=paste_text)
edit_submenu.add_separator()
edit_submenu.add_command(label="Find",command=find_text)
edit_submenu.add_command(label="Replace",command=replace_text)
main_menu.add_cascade(label="Edit",menu=edit_submenu)

view_submenu = Menu(root,tearoff=False)

view_submenu.add_checkbutton(label="Status bar",command=show_status_bar)

main_menu.add_cascade(label="View",menu=view_submenu)


help_submenu = Menu(root,tearoff=False)

help_submenu.add_command(label="About the software",command=editor_help)
help_submenu.add_command(label="Rate Us",command=rate)
help_submenu.add_command(label="Befriend Divya",command=divya)
main_menu.add_cascade(label="Help",menu=help_submenu)


root.config(menu=main_menu)
root.mainloop()