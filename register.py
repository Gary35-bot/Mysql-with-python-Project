from tkinter import *
import mysql.connector

root = Tk()
root.title("Register")
root.geometry("500x400")
root.config(bg="#2e8bc0")
root.resizable(0, 0)

# class created for the register


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
        self.password_label = Label(mastery, text="Create password:", bg="#2e8bc0")
        self.password_label.place(x=20, y=290)
        self.entry_password = Entry(mastery)
        self.entry_password.place(x=20, y=320)
    # next of kin details
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
        # buttons for register form
        self.btn3 = Button(mastery, text="Register", command=self.get_info)
        self.btn3.place(x=350, y=310)
        self.btn4 = Button(mastery, text="Return to main screen", command=self.back_main)
        self.btn4.place(x=310, y=350)

    def get_info(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_sign_in')
        mycursor = mydb.cursor()

        val = (self.entry_ID_number.get(), self.entry_name.get(), self.entry_surname.get(), self.entry_phone_number.get(), self.entry_password.get())
        sql = 'INSERT INTO Register_me(Id_number, Name, Surname, Phone_number, Password) \n VALUES(%s, %s, %s, %s, %s)'
        xy = mycursor.execute(sql, val)

        mydb.commit()

        val1 = (self.entry_name_label1.get(), self.entry_surname_label1.get(), self.mobile_entry.get())
        SQL1 = 'INSERT INTO My_nextkin(Name, Surname, Phone_number) \n VALUES(%s, %s, %s)'
        xy = mycursor.execute(SQL1, val1)

        mydb.commit()

        # insert = "INSERT INTO Register_me(Id_number ,Name, Surname, Phone_number, Password) VALUES (%s, %s, %s, %s, %s)"
        # val = (self.entry_ID_number.get(), self.entry_name.get(), self.entry_surname.get(), self.entry_phone_number.get(), self.entry_password.get())
        #
        # insert1 = "INSERT INTO My_nextkin(Name, Surname, Phone_number ) VALUES (%s, %s, %s)"
        # val1 = (self.entry_name_label1.get(), self.entry_surname_label1, self.mobile_entry.get())
        #
        # try:
        #     mycursor.execute(insert, val)
        #     mydb.commit()
        #     mycursor.execute(insert1, val1)
        #     mydb.commit(buffered=True)
        #
        #     messagebox.showinfo("Completed")
        # except:
        #     mycursor.execute('Select * from Register_me')
        #     mycursor.execute('Select * from My_nextkin')

        # does not show the screen
        # mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='Lifechoices_sign_in')
        # mycursor = mydb.cursor()
        #
        # val = (self.entry_ID_number.get(), self.entry_name.get(), self.entry_surname.get(), self.mobile_entry.get(), self.entry_password.get())
        # sql = "INSERT INTO Register_me(Client_id ,Name, Surname, Phone_number, Password) VALUES (%s, %s, %s, %s, %s)"
        # xy = mycursor.execute(sql, val)
        #
        # # next kin
        #
        # val = (self.entry_name_label1.get(), self.entry_surname_label1, self.mobile_entry.get())
        # sql = "INSERT INTO My_nextkin(Name, Surname, Phone_number ) VALUES (%s, %s, %s)"
        # xy = mycursor.execute(sql, val)
        #
        # xy = mycursor.execute("Select * from Clientle")
        # for i in mycursor:
        #     print(i)
        #     mydb.commit()

    def back_main(self):
        root.destroy()
        import main


x = Register(root)
root.mainloop()
