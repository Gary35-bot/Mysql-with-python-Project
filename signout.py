import tkinter
from tkinter import ttk
import mysql.connector
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("signed")
root.geometry("200x200")
root.config(bg="#2e8bc0")
root.resizable(0, 0)


def sign_out():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_sign_in', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()

    xy = mycursor.execute("Select * from Clientle")
    verified = False
    for i in mycursor:
        verified = TRUE
        timer = "UPDATE Clientle SET Leave_date = curdate(), Leave_time = curtime() WHERE Client_id = " + str(i[0])
        mycursor.execute(timer)
        mydb.commit()
    if verified:
        messagebox.showinfo("logged_out Successfully! Enjoy the Evening")
    elif not verified:
        messagebox.showinfo("Fail", "The information you typed in is wrong")


def back_main():
    import main


btn = Button(root, text="sign_out", command=sign_out)
btn.place(x=20, y=50)
btn1 = Button(root, text="return to main", command=back_main)
btn1.place(x=20, y=100)

root.mainloop()
