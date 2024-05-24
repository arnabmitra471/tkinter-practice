# Travel form using tkinter

from tkinter import *

root = Tk()
root.title("Travel form with grid layout")

root.geometry("644x344")
# Creating the Heading label
title_label = Label(root,text="Welcome to anala tours",font="comicsansms 13 bold",pady=15)

title_label.grid(row=0,column=3)

# Creating label for our travel form
name_label = Label(root,text="Name")
phone_label = Label(root,text="Phone")
gender_label = Label(root,text="Gender")
enmergency_label = Label(root,text="emergency contact")
payment_mode_label = Label(root,text="Payment mode")
food_service_label = Label(root,text="Choose Food Service")

# Packing the labels for our travel form

name_label.grid(row=1,column=1)
phone_label.grid(row=2,column=1)
gender_label.grid(row=3,column=1)
enmergency_label.grid(row=4,column=1)
payment_mode_label.grid(row=5,column=1)
food_service_label.grid(row=6,column=1)

# Creating Tkinter variables to store entry values

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
enmergency_value = StringVar()
payment_mode_value = StringVar()
food_service_value = IntVar()

# Creating the entries with the entry values

name_entry = Entry(root,textvariable=name_value)
phone_entry = Entry(root,textvariable=phone_value)
gender_entry = Entry(root,textvariable=phone_value)
emergency_entry = Entry(root,textvariable=phone_value)
payment_mode_entry = Entry(root,textvariable=phone_value)


# Packing the entries

name_entry.grid(row=1,column=2)
phone_entry.grid(row=2,column=2)
gender_entry.grid(row=3,column=2)
emergency_entry.grid(row=4,column=2)
payment_mode_entry.grid(row=5,column=2)

# Starting the GUI

root.mainloop()