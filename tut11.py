# Travel form using tkinter

from tkinter import *

root = Tk()
root.title("Travel form with grid layout")

root.geometry("644x444")
def get_data():
    """
    This function handles the data submiited from the application
    and writes the data to a text file
    """
    if name_value.get() == "" or phone_value.get() == "" or gender_value.get() == "" or enmergency_value.get() == "" or payment_mode_value.get() == "":
        submit_btn["state"] = "disabled"
        print("Please enter the values first before sumitting")
        
    else:
        submit_btn["state"] = "normal"
        with open("traveldata.txt","a") as file:
            file.write(f"name: {name_value.get()} \n phone: {phone_value.get()} \n gender: {gender_value.get()} \n emergency contact: {enmergency_value.get()} \n payment mode: {payment_mode_value.get()} \n food service chosen: {food_service_value.get()}")
        print("Written to file successfully")
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
gender_entry = Entry(root,textvariable=gender_value)
emergency_entry = Entry(root,textvariable=enmergency_value)
payment_mode_entry = Entry(root,textvariable=payment_mode_value)

# Checkbutton for food service

food_service_check = Checkbutton(root,text="Want to prebook your meals",fg="orangered",variable=food_service_value,borderwidth=5,relief=RAISED)

# Creating a button packing it and assigning it a command
submit_btn = Button(root,text="Submit to anala tours",bg="salmon",fg="white",command=get_data)
submit_btn.grid(row=7,column=2)


# Packing the entries

name_entry.grid(row=1,column=2,pady=15)
phone_entry.grid(row=2,column=2,pady=15)
gender_entry.grid(row=3,column=2,pady=15)
emergency_entry.grid(row=4,column=2,pady=15)
payment_mode_entry.grid(row=5,column=2,pady=15)
food_service_check.grid(row=6,column=2,pady=15)

# Starting the GUI

root.mainloop()