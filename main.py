#-------------------------------importing files----------------------------#
import csv
import re
import pandas
import xlwt
import pandas.io.sql as sql
import openpyxl
import pdb

#-----------------------------main frame code-------------------------------#

from tkinter import*
from tkinter import messagebox
from tkinter.font import *
import tkinter.font
from tkinter import ttk
import pymysql
from tkinter.ttk import Treeview
from tkcalendar import *
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import *
import tkinter.font
def exp ():
    ff = filedialog.asksaveasfile(
        defaultextension=".xlsx", initialdir='/Users/rohitnagula/Documents/Corel Cloud',
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")]
    )
    return ff


# Define the size of the window
WIDTH = 800
HEIGHT = 500

# Create the main window
root1 = Tk()
root1.title("Vidyalankar Institute of Technology")
root1.geometry("800x500")

# Calculate the center position of the screen
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
x_pos = int((screen_width / 2) - (800 / 2))
y_pos = int((screen_height / 2) - (500 / 2))

# Set the window position to the center of the screen
root1.geometry("+{}+{}".format(x_pos, y_pos))

photo1 = PhotoImage(file="final 1 (2).png")
label1 = Label(root1, image=photo1)
label1.place(x=0, y=0, width=798, height=529)
root1.config(highlightcolor="white")


def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "password":
        result_label.config(text="Login Successful!", fg="green")
        root1.destroy()
        nextinterface()
    else:
        result_label.config(text="Invalid username or password", fg="red")

