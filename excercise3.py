from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry("644x344")

root.title("Window Resizer")

# taking the initial values again for resetting
initial_width = 644
initial_height = 344

def resize_window():
    '''
    This function resizes the window according to the width and height values entered by the user
    '''
    window_width = width_value.get()
    window_height = height_value.get()

    if window_width.isdigit() and window_height.isdigit():
        window_width = int(window_width)
        window_height = int(window_height)

        root.geometry(f"{window_width}x{window_height}")
        messagebox.showinfo("Voila !! Success","The window size was updated successfully")
    else:
        messagebox.showerror("Invalid input","Please enter valid values for width and height")

def reset_window_size():
    '''
    This function resets the window to its original size and populates the entries accordingly
    '''
    root.geometry(f"{initial_width}x{initial_height}")
    width_value.set(initial_width)
    height_value.set(initial_height)
    messagebox.showinfo("Reset success","Window size has been reset successfully")

# Creating labels for indicating user inputs

title_label = Label(root,text="Window resizer",font="Lucida 13 underline",fg="navyblue")
title_label.grid(row=0,column=3)


width_label = Label(root,text="Enter the width")
height_label = Label(root,text="Enter the height")

# packing the labels in the grid
width_label.grid(row=1,column=1,pady=15,padx=15)
height_label.grid(row=2,column=1,pady=15,padx=15)

# creating tkinter variables to store entry values
width_value = StringVar()
height_value = StringVar()

width_entry = Entry(root,textvariable=width_value)
height_entry = Entry(root,textvariable=height_value)

width_entry.grid(row=1,column=2)
height_entry.grid(row=2,column=2)

# Creating the apply and reset buttons
apply_btn = Button(root,text="Apply",font="Lucida 13 bold",command=resize_window)
reset_btn = Button(root,text="Reset to original size",command=reset_window_size,font="Lucida 13 bold")

# Packing the buttons
apply_btn.grid(row=3,column=2,pady=15)
reset_btn.grid(row=3,column=3,pady=15)

# staring the GUI
root.mainloop()