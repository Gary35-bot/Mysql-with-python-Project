import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter. font as font

root = Tk()
root.title("Register")
root.geometry("500x400")
root.config(bg="#2e8bc0")
root.resizable(0, 0)


class Register:
    def __init__(self, mastery):
        self.hed_label = Label(mastery, text="Fill In The Following To Register", font="bold", bg="#2e8bc0")
        self.hed_label.place(x=135, y=5)
        self.name_label = Label(mastery, text="Name:", bg="#2e8bc0")
        self.name_label.place(x=20, y=50)
        self.entry_name = Entry(mastery)
        self.entry_name.place(x=20, y=80)
        self.surname_label = Label(mastery, text="Surname:", bg="#2e8bc0")
        self.surname_label.place(x=20, y=110)
        self.entry_surname = Entry(mastery)
        self.entry_surname.place(x=20, y=140)
        self.ID_number_label = Label(mastery, text="ID Number:", bg="#2e8bc0")
        self.ID_number_label.place(x=20, y=170)
        self.entry_ID_number = Entry(mastery)
        self.entry_ID_number.place(x=20, y=200)
        self.phone_number_label = Label(mastery, text="Phone Number:", bg="#2e8bc0")
        self.phone_number_label.place(x=20, y=230)
        self.entry_phone_number = Entry(mastery)
        self.entry_phone_number.place(x=20, y=260)

        self.label_next_kin = Label(mastery, text="Next of Kin Details")
        self.label_next_kin.place(x=300, y=50)
        self.name_label1 = Label(mastery, text="Name:")
        self.name_label1.place(x=300, y=100)
        self.entry_name_label1 = Entry(mastery)
        self.entry_name_label1.place(x=300, y=130)
        self.surname_label1 = Label(mastery, text="Surname:")
        self.surname_label1.place(x=300, y=160)
        self.entry_surname_label1 = Entry(mastery)
        self.entry_surname_label1.place(x=300, y=190)
        self.mobile_label = Label(mastery, text="Mobile Number:")
        self.mobile_label.place(x=300, y=220)
        self.mobile_entry = Entry(mastery)
        self.mobile_entry.place(x=300, y=260)


x = Register(root)
root.mainloop()