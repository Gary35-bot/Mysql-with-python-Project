import tkinter
from tkinter import ttk
import mysql.connector
from tkinter import *
from tkinter import  messagebox as mb

from PIL.XVThumbImagePlugin import r

root = Tk()

root.title("Management")
root.geometry("600x600")
root.config(bg="#2e8bc0")

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_sign_in', auth_plugin='mysql_native_password')

mycursor = mydb.cursor()



tree = ttk.Treeview(root)
tree['show'] = 'headings'

s = ttk.Style(root)
s.theme_use("clam")

tree["columns"] = ("Client_id", "Name", "Surname", "Phone_number", "Password", "Start_in_date", "Start_in_time")


tree.column("Name", width=100, minwidth=100, anchor=tkinter.CENTER)
tree.column("Surname", width=50, minwidth=150, anchor=tkinter.CENTER)
tree.column("Phone_number", width=150, minwidth=150, anchor=tkinter.CENTER)
tree.column("Password", width=150, minwidth=150, anchor=tkinter.CENTER)
tree.column("Start_in_date", width=150, minwidth=150, anchor=tkinter.CENTER)
tree.column("Start_in_time", width=150, minwidth=150, anchor=tkinter.CENTER)

tree.heading("Client_id", text="Client_id", anchor=tkinter.CENTER)
tree.heading("Name", text="Name", anchor=tkinter.CENTER)
tree.heading("Surname", text="Surname", anchor=tkinter.CENTER)
tree.heading("Phone_number", text="Phone_number", anchor=tkinter.CENTER)
tree.heading("Password", text="Password", anchor=tkinter.CENTER)
tree.heading("Start_in_date", text="Start_in_date", anchor=tkinter.CENTER)
tree.heading("Start_in_time", text="Start_in_time", anchor=tkinter.CENTER)


xy = mycursor.execute("Select * from Clientle ORDER BY client_id")
global count
counter = 0
for i in mycursor:
    if counter % 2 == 0:
        tree.insert(parent="", index=counter, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5],))
    else:
        tree.insert(parent="", index=counter, values=(i[0], i[1], i[2], i[3], i[4], i[5]))
    counter += 1

hsb = ttk.Scrollbar(root, orient="horizontal")

hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X, side=BOTTOM)

tree.pack()
name = tkinter.StringVar()
surname = tkinter.StringVar()
phone = tkinter.IntVar()
password = tkinter.StringVar



def add_data():
    add_frame = Frame(root, width=600, height=320, background="grey")
    add_frame.place(x=10, y=250)

    name_label = Label(root, text="Name", bg="#2e8bc0")
    name_label.place(x=130, y=250)
    surname_label = Label(root, text="Surname", bg="#2e8bc0")
    surname_label.place(x=240, y=250)
    phone_label = Label(root, text="Phone no.", bg="#2e8bc0")
    phone_label.place(x=350, y=250)
    password_label = Label(root, text="Password", bg="#2e8bc0")
    password_label.place(x=470, y=250)

    name_box = Entry(root, width=10, textvariable=name)
    name_box.place(x=130, y=280)
    surname_box = Entry(root, width=10, textvariable=surname)
    surname_box.place(x=240, y=280)
    phone_box = Entry(root, width=10, textvariable=phone)
    phone_box.place(x=350, y=280)
    password_box = Entry(root, width=10, textvariable=password)
    password_box.place(x=470, y=280)

    def insert_data():
        nonlocal name_box, surname_box, phone_box, password_box
        s_name = name.get()
        sur = surname.get()
        p = phone_box.get()
        pass_w = password_box.get()
        mycursor.execute('INSERT INTO Clientle(name, surname, phone_number, password) VALUES(%s, %s, %s, %s)', (s_name, sur, p, pass_w))

        print(mycursor.lastrowid)
        mydb.commit()
        tree.insert('', 'end', text="", values=(mycursor.lastrowid, s_name, sur, p, pass_w))
        mb.showinfo("Success")

    btn = Button(root, text="submit", command=insert_data)
    btn.place(x=250, y=400)
    btn1 = Button(root, text="Cancel")
    btn1.place(x=350, y=400)

def delete_col():
    selected_items = tree.selection()[0]
    print(tree.item(selected_items)['values'])
    uid = tree.item(selected_items)['values'][0]
    del_query = "DELETE FROM Clientle WHERE Client_id=%s"
    sel_data = (uid,)
    mycursor.execute(del_query, sel_data)
    mydb.commit()
    tree.delete(selected_items)
    mb.showinfo("success", "deleted successfully")


add_record = Button(root, text="Add record", command=add_data)
add_record.place(x=250, y=350)

delete_button = tkinter.Button(root, text="delete", command=delete_col)
delete_button.place(x=350, y=350)

root.mainloop()
