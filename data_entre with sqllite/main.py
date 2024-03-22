import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os
# this is the parent window for the other widget
def enter_data():
    accepted = accept_val.get()

    if accepted == "accepted":

        #user info
        firstname = first_entry.get()
        lastname = last_entry.get()
        #condition for first and last name to be required
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            #course info
            numbercourse = numbercourse_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            registration = reg_status_var.get()

            print("First name:", firstname, "Last name:", lastname)
            print("Title:", title, "Age:", age)
            print("Nationality:", nationality)
            print("# Courses:", numbercourse, "#Semesters:", numsemesters)
            print("# Current Registered:", registration)
            print("--------------------------------------------------------")
            #create a connection
            conn = sqlite3.connect('data.db')
            #create  table
            table_create_query = '''CREATE TABLE IF NOT EXISTS student_data(firstname TEXT, 
                                  lastname TEXT, title TEXT,age INT,nationality TEXT,
                                   registration_status TEXT, num_courses INT, num_semesters INT)'''
            conn.execute(table_create_query)
            #insert data
            data_insert_query = ''' INSERT INTO student_data(firstname, lastname, title,age,nationality,registration_status,num_courses,num_semesters)
            VALUES (?,?,?,?,?,?,?,?) '''

            #from the variable declared to enter data
            data_insert_tuple = (firstname,lastname,title, age,nationality,numbercourse,numsemesters,registration)
            cursor = conn.cursor()
            cursor.execute(data_insert_query,data_insert_tuple)
            conn.commit()
            conn.close()
            #make sure to close the connection

            # Clear the data in entry widgets, comboboxes, and spinboxes
            first_entry.delete(0, tkinter.END)
            last_entry.delete(0, tkinter.END)
            title_combobox.set('')
            age_spinbox.delete(0, tkinter.END)
            nationality_combobox.set('')
            reg_status_var.set('Not Registered')
            #numbercourse_spinbox.delete(0, tkinter.END)
            #numsemesters_spinbox.delete(0, tkinter.END)

        else:
            tkinter.messagebox.showwarning(title="Error",message="First Name and Last Name are required")
    else:
        tkinter.messagebox.showwarning(title="Error",message="you have not Accepted the terms")

window = tkinter.Tk()
window.title("Data_Entre Form")
#our first frame
frame = tkinter.Frame(window)
frame.pack()#the pack layout make it responsive

# saving user info
# two task to always to do :
# 1: to define the widget
#2: to pack the widget for it to display on the screen
user_info = tkinter.LabelFrame(frame, text="User Information",font="times 12 bold")
user_info.grid(row=0, column=0,padx=20,pady=15)

#creating the widgets
first_name = tkinter.Label(user_info, text="First Name",font="times 12 bold")
first_name.grid(row=0,column=0)
last_name = tkinter.Label(user_info,text="Last Name",font="times 12 bold")
last_name.grid(row=0,column=1)

#creating the Entry widget to capture data
first_entry = tkinter.Entry(user_info,font="arial 12 bold")
last_entry = tkinter.Entry(user_info,font="arial 12 bold")
# to disply them to the screen
first_entry.grid(row=1,column=0)
last_entry.grid(row=1,column=1)

#creation of the combobox
title = tkinter.Label(user_info, text="Title",font="times 12 bold")
title_combobox = ttk.Combobox(user_info, values=["","Mr.","Ms.","Dr."],font="arial 12 bold")
#displying the combo itemes
title.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)
# spinbox for user age
age_lable = tkinter.Label(user_info,text="age",font="times 12 bold")
age_spinbox = tkinter.Spinbox(user_info, from_ = 18 ,to = 100,font="arial 12 bold")
age_lable.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

# combobox for users nationality
nationality_label = tkinter.Label(user_info,text="Nationality",font="times 12 bold")
nationality_combobox = ttk.Combobox(user_info, values=["Africa","Asia","Europe","Congolese","chine","japan","American"],font="arial 12 bold")
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

# create space in between widgets
for widgets in user_info.winfo_children():
    widgets.grid_configure(padx=10,pady=5)
# second Label frame
#saving course info
courses_frame = tkinter.LabelFrame(frame, text="Course info",font="times 12 bold")
courses_frame.grid(row=1, column=0,sticky="news",padx=20,pady=15)

#adding our Lables
reg_status_var = tkinter.StringVar(value="Not Registered")
registwe_lable = tkinter.Label(courses_frame, text="Registered Status",font="times 12 bold")
register_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",variable=reg_status_var,
                                     onvalue="Registered", offvalue="Not Registered",font="times 10 bold")
registwe_lable.grid(row=0,column=0)
register_check.grid(row=1,column=0)

# creating number of course with spinbox
numbercourse = tkinter.Label(courses_frame, text="# Completed courses",font="times 12 bold")
numbercourse_spinbox =tkinter.Spinbox(courses_frame, from_= 0, to='infinity',font="arial 12 bold")
numbercourse.grid(row=0,column=1)
numbercourse_spinbox.grid(row=1,column=1)

# adding another spinbox for numbers of semesters
numsemesters = tkinter.Label(courses_frame,text="# Semesters",font="times 12 bold")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity",font="arial 12 bold")
numsemesters.grid(row=0,column=2)
numsemesters_spinbox.grid(row=1,column=2)
# create space in between widgets
for widgets in courses_frame.winfo_children():
    widgets.grid_configure(padx=10,pady=5)

#Accept terms

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions",font="times 12 bold")
terms_frame.grid(row=2, column=0,sticky="news",padx=20,pady=15)
#the creation of variable (accept_val = StringVar()) and parameters (onvalue, offvalue)
accept_val = tkinter.StringVar(value="not accepted")
terms_check = tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions.",
                                  variable=accept_val,onvalue="accepted",
                                  offvalue="not accepted",font="times 10 bold")
terms_check.grid(row=0,column=0)

#button
btn = ttk.Button(frame,text="Enter data",command= enter_data)
#adding style when the cursor is over
btn.grid(row=3,column=0,sticky="news",padx=20,pady=15)
ttk.Style().configure("TButton", padding=6, relief="raised",
   background="#ccc",font="times 12 bold")

window.mainloop()