import tkinter.filedialog as fd
count = 0
text = ""
def nextinterface():
    print("destroyed 1")
    root = Tk()
    root.geometry("1174x700+200+50")
    root.title("Student Management System")
    root.config(bg="white")
    root.iconbitmap('icon.ico')
    root.resizable(False, False)
    # -----------------------------header frames-----------------------------------#
    DataEntryFrame = Frame(root, bg="white smoke", relief=GROOVE, borderwidth=2)
    DataEntryFrame.place(x=0, y=0, width=1202, height=65)

    # -----------------------College photo frame frame-----------------------------#

    ShowDataFrame = Frame(root, bg='white', relief=RIDGE, bd=0, borderwidth=0)
    ShowDataFrame.place(x=256, y=58, width=918, height=642)

    DataEntryFrame1 = Frame(root, bg='white smoke', relief=GROOVE, borderwidth=2, bd=2)
    DataEntryFrame1.place(x=0, y=58, width=256, height=642)

    # --------------------------------import images--------------------------------#
    photo = PhotoImage(file="side 2.png")
    label1 = Label(DataEntryFrame1, image=photo)
    label1.place(x=-2, y=-2, width=260, height=697)

    photo4 = PhotoImage(file="texture 2.png")
    label2 = Label(root, image=photo4)
    label2.place(x=0, y=0, width=1172, height=57)

    # --------------------------------Treeview Creation----------------------------#

    style = ttk.Style()
    style.configure('Treeview.Heading', font=("roman", 14, 'bold'), foreground="midnight blue")
    scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
    scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
    studenttable = Treeview(ShowDataFrame, columns=(
        "Roll No", "Name", "Mobile No", "Email id", "Address", "Gender", "D.O.B", "SSC Result", "HSC Result",
        "Branch", "Sem 1",
        "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6", "Sem 7", "Sem 8"), yscrollcommand=scroll_y.set,
                            xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=studenttable.xview)
    scroll_y.config(command=studenttable.yview)
    studenttable.heading("Roll No", text="Roll No")
    studenttable.heading("Name", text="Name")
    studenttable.heading("Mobile No", text="Mobile No")
    studenttable.heading("Email id", text="Email id")
    studenttable.heading("Address", text="Address")
    studenttable.heading("Gender", text="Gender")
    studenttable.heading("D.O.B", text="D.O.B")
    studenttable.heading("SSC Result", text="SSC Result")
    studenttable.heading("HSC Result", text="HSC Result")
    studenttable.heading("Branch", text="Branch")
    studenttable.heading("Sem 1", text="Sem 1")
    studenttable.heading("Sem 2", text="Sem 2")
    studenttable.heading("Sem 3", text="Sem 3")
    studenttable.heading("Sem 4", text="Sem 4")
    studenttable.heading("Sem 5", text="Sem 5")
    studenttable.heading("Sem 6", text="Sem 6")
    studenttable.heading("Sem 7", text="Sem 7")
    studenttable.heading("Sem 8", text="Sem 8")
    studenttable['show'] = 'headings'
    studenttable.column('Roll No', width=90)
    studenttable.column('Name', width=200)
    studenttable.column('Mobile No', width=90)
    studenttable.column('Email id', width=200)
    studenttable.column('Address', width=120)
    studenttable.column('Gender', width=65)
    studenttable.column('D.O.B', width=70)
    studenttable.column('SSC Result', width=85)
    studenttable.column('HSC Result', width=85)
    studenttable.column('Branch', width=70)
    studenttable.column('Sem 1', width=60)
    studenttable.column('Sem 2', width=60)
    studenttable.column('Sem 3', width=60)
    studenttable.column('Sem 4', width=60)
    studenttable.column('Sem 5', width=60)
    studenttable.column('Sem 6', width=60)
    studenttable.column('Sem 7', width=60)
    studenttable.column('Sem 8', width=60)
    studenttable.pack(fill=BOTH, expand=1)

    # --------------college photo-----------#
    '''photo1 = PhotoImage(file="final 1.png")
    label1 = Label(ShowDataFrame,image=photo1)
    label1.place(x=0,y=0,width=921,height=647)
    ShowDataFrame.config(highlightcolor="white")'''

    # ----------------------------------intro-slider----------------------------------#
    import random
    colours = ['blue4', 'black', "midnight blue"]
    # -----------------------------------slider---------------------------------------#
    ss = "Vidyalankar Institute of Technology | विद्यालंकार प्रौद्योगिकी संस्थान   "
    count = 0
    text = ''


    def IntroLabelColorTick():
        fg = random.choice(colours)
        SliderLabel.config(fg=fg)
        SliderLabel.after(300, IntroLabelColorTick)

    def IntroLabelTick():
        global count, text
        if (count >= len(ss)):
            count = 0
            text = ""
            SliderLabel.config(text=text)
        else:
            text = text + ss[count]
            SliderLabel.config(text=text)
            count += 1
        SliderLabel.after(125, IntroLabelTick)

    # --------------------------------college slider-----------------------------------#

    # -----------------------------------Slider function call--------------------------#
    SliderLabel = Label(root, text=ss, font=('Times', 25, 'bold'), relief=RIDGE, borderwidth=0, width=55,
                        bg='white', bd=2, highlightbackground="light blue")
    SliderLabel.place(x=260, y=11)
    IntroLabelTick()
    IntroLabelColorTick()

    # -------------------------time and date working--------------------------------#
    def tick():
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        clock.config(text='Date = ' + date_string + "\n" + "Time = " + time_string, bg="white smoke", bd=2)
        clock.after(200, tick)
        print(time_string, date_string)

    # -----------------------------------clock function call -----------------------------------#
    clock = Label(root, font=('Times', 13, 'bold'), relief=RIDGE, borderwidth=0, bg='white', fg="midnight blue")
    clock.place(x=1070, y=12)
    tick()

    def addstudent():

        def submit():
            global cursor, con
            RollNo = rollval.get()
            Name = nameval.get()
            MobileNo = mobileval.get()
            Emailid = emailval.get()
            Address = addressval.get()
            Gender = genderval.get()
            DOB = dobval.get()
            SSCResult = sscval.get()
            HSCResult = hscval.get()
            Branch = branchval.get()
            Sem1 = sem1val.get()
            Sem2 = sem2val.get()
            Sem3 = sem3val.get()
            Sem4 = sem4val.get()
            Sem5 = sem5val.get()
            Sem6 = sem6val.get()
            Sem7 = sem7val.get()
            Sem8 = sem8val.get()

            details = (
                RollNo, Name, MobileNo, Emailid, Address, Gender, DOB, SSCResult, HSCResult, Branch, Sem1, Sem2, Sem3,
                Sem4, Sem5, Sem6, Sem7, Sem8)

            try:
                if (len(MobileNo) == 10 or MobileNo == ""):
                    print("Phone accepted")
                    # connect to MySQL database
                    if ((re.match(r"[^@]+@[^@]+\.[^@]+", Emailid)) or Emailid == ""):

                        if SSCResult >= 0 and SSCResult <= 100 or SSCResult == "0":

                            if HSCResult >= 0 and HSCResult <= 100 or HSCResult == "0":

                                if Sem1 >= 0 and Sem1 <= 100 or Sem1 == "0":

                                    if Sem2 >= 0 and Sem2 <= 100 or Sem2 == "0":

                                        if Sem3 >= 0 and Sem3 <= 100 or Sem3 == "0":

                                            if Sem4 >= 0 and Sem4 <= 100 or Sem4 == "0":

                                                if Sem5 >= 0 and Sem5 <= 100 or Sem5 == "0":

                                                    if Sem6 >= 0 and Sem6 <= 100 or Sem6 == "0":

                                                        if Sem7 >= 0 and Sem7 <= 100 or Sem7 == "0":

                                                            if Sem8 >= 0 and Sem8 <= 100 or Sem8 == "0":
                                                                conn = pymysql.connect(host='localhost',
                                                                                       database='studentmanagementsystem1',
                                                                                       user='root',
                                                                                       password='Rohit@9324')
                                                                # prepare a cursor object using cursor() method
                                                                cursor = conn.cursor()
                                                                # prepare SQL query stringto insert a row
                                                                str = "insert into studentdata(Rollno,Name,Mobileno,Emailid,Address,Gender,DOB_MM_DD_YY,SSCResult,HSCResult,Branch,Sem1,Sem2,Sem3,Sem4,Sem5,Sem6,Sem7,Sem8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                                try:
                                                                    # execute the SQL query using execute() method
                                                                    print("hello")
                                                                    cursor.execute(str, (
                                                                        RollNo, Name, MobileNo, Emailid, Address,
                                                                        Gender,
                                                                        DOB, SSCResult, HSCResult, Branch,
                                                                        Sem1,
                                                                        Sem2,
                                                                        Sem3, Sem4, Sem5, Sem6, Sem7, Sem8))
                                                                    print("hello")
                                                                    # save the changes to the database
                                                                    conn.commit()
                                                                    res = messagebox.askyesnocancel('Notifications',
                                                                                                    'Roll No {} Details Added Succesfully !\nDo u want to clear the form?'.format(
                                                                                                        RollNo),
                                                                                                    parent=addroot)
                                                                    if (res == True):
                                                                        rollval.set('')
                                                                        nameval.set('')
                                                                        mobileval.set('')
                                                                        emailval.set('')
                                                                        addressval.set('')
                                                                        genderval.set('                       ')
                                                                        dobval.set('')
                                                                        sscval.set('0')
                                                                        hscval.set('0')
                                                                        branchval.set('                       ')
                                                                        sem1val.set('0')
                                                                        sem2val.set('0')
                                                                        sem3val.set('0')
                                                                        sem4val.set('0')
                                                                        sem5val.set('0')
                                                                        sem6val.set('0')
                                                                        sem7val.set('0')
                                                                        sem8val.set('0')

                                                                    strr = 'select * from studentdata'
                                                                    print("DOne")

                                                                    cursor.execute(strr)
                                                                    strr = 'select * from studentdata'
                                                                    print("DOne")

                                                                    cursor.execute(strr)
                                                                    print("DOne")

                                                                    datas = cursor.fetchall()

                                                                    print("DOne")
                                                                    studenttable.delete(
                                                                        *studenttable.get_children())
                                                                    print("DOne")
                                                                    for i in datas:
                                                                        vv = [i[0], i[1], i[2], i[3], i[4], i[5],
                                                                              i[6],
                                                                              i[7], i[8], i[9], i[10], i[11],
                                                                              i[12],
                                                                              i[13],
                                                                              i[14], i[15],
                                                                              i[16], i[17]]
                                                                        studenttable.insert('', END, values=vv)
                                                                    cursor.close()
                                                                    conn.close()

                                                                    print("hello")
                                                                    print('1 row inserted.....')

                                                                except:

                                                                    # rollback if there is any error
                                                                    messagebox.showerror('Notifications',
                                                                                         'Roll No {} Already Exist !\nPlease Try Another Roll No'.format(
                                                                                             RollNo),
                                                                                         parent=addroot)
                                                                    rollval.set('')
                                                                    nameval.set('')
                                                                    mobileval.set('')
                                                                    emailval.set('')
                                                                    addressval.set('')
                                                                    genderval.set('                       ')
                                                                    dobval.set('')
                                                                    sscval.set('0')
                                                                    hscval.set('0')
                                                                    branchval.set('                       ')
                                                                    sem1val.set('0')
                                                                    sem2val.set('0')
                                                                    sem3val.set('0')
                                                                    sem4val.set('0')
                                                                    sem5val.set('0')
                                                                    sem6val.set('0')
                                                                    sem7val.set('0')
                                                                    sem8val.set('0')
                                                                    conn.rollback()
                                                                # connection close
                                                            else:
                                                                messagebox.showerror('Notifications',
                                                                                     'Invalid Percentage of Sem 8!\nPlease Enter Correct Percentage',
                                                                                     parent=addroot)
                                                                sem8val.set('0')

                                                        else:
                                                            messagebox.showerror('Notifications',
                                                                                 'Invalid Percentage of Sem 7 !\nPlease Enter Correct Percentage',
                                                                                 parent=addroot)
                                                            sem7val.set('0')

                                                    else:
                                                        messagebox.showerror('Notifications',
                                                                             'Invalid Percentage of Sem 6 !\nPlease Enter Correct Percentage',
                                                                             parent=addroot)
                                                        sem6val.set('0')

                                                else:
                                                    messagebox.showerror('Notifications',
                                                                         'Invalid Percentage of Sem 5 !\nPlease Enter Correct Percentage',
                                                                         parent=addroot)
                                                    sem5val.set('0')

                                            else:
                                                messagebox.showerror('Notifications',
                                                                     'Invalid Percentage of Sem 4 !\nPlease Enter Correct Percentage',
                                                                     parent=addroot)
                                                sem4val.set('0')

                                        else:
                                            messagebox.showerror('Notifications',
                                                                 'Invalid Percentage of Sem 3 !\nPlease Enter Correct Percentage',
                                                                 parent=addroot)
                                            sem3val.set('0')

                                    else:
                                        messagebox.showerror('Notifications',
                                                             'Invalid Percentage of Sem 2 !\nPlease Enter Correct Percentage',
                                                             parent=addroot)
                                        sem2val.set('0')

                                else:
                                    messagebox.showerror('Notifications',
                                                         'Invalid Percentage of Sem 1 !\nPlease Enter Correct Percentage',
                                                         parent=addroot)
                                    sem1val.set('0')

                            else:
                                messagebox.showerror('Notifications',
                                                     'Invalid Percentage of HSC !\nPlease Enter Correct Percentage',
                                                     parent=addroot)
                                hscval.set('0')


                        else:
                            messagebox.showerror('Notifications',
                                                 'Invalid Percentage of SSC !\nPlease Enter Correct Percentage',
                                                 parent=addroot)
                            sscval.set('0')


                    else:
                        messagebox.showerror('Notifications', 'Invalid Email Id !\nPlease Enter Correct Email Id',
                                             parent=addroot)

                        emailval.set('')

                else:
                    messagebox.showerror('Notifications', 'Invalid Phone Number !\nPlease Enter Correct Number',
                                         parent=addroot)

                    mobileval.set('')


            except:
                print("DOne")

        addroot = Toplevel()
        addroot.geometry("913x615+460+135")
        addroot.title("Add Student Details")
        addroot.config(bg='white')
        addroot.iconbitmap('icon.ico')
        addroot.resizable(False, False)

        # --------------------Student Labels---------------------#

        # ---------------frame for left part------------------------#
        DataEntryFrame2 = Frame(addroot, bg="white", relief=GROOVE, borderwidth=2, bd=1)
        DataEntryFrame2.place(x=0, y=0, width=457, height=540)

        idlabel = Label(addroot, text="Roll No : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=10, y=10)
        idlabel = Label(addroot, text="Full Name: ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=70)
        idlabel = Label(addroot, text="Mobile no : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=130)
        idlabel = Label(addroot, text="Email id : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=190)
        idlabel = Label(addroot, text="Address : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=250)
        idlabel = Label(addroot, text="Gender : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=310)
        idlabel = Label(addroot, text="Date Of Birth : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=14)
        idlabel.place(x=10, y=370)
        idlabel = Label(addroot, text="SSC Result in Percentage: ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=26)
        idlabel.place(x=10, y=430)
        idlabel = Label(addroot, text="HSC Result in Percentage: ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=26)
        idlabel.place(x=10, y=490)
        # --------------------frame for right part----------------------#
        DataEntryFrame3 = Frame(addroot, bg="white", relief=GROOVE, borderwidth=2, bd=2)
        DataEntryFrame3.place(x=457, y=0, width=1200, height=541)

        idlabel = Label(addroot, text="Branch : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=10)
        idlabel = Label(addroot, text="Sem 1 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=70)
        idlabel = Label(addroot, text="Sem 2 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=130)
        idlabel = Label(addroot, text="Sem 3 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=190)
        idlabel = Label(addroot, text="Sem 4 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=250)
        idlabel = Label(addroot, text="Sem 5 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=310)
        idlabel = Label(addroot, text="Sem 6 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=370)
        idlabel = Label(addroot, text="Sem 7 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=430)
        idlabel = Label(addroot, text="Sem 8: ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=490)

        # ---------------------------------add student entry boxes---------------------------------#

        rollval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        addressval = StringVar()
        genderval = StringVar()
        genderval.set("                          ")
        options = ["Male",
                   "Female",
                   "Other"]
        drop = OptionMenu(addroot, genderval, *options)
        drop.pack()
        drop.place(x=130, y=310)
        dobval = StringVar()

        sscval = IntVar()
        hscval = IntVar()
        branchval = StringVar()
        branchval.set("                        ")
        options1 = ["INFT",
                    "EXTC",
                    "CMPN",
                    "ETRX",
                    "BIOMED",
                    "EXCS"]
        drop1 = OptionMenu(addroot, branchval, *options1)
        drop1.pack()  # dropdown
        drop1.place(x=630, y=10)
        sem1val = IntVar()
        sem2val = IntVar()
        sem3val = IntVar()
        sem4val = IntVar()
        sem5val = IntVar()
        sem6val = IntVar()
        sem7val = IntVar()
        sem8val = IntVar()
        identry = Entry(addroot, font=("Times", 14), bg="white", bd=1, textvariable=rollval, highlightthickness=1)
        identry.place(x=130, y=10)

        nameentry = Entry(addroot, font=("Times", 14), bd=1, textvariable=nameval, highlightthickness=1)
        nameentry.place(x=130, y=70)

        mobileentry = Entry(addroot, font=("Times", 14), bd=1, textvariable=mobileval, highlightthickness=1)
        mobileentry.place(x=130, y=130)

        emailentry = Entry(addroot, font=("Times", 14), bd=1, textvariable=emailval, highlightthickness=1)
        emailentry.place(x=130, y=190)

        addressentry = Entry(addroot, font=("Times", 14), bd=1, textvariable=addressval, highlightthickness=1)
        addressentry.place(x=130, y=250)

        dobentry = DateEntry(addroot, font=("Times", 16), background="black", disabledbackground="black",
                             bordercolor="black", headersbackground="black", normalbackground="white",
                             foreground='black', normalforeground='black', headersforeground='black', bd=0,
                             textvariable=dobval, selectmode='day')
        dobentry.config(background="black")
        dobentry.grid(row=1, column=1, padx=15)
        dobentry.place(x=160, y=370)
        dobval.set("")

        sscentry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sscval, highlightthickness=1)
        sscentry.place(x=260, y=430)

        hscentry = Entry(addroot, font=("Times", 14), bd=1, textvariable=hscval, highlightthickness=1)
        hscentry.place(x=260, y=490)

        sem1entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem1val, highlightthickness=1)
        sem1entry.place(x=630, y=70)

        sem2entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem2val, highlightthickness=1)
        sem2entry.place(x=630, y=130)

        sem3entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem3val, highlightthickness=1)
        sem3entry.place(x=630, y=190)

        sem4entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem4val, highlightthickness=1)
        sem4entry.place(x=630, y=250)

        sem5entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem5val, highlightthickness=1)
        sem5entry.place(x=630, y=310)

        sem6entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem6val, highlightthickness=1)
        sem6entry.place(x=630, y=370)

        sem7entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem7val, highlightthickness=1)
        sem7entry.place(x=630, y=430)

        sem8entry = Entry(addroot, font=("Times", 14), bd=1, textvariable=sem8val, highlightthickness=1)
        sem8entry.place(x=630, y=490)

        # -------------------submit button----------------------#

        submitbtn = Button(addroot, text="Submit", font=('Times', 20, 'bold'), width=20, bg='white', bd=1,
                           activeforeground="white", command=submit, highlightthickness=1)
        submitbtn.place(x=313, y=550)

        addroot.mainloop()

    # ------------------------------------Database Connectivity----------------------------------#

    def Connectdatabase():
        global mycursor, con
        try:
            con = pymysql.connect(host="localhost", user="root", database='studentmanagementsystem1',
                                  password="Rohit@9324")
            mycursor = con.cursor()
            print("Connected")
        except:
            messagebox.showerror('Database is Not Connected')
            return

    # --------------------------------------------------add student submit button working-----------------------------------#

    # --------------------------------button definiton----------------------------#

    def searchstudent():
        def search():
            RollNo = rollval.get()
            Name = nameval.get()
            MobileNo = mobileval.get()
            Emailid = emailval.get()
            Address = addressval.get()
            Gender = genderval.get()
            DOB = dobval.get()
            SSCResult = sscval.get()
            HSCResult = hscval.get()
            Branch = branchval.get()
            Sem1 = sem1val.get()
            Sem2 = sem2val.get()
            Sem3 = sem3val.get()
            Sem4 = sem4val.get()
            Sem5 = sem5val.get()
            Sem6 = sem6val.get()
            Sem7 = sem7val.get()
            Sem8 = sem8val.get()
            conn = pymysql.connect(host='localhost', database='studentmanagementsystem1', user='root',
                                   password='Rohit@9324')
            # prepare a cursor object using cursor() method
            cursor = conn.cursor()
            if (RollNo != ''):
                strr = 'select * from studentdata where RollNo=%s'
                cursor.execute(strr, (RollNo))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15], i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            elif (Name != ''):
                strr = 'select * from studentdata where Name=%s'
                cursor.execute(strr, (Name))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            elif (MobileNo != ''):
                strr = 'select * from studentdata where MobileNo=%s'
                cursor.execute(strr, (MobileNo))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            elif (Emailid != ''):
                strr = 'select * from studentdata where  Emailid=%s'
                cursor.execute(strr, (Emailid))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            elif (Address != ''):
                strr = 'select * from studentdata where Address=%s'
                cursor.execute(strr, (Address))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            elif (Gender != ''):
                strr = 'select * from studentdata where Gender=%s'
                cursor.execute(strr, (Gender))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)


            elif (DOB != ''):
                strr = 'select * from studentdata where DOB=%s'
                cursor.execute(strr, (DOB))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            elif (SSCResult != ''):
                strr = 'select * from studentdata where SSCResult =%s'
                cursor.execute(strr, (SSCResult))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            elif (HSCResult != ''):
                strr = 'select * from studentdata where HSCResult=%s'
                cursor.execute(strr, (HSCResult))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Branch != ''):
                strr = 'select * from studentdata where Branch=%s'
                cursor.execute(strr, (Branch))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem1 != ''):
                strr = 'select * from studentdata where Sem1=%s'
                cursor.execute(strr, (Sem1))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem2 != ''):
                strr = 'select * from studentdata where Sem2=%s'
                cursor.execute(strr, (Sem2))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem3 != ''):
                strr = 'select * from studentdata where Sem3=%s'
                cursor.execute(strr, (Sem3))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem4 != ''):
                strr = 'select * from studentdata where Sem4 =%s'
                cursor.execute(strr, (Sem4))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem5 != ''):
                strr = 'select * from studentdata where Sem5=%s'
                cursor.execute(strr, (Sem5))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem6 != ''):
                strr = 'select * from studentdata where Sem6=%s'
                cursor.execute(strr, (Sem6))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem7 != ''):
                strr = 'select * from studentdata where Sem7=%s'
                cursor.execute(strr, (Sem7))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)
            elif (Sem8 != ''):
                strr = 'select * from studentdata where Sem8=%s'
                cursor.execute(strr, (Sem8))
                datas = cursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                          i[14], i[15],
                          i[16], i[17]]
                    studenttable.insert('', END, values=vv)

            print("submitted")

        searchroot = Toplevel()
        searchroot.grab_set()
        searchroot.geometry("913x615+460+135")
        searchroot.title("Search Student Details")
        searchroot.config(bg='white')
        searchroot.iconbitmap('icon.ico')
        searchroot.resizable(False, False)
        # ----------------Student Labels---------------3

        # ------------frame for left part---------------#
        DataEntryFrame2 = Frame(searchroot, bg="white", relief=GROOVE, borderwidth=2, bd=1)
        DataEntryFrame2.place(x=0, y=0, width=457, height=540)

        idlabel = Label(searchroot, text="Roll No : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=10, y=10)
        idlabel = Label(searchroot, text="Full Name: ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=70)
        idlabel = Label(searchroot, text="Mobile no : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=130)
        idlabel = Label(searchroot, text="Email id : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=190)
        idlabel = Label(searchroot, text="Address : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=250)
        idlabel = Label(searchroot, text="Gender : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=310)
        idlabel = Label(searchroot, text="Date Of Birth : ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=14)
        idlabel.place(x=10, y=370)
        idlabel = Label(searchroot, text="SSC Result in Percentage: ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=26)
        idlabel.place(x=10, y=430)
        idlabel = Label(searchroot, text="HSC Result in Percentage: ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=26)
        idlabel.place(x=10, y=490)
        # ----------frame for right part---------------#
        DataEntryFrame3 = Frame(searchroot, bg="white", relief=GROOVE, borderwidth=2, bd=2)
        DataEntryFrame3.place(x=457, y=0, width=1200, height=541)

        idlabel = Label(searchroot, text="Branch : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=10)
        idlabel = Label(searchroot, text="Sem 1 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=70)
        idlabel = Label(searchroot, text="Sem 2 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=130)
        idlabel = Label(searchroot, text="Sem 3 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=190)
        idlabel = Label(searchroot, text="Sem 4 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=250)
        idlabel = Label(searchroot, text="Sem 5 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=310)
        idlabel = Label(searchroot, text="Sem 6 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=370)
        idlabel = Label(searchroot, text="Sem 7 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=430)
        idlabel = Label(searchroot, text="Sem 8: ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=490)

        # -------------------------- add student entry boxes---------------------------3
        rollval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        addressval = StringVar()
        genderval = StringVar()
        genderval.set("                         ")
        options = ["Male",
                   "Female",
                   "Other"]
        drop = OptionMenu(searchroot, genderval, *options)
        drop.pack()
        drop.place(x=130, y=310)
        dobval = StringVar()
        sscval = IntVar()
        hscval = IntVar()
        branchval = StringVar()
        branchval.set("                       ")
        options1 = ["INFT",
                    "EXTC",
                    "CMPN",
                    "ETRX",
                    "BIOMED",
                    "EXCS"]
        drop1 = OptionMenu(searchroot, branchval, *options1)
        drop1.pack()  # dropdown
        drop1.place(x=630, y=10)
        sem1val = IntVar()
        sem2val = IntVar()
        sem3val = IntVar()
        sem4val = IntVar()
        sem5val = IntVar()
        sem6val = IntVar()
        sem7val = IntVar()
        sem8val = IntVar()
        identry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=rollval, highlightthickness=1)
        identry.place(x=130, y=10)

        nameentry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=nameval, highlightthickness=1)
        nameentry.place(x=130, y=70)

        mobileentry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=mobileval, highlightthickness=1)
        mobileentry.place(x=130, y=130)

        emailentry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=emailval, highlightthickness=1)
        emailentry.place(x=130, y=190)

        addressentry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=addressval, highlightthickness=1)
        addressentry.place(x=130, y=250)

        dobentry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=dobval, highlightthickness=1)
        dobentry.place(x=160, y=370)

        sscentry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sscval, highlightthickness=1)
        sscentry.place(x=260, y=430)

        hscentry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=hscval, highlightthickness=1)
        hscentry.place(x=260, y=490)

        sem1entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem1val, highlightthickness=1)
        sem1entry.place(x=630, y=70)

        sem2entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem2val, highlightthickness=1)
        sem2entry.place(x=630, y=130)

        sem3entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem3val, highlightthickness=1)
        sem3entry.place(x=630, y=190)

        sem4entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem4val, highlightthickness=1)
        sem4entry.place(x=630, y=250)

        sem5entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem5val, highlightthickness=1)
        sem5entry.place(x=630, y=310)

        sem6entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem6val, highlightthickness=1)
        sem6entry.place(x=630, y=370)

        sem7entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem7val, highlightthickness=1)
        sem7entry.place(x=630, y=430)

        sem8entry = Entry(searchroot, font=("Times", 14), bd=1, textvariable=sem8val, highlightthickness=1)
        sem8entry.place(x=630, y=490)

        # --------------submit button---------------#

        searchbtn = Button(searchroot, text="Search", font=('Times', 20, 'bold'), width=20, bg='white', bd=1,
                           activeforeground="white", command=search, highlightthickness=1)
        searchbtn.place(x=313, y=550)

        searchroot.mainloop()

    def deletetudent():
        print("Student deleted :)")
        cc = studenttable.focus()
        content = studenttable.item(cc)
        pp = content['values'][0]
        res = messagebox.askyesnocancel('Notifications',
                                        'Do You Want To Delete {} Details Permanently ?'.format(pp))
        if (res == True):
            strr = "delete from studentdata where RollNo='{}'".format(pp)
            mycursor.execute(strr)
            con.commit()
            strr = 'select * from studentdata'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14],
                      i[15], i[16], i[17]]
                studenttable.insert('', END, values=vv)
            messagebox.showinfo('Notifications', 'Details Deleted Sucessfully !'.format(pp))
        else:
            print("deleted")

    def updatestudent():
        def update():
            conn = pymysql.connect(host='localhost', database='studentmanagementsystem1', user='root',
                                   password='Rohit@9324')
            # prepare a cursor object using cursor() method
            cursor = conn.cursor()

            RollNo = rollval.get()
            Name = nameval.get()
            MobileNo = mobileval.get()
            Emailid = emailval.get()
            Address = addressval.get()
            Gender = genderval.get()
            DOB = dobval.get()
            SSCResult = sscval.get()
            HSCResult = hscval.get()
            Branch = branchval.get()
            Sem1 = sem1val.get()
            Sem2 = sem2val.get()
            Sem3 = sem3val.get()
            Sem4 = sem4val.get()
            Sem5 = sem5val.get()
            Sem6 = sem6val.get()
            Sem7 = sem7val.get()
            Sem8 = sem8val.get()

            if (len(MobileNo) == 10 or MobileNo == ""):
                print("Phone accepted")
                # connect to MySQL database
                if ((re.match(r"[^@]+@[^@]+\.[^@]+", Emailid)) or Emailid == ""):

                    if SSCResult >= 0 and SSCResult <= 100 or SSCResult == "0":

                        if HSCResult >= 0 and HSCResult <= 100 or HSCResult == "0":

                            if Sem1 >= 0 and Sem1 <= 100 or Sem1 == "0":

                                if Sem2 >= 0 and Sem2 <= 100 or Sem2 == "0":

                                    if Sem3 >= 0 and Sem3 <= 100 or Sem3 == "0":

                                        if Sem4 >= 0 and Sem4 <= 100 or Sem4 == "0":

                                            if Sem5 >= 0 and Sem5 <= 100 or Sem5 == "0":

                                                if Sem6 >= 0 and Sem6 <= 100 or Sem6 == "0":

                                                    if Sem7 >= 0 and Sem7 <= 100 or Sem7 == "0":

                                                        if Sem8 >= 0 and Sem8 <= 100 or Sem8 == "0":
                                                            conn = pymysql.connect(host='localhost',
                                                                                   database='studentmanagementsystem1',
                                                                                   user='root',
                                                                                   password='Rohit@9324')
                                                            # prepare a cursor object using cursor() method
                                                            cursor = conn.cursor()
                                                            # prepare SQL query stringto insert a row
                                                            strr = "UPDATE studentdata SET Name=%s,MobileNo=%s,Emailid=%s,Address=%s,Gender=%s,DOB_MM_DD_YY=%s,SSCResult=%s,HSCResult=%s,Branch=%s,Sem1=%s,Sem2=%s,Sem3=%s,Sem4=%s,Sem5=%s,Sem6=%s,Sem7=%s,Sem8=%s WHERE Rollno = %s"

                                                            # execute the SQL query using execute() method
                                                            print("hello")
                                                            cursor.execute(strr, (
                                                                Name, MobileNo, Emailid, Address, Gender, DOB,
                                                                SSCResult, HSCResult, Branch, Sem1,
                                                                Sem2,
                                                                Sem3, Sem4, Sem5, Sem6, Sem7, Sem8, RollNo))
                                                            print("hello")
                                                            # save the changes to the database
                                                            conn.commit()
                                                            res = messagebox.askyesnocancel('Notifications',
                                                                                            'Roll No {} Details Modified Succesfully !\nDo u want to clear the form?'.format(
                                                                                                RollNo),
                                                                                            parent=updateroot)

                                                            strr = 'select * from studentdata'
                                                            print("DOne")

                                                            cursor.execute(strr)
                                                            print("DOne")

                                                            datas = cursor.fetchall()

                                                            print("DOne")
                                                            studenttable.delete(*studenttable.get_children())
                                                            print("DOne")
                                                            for i in datas:
                                                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                                                      i[7], i[8], i[9], i[10], i[11],
                                                                      i[12],
                                                                      i[13],
                                                                      i[14], i[15],
                                                                      i[16], i[17]]
                                                                studenttable.insert('', END, values=vv)
                                                            cursor.close()
                                                            conn.close()

                                                            print("hello")
                                                            print('1 row inserted.....')


                                                        else:
                                                            messagebox.showerror('Notifications',
                                                                                 'Invalid Percentage of Sem 8!\nPlease Enter Correct Percentage',
                                                                                 parent=updateroot)
                                                            sem8val.set('0')

                                                    else:
                                                        messagebox.showerror('Notifications',
                                                                             'Invalid Percentage of Sem 7 !\nPlease Enter Correct Percentage',
                                                                             parent=updateroot)
                                                        sem7val.set('0')

                                                else:
                                                    messagebox.showerror('Notifications',
                                                                         'Invalid Percentage of Sem 6 !\nPlease Enter Correct Percentage',
                                                                         parent=updateroot)
                                                    sem6val.set('0')

                                            else:
                                                messagebox.showerror('Notifications',
                                                                     'Invalid Percentage of Sem 5 !\nPlease Enter Correct Percentage',
                                                                     parent=updateroot)
                                                sem5val.set('0')

                                        else:
                                            messagebox.showerror('Notifications',
                                                                 'Invalid Percentage of Sem 4 !\nPlease Enter Correct Percentage',
                                                                 parent=updateroot)
                                            sem4val.set('0')

                                    else:
                                        messagebox.showerror('Notifications',
                                                             'Invalid Percentage of Sem 3 !\nPlease Enter Correct Percentage',
                                                             parent=updateroot)
                                        sem3val.set('0')

                                else:
                                    messagebox.showerror('Notifications',
                                                         'Invalid Percentage of Sem 2 !\nPlease Enter Correct Percentage',
                                                         parent=updateroot)
                                    sem2val.set('0')

                            else:
                                messagebox.showerror('Notifications',
                                                     'Invalid Percentage of Sem 1 !\nPlease Enter Correct Percentage',
                                                     parent=updateroot)
                                sem1val.set('0')

                        else:
                            messagebox.showerror('Notifications',
                                                 'Invalid Percentage of HSC !\nPlease Enter Correct Percentage',
                                                 parent=updateroot)
                            hscval.set('0')


                    else:
                        messagebox.showerror('Notifications',
                                             'Invalid Percentage of SSC !\nPlease Enter Correct Percentage',
                                             parent=updateroot)
                        sscval.set('0')


                else:
                    messagebox.showerror('Notifications', 'Invalid Email Id !\nPlease Enter Correct Email Id',
                                         parent=updateroot)

                    emailval.set('')

            else:
                messagebox.showerror('Notifications', 'Invalid Phone Number !\nPlease Enter Correct Number',
                                     parent=updateroot)

                mobileval.set('')

        updateroot = Toplevel(master=ShowDataFrame)
        updateroot.grab_set()
        updateroot.geometry("913x615+460+135")
        updateroot.title("Update Student Details")
        updateroot.config(bg='white')
        updateroot.iconbitmap('icon.ico')
        updateroot.resizable(False, False)
        DataEntryFrame2 = Frame(updateroot, bg="white", relief=GROOVE, borderwidth=2, bd=1)
        DataEntryFrame2.place(x=0, y=0, width=457, height=540)

        idlabel = Label(updateroot, text="Roll No : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=10, y=10)
        idlabel = Label(updateroot, text="Full Name: ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=70)
        idlabel = Label(updateroot, text="Mobile no : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=130)
        idlabel = Label(updateroot, text="Email id : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=190)
        idlabel = Label(updateroot, text="Address : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=250)
        idlabel = Label(updateroot, text="Gender : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=10)
        idlabel.place(x=10, y=310)
        idlabel = Label(updateroot, text="Date Of Birth : ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=14)
        idlabel.place(x=10, y=370)
        idlabel = Label(updateroot, text="SSC Result in Percentage: ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=26)
        idlabel.place(x=10, y=430)
        idlabel = Label(updateroot, text="HSC Result in Percentage: ", bg="white smoke", font=("Times", 15), bd=0,
                        relief=GROOVE,
                        borderwidth=2, width=26)
        idlabel.place(x=10, y=490)
        # ----------frame for right part---------------#
        DataEntryFrame3 = Frame(updateroot, bg="white", relief=GROOVE, borderwidth=2, bd=2)
        DataEntryFrame3.place(x=457, y=0, width=1200, height=541)

        idlabel = Label(updateroot, text="Branch : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=10)
        idlabel = Label(updateroot, text="Sem 1 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=70)
        idlabel = Label(updateroot, text="Sem 2 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=130)
        idlabel = Label(updateroot, text="Sem 3 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=190)
        idlabel = Label(updateroot, text="Sem 4 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=250)
        idlabel = Label(updateroot, text="Sem 5 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=310)
        idlabel = Label(updateroot, text="Sem 6 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=370)
        idlabel = Label(updateroot, text="Sem 7 : ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=430)
        idlabel = Label(updateroot, text="Sem 8: ", bg="white smoke", font=("Times", 15), bd=0, relief=GROOVE,
                        borderwidth=2, width=9)
        idlabel.place(x=510, y=490)

        # -------------------------- add student entry boxes---------------------------3
        rollval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        addressval = StringVar()
        genderval = StringVar()
        genderval.set("                         ")
        options = ["Male",
                   "Female",
                   "Other"]
        drop = OptionMenu(updateroot, genderval, *options)
        drop.pack()
        drop.place(x=130, y=310)
        dobval = StringVar()
        sscval = IntVar()
        hscval = IntVar()
        branchval = StringVar()
        branchval.set("                       ")
        options1 = ["INFT",
                    "EXTC",
                    "CMPN",
                    "ETRX",
                    "BIOMED",
                    "EXCS"]
        drop1 = OptionMenu(updateroot, branchval, *options1)
        drop1.pack()  # dropdown
        drop1.place(x=630, y=10)
        sem1val = IntVar()
        sem2val = IntVar()
        sem3val = IntVar()
        sem4val = IntVar()
        sem5val = IntVar()
        sem6val = IntVar()
        sem7val = IntVar()
        sem8val = IntVar()
        identry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=rollval, highlightthickness=1)
        identry.place(x=130, y=10)

        nameentry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=nameval, highlightthickness=1)
        nameentry.place(x=130, y=70)

        mobileentry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=mobileval, highlightthickness=1)
        mobileentry.place(x=130, y=130)

        emailentry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=emailval, highlightthickness=1)
        emailentry.place(x=130, y=190)

        addressentry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=addressval, highlightthickness=1)
        addressentry.place(x=130, y=250)

        dobentry = DateEntry(updateroot, font=("Times", 16), background="black", disabledbackground="black",
                             bordercolor="black", headersbackground="black", normalbackground="white",
                             foreground='black',
                             normalforeground='black', headersforeground='black', bd=0, textvariable=dobval,
                             selectmode='day')
        dobentry.config(background="black")
        dobentry.grid(row=1, column=1, padx=15)
        dobentry.place(x=160, y=370)
        dobval.set("")

        sscentry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sscval, highlightthickness=1)
        sscentry.place(x=260, y=430)

        hscentry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=hscval, highlightthickness=1)
        hscentry.place(x=260, y=490)

        sem1entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem1val, highlightthickness=1)
        sem1entry.place(x=630, y=70)

        sem2entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem2val, highlightthickness=1)
        sem2entry.place(x=630, y=130)

        sem3entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem3val, highlightthickness=1)
        sem3entry.place(x=630, y=190)

        sem4entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem4val, highlightthickness=1)
        sem4entry.place(x=630, y=250)

        sem5entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem5val, highlightthickness=1)
        sem5entry.place(x=630, y=310)

        sem6entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem6val, highlightthickness=1)
        sem6entry.place(x=630, y=370)

        sem7entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem7val, highlightthickness=1)
        sem7entry.place(x=630, y=430)

        sem8entry = Entry(updateroot, font=("Times", 14), bd=1, textvariable=sem8val, highlightthickness=1)
        sem8entry.place(x=630, y=490)

        # --------------submit button---------------#

        searchbtn = Button(updateroot, text="Update", font=('Times', 20, 'bold'), width=20, bg='white', bd=1,
                           activeforeground="white", command=update, highlightthickness=1)
        searchbtn.place(x=313, y=550)
        cc = studenttable.focus()
        content = studenttable.item(cc)
        pp = content['values']
        if (len(pp) != 0):
            rollval.set(pp[0])
            nameval.set(pp[1])
            mobileval.set(pp[2])
            emailval.set(pp[3])
            addressval.set(pp[4])
            genderval.set(pp[5])
            dobval.set(pp[6])
            sscval.set(pp[7])
            hscval.set(pp[8])
            branchval.set(pp[9])
            sem1val.set(pp[10])
            sem2val.set(pp[11])
            sem3val.set(pp[12])
            sem4val.set(pp[13])
            sem5val.set(pp[14])
            sem6val.set(pp[15])
            sem7val.set(pp[16])
            sem8val.set(pp[17])

        updateroot.mainloop()

    def showstudent():
        conn = pymysql.connect(host='localhost', database='studentmanagementsystem1', user='root',
                               password='Rohit@9324')
        # prepare a cursor object using cursor() method
        cursor = conn.cursor()
        strr = 'select * from studentdata'
        cursor.execute(strr)
        datas = cursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14],
                  i[15], i[16], i[17]]
            studenttable.insert('', END, values=vv)
        print("Student show")



    # -------------------------------Exit Button Working---------------------------#
    def exitstudent():
        res = messagebox.askyesnocancel("Notification", "Do u want to exit ?")
        if (res == True):
            root.destroy()

    # ------------------------------------buttons  creation -------------------------------------#

    frontlabel = Label(DataEntryFrame1, text="Menu", bg="white", font=("roman", 22, "bold"), bd=0,
                       relief=GROOVE,
                       borderwidth=0, width=32)
    frontlabel.pack(side=TOP, expand=TRUE)
    addbtn = Button(DataEntryFrame1, text='Add Student', font=("roman", 15, "bold"), width=32, bd=1,
                    highlightthickness=0, bg="white", highlightcolor="white", command=addstudent)
    addbtn.pack(side=TOP, expand=TRUE)
    searchbtn = Button(DataEntryFrame1, text='Search Student', width=32, font=('roman', 15, 'bold'), bg='white',
                       borderwidth=1, bd=0, command=searchstudent)
    searchbtn.pack(side=TOP, expand=TRUE)
    delbtn = Button(DataEntryFrame1, text='Delete Student', width=32, font=('roman', 15, 'bold'), bg='white',
                    borderwidth=1, bd=0, command=deletetudent)
    delbtn.pack(side=TOP, expand=TRUE)
    updatebtn = Button(DataEntryFrame1, text='Update Student', width=32, font=('roman', 15, 'bold'), bg='white',
                       borderwidth=1, bd=0, command=updatestudent)
    updatebtn.pack(side=TOP, expand=TRUE)
    showbtn = Button(DataEntryFrame1, text='Show All', width=32, font=('roman', 15, 'bold'), bg='white', bd=0,
                     borderwidth=1, command=showstudent)
    showbtn.pack(side=TOP, expand=TRUE)
    def expp():
        global ff


        res = messagebox.askyesnocancel("Notifications","Do u want Export the data")
        if res == True:
            print("hello")
            print("byeee")

            gg = studenttable.get_children()
            print("hello")

            Rollno, Name, Mobileno, Emailid, Address, Gender, DOB, SSCResult, HSCResult, Branch, Sem1, Sem2, Sem3, Sem4, Sem5, Sem6, Sem7, Sem8 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
            try:
                ff = fd.asksaveasfilename(defaultextension=".xlsx",
                                          initialdir='/Users/rohitnagula/Documents/Corel Cloud',
                                          filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")]
                                          )
                print("hello")

                for i in gg:
                    print("for loop")
                    content = studenttable.item(i)
                    pp = content["values"]
                    print("hello")
                    Rollno.append(pp[0]), Name.append(pp[1]), Mobileno.append(pp[2]), Emailid.append(
                        pp[3]), Address.append(
                        pp[4]), Gender.append(pp[5]), DOB.append(pp[6]), SSCResult.append(pp[7]), HSCResult.append(
                        pp[8]), Branch.append(pp[9]), Sem1.append(pp[10]), Sem2.append(pp[11]), Sem3.append(
                        pp[12]), Sem4.append(pp[13]), Sem5.append(pp[14]), Sem6.append(pp[15]), Sem7.append(
                        pp[16]), Sem8.append(pp[17])
                    dd = ["Roll No", "Name", "Mobile No", "Email id", "Address", "Gender", "D.O.B", "SSC Result",
                          "HSC Result", "Branch", "Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6", "Sem 7",
                          "Sem 8"]
                    df = pandas.DataFrame(list(
                        zip(Rollno, Name, Mobileno, Emailid, Address, Gender, DOB, SSCResult, HSCResult, Branch, Sem1,
                            Sem2,
                            Sem3, Sem4, Sem5, Sem6, Sem7, Sem8)), columns=dd)
                    print("hello")
                    print(df)
                    paths = r'{}.xlsx'.format(ff)
                    print("hello")
                    df.to_excel(paths, index=False)
                messagebox.showinfo('Notification', 'Student Data Saved'.format(ff))
            except:
                print("ghgh")


        else :
            print("Hello")
    exportbtn = Button(DataEntryFrame1, text='Export Data', width=32, font=('roman', 15, 'bold'), bg='white',
                       borderwidth=1, bd=0, command=expp)
    exportbtn.pack(side=TOP, expand=TRUE)
    exitbtn = Button(DataEntryFrame1, text='Exit', width=32, borderwidth=1, font=('roman', 15, 'bold'), bg="white",
                     bd=0, command=exitstudent)
    exitbtn.pack(side=TOP, expand=TRUE)
    connect = Connectdatabase()

    root.mainloop()



# Create the username label and entry
username_label = tk.Label(root1, text="Username:")
username_label.place(relx=0.3, rely=0.4, anchor="center")
username_entry = tk.Entry(root1)
username_entry.place(relx=0.5, rely=0.4, anchor="center")

# Create the password label and entry
password_label = tk.Label(root1, text="Password:")
password_label.place(relx=0.3, rely=0.5, anchor="center")
password_entry = tk.Entry(root1, show="*")
password_entry.place(relx=0.5, rely=0.5, anchor="center")

# Create the login button
login_button = tk.Button(root1, text="Login", bd=0, command=validate_login)
login_button.place(relx=0.5, rely=0.6, anchor="center")

# Create the result label
result_label = tk.Label(root1, text="")
result_label.place(relx=0.5, rely=0.7, anchor="center")

# Run the main loop
root1.mainloop()
