from tkinter import *
from contacts import *
from tkinter import messagebox
import os
from datetime import datetime

# Programmer Information
# Name: FNU Tripti
# A-ID: A20503656
# Course: ITMD-513
# Date: 07/18/2022
# Lab #: 7

def selection():
    print("At %s of %d" % (select.curselection(), len(contactlist)))
    return int(select.curselection()[0])


def addContact():
    contactlist.append([nameVar.get(), phoneVar.get()])
    setList()
    messagebox.showinfo(title="Add", message="Contacts Added successfully")


def updateContact():
    contactlist[selection()] = [nameVar.get(), phoneVar.get()]
    setList()
    messagebox.showinfo(title="Update", message="Contacts Updated successfully")


def deleteContact():
    if (
            messagebox.askokcancel(title="Delete",
                                   message="Are you sure you want to delete this contact?, OK or Cancel")) == 1:
        del contactlist[selection()]
        setList()


def loadContact():
    name, phone = contactlist[selection()]
    nameVar.set(name)
    phoneVar.set(phone)


# Code added to save the contents of a file
def saveContact():
    try:
        file = open('contacts.py', 'w')
        file.write("contactlist = [")

        for item in contactlist:
            file.write("%s" % item + ",")
        file.write("\n")
        file.write("]")
        file.close()
        setList()
        messagebox.showinfo(title="Save", message="Contacts Saved successfully")
    except IOError as e:
        print(e)


def exitContact():
    if (messagebox.askokcancel(title="Exit", message="Do you really want to quit?, OK or Cancel")) == 1:
        os._exit(1)


def buildFrame():
    print("This program for course ITMD-513 is executed by FNU Tripti (A20503656) on : ", datetime.now())
    global nameVar, phoneVar, select
    root = Tk()
    # Code added to show the title of the frame.
    root.title("My Contact List")

    frame1 = Frame(root)
    frame1.pack()

    Label(frame1, text="Name:").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Phone:").grid(row=1, column=0, sticky=W)
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame1 = Frame(root)  # add a row of buttons
    frame1.pack()
    btn1 = Button(frame1, text=" Add  ", command=addContact)
    btn2 = Button(frame1, text="Update", command=updateContact)
    btn3 = Button(frame1, text="Delete", command=deleteContact)
    btn4 = Button(frame1, text=" Load ", command=loadContact)
    btn5 = Button(frame1, text=" Save ", command=saveContact)
    btn1.pack(side=LEFT, padx=15, pady=15)
    btn2.pack(side=LEFT, padx=15, pady=15)
    btn3.pack(side=LEFT, padx=15, pady=15)
    btn4.pack(side=LEFT, padx=15, pady=15)
    btn5.pack(side=LEFT, padx=15, pady=15)

    frame1 = Frame(root)  # allow for selection of names
    frame1.pack()
    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=7)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH)

    frame1 = Frame(root)  # add a row for the exit button
    frame1.pack()

    btn6 = Button(frame1, text=" Exit ", command=exitContact)
    btn6.pack(side=BOTTOM, pady=15)

    return root


def setList():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


root = buildFrame()
setList()

root.mainloop()
