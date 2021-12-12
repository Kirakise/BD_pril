import mariadb
import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
try:
    conn = mariadb.connect(
            user="root",
            password="201070",
            host="0.0.0.0",
            port=3306,
            database="tables")
except mariadb.Error as e:
    print(e)
    sys.exit(1)

def callbackFunc(x):
    if cmb.get() == "Select" or cmb.get() == "Delete":
        lb.config(text = "FROM")
    if cmb.get() == "Update":
        lb.config(text = 'SET')
    if cmb.get() == "Insert":
        lb.config(text = "VALUES")
    if cmb.get() == "Alter/Add":
        lb.config(text = "Add")
    if cmb.get() == "Alter/Modify":
        lb.config(text = "Modify")

def showdb(x = 0):
    curs = conn.cursor()
    curs.execute("show tables;")
    if (x == 1):
        a = []
        for i in curs:
            for j in i:
                a.append(j)
        return a
    txt.delete(1.0, END)
    txt.insert(INSERT, "DATABASES :\n")
    for i in curs:
        for j in i:
            txt.insert(INSERT, j)
            txt.insert(INSERT, "\n")

def doexec():
    txt.delete(1.0, END)
    curs = conn.cursor()
    if cmb.get() == "Select" or cmb.get() == "Delete":
        try:
            curs.execute(cmb.get() + " " + txt1.get() + " " + lb.cget("text") + " " + txt2.get() + ";")
        except mariadb.Error as e:
            txt.insert(INSERT, e)
            return
    elif cmb.get() == "Insert":
        try:
            curs.execute("insert into" + " " + txt1.get() + " " + lb.cget("text") + " " + txt2.get() + ";")
        except mariadb.Error as e:
            txt.insert(INSERT, e)
            return
    elif cmb.get() == "Alter/Add":
        try:
            curs.execute("alter table" + " " + txt1.get() + " " + lb.cget("text") + " " + txt2.get() + ";")
        except mariadb.Error as e:
            txt.insert(INSERT, e)
            return
    elif cmb.get() == "Alter/Modify":
        try:
            curs.execute("alter table" + " " + txt1.get() + " " + lb.cget("text") + " " + txt2.get() + ";")
        except mariadb.Error as e:
            txt.insert(INSERT, e)
            return
    for i in curs:
        for j in i:
            txt.insert(INSERT, str(j) + "\t\t")
        txt.insert(INSERT, "\n")


def describe():
    curs = conn.cursor()
    if (cmb2.get() != ""):
        curs.execute("describe " + cmb2.get())
        txt.delete(1.0, END)
        for i in curs:
            for j in i:
                txt.insert(INSERT, str(j) + "\t\t")
            txt.insert(INSERT, "\n")

def showt():
    curs = conn.cursor()
    if (cmb2.get() != ""):
        curs.execute("select * from "  + cmb2.get())
        txt.delete(1.0, END)
        for i in curs:
            for j in i:
                txt.insert(INSERT, str(j) + "\t\t")
            txt.insert(INSERT, "\n")
root = Tk()
root.geometry('1200x720')


#Кнока дб
btn = Button(root, text = "Show db", command=showdb)
btn.grid(column=101, row = 0)


#Первый комбобокс
cmb = Combobox(root);
cmb.grid(column = 0, row = 51);
cmb['values'] = ("Select", "Delete", "Insert", "Update", "Alter/Add", "Alter/Modify")
cmb.bind("<<ComboboxSelected>>", callbackFunc)

#Второй комбобокс
lb = Label(root, text="")
lb.grid(column=2, row=51)

txt1 = Entry(root)
txt1.grid(column=1, row=51)

lb1 = Label(root, text = "")
lb1.grid(column=3, row = 51)

txt2 = Entry(root)
txt2.grid(column=4, row=51)

txt = scrolledtext.ScrolledText(root, width=100, height=50)
txt.grid(column=0, row=0, columnspan=5, rowspan=5)
txt.insert(INSERT,"asd");

cmb2 = Combobox(root);
cmb2['values'] = showdb(1)
cmb2.grid(column = 101, row = 1)

btn3 = Button(root, text = "Describe table", command=describe)
btn3.grid(column = 102, row = 1)

btn4 = Button(root, text = "Show table", command=showt)
btn4.grid(column = 102, row = 2)

btn2 = Button(root, text = "Exec", command=doexec)
btn2.grid(column=0, row = 52)

root.mainloop()

