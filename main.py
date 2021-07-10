import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter. font as font

root = Tk()
root.title("Main Screen")
root.geometry("500x400")
root.config(bg="#2e8bc0")
root.resizable(0, 0)

img = PhotoImage(file="forest-trees-aerial-view-road-wallpaper-preview.png")
canvas = Canvas(root, width=180, height=500)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=0, y=0)


class MainScreen:

    def __init__(self, mastery):
        self.heading_label = Label(mastery, text="Welcome", bg="#2e8bc0", font="bold")
        self.heading_label.place(x=300, y=50)
        self.username = Label(mastery, text="UserName:", bg="#2e8bc0")
        self.username.place(x=250, y=100)
        self.username_entry = Entry(mastery,)
        self.username_entry.place(x=250, y=130)
        self.password_label = Label(mastery, text="Password:", bg="#2e8bc0")
        self.password_label.place(x=250, y=160)
        self.password_label1 = Entry(mastery,)
        self.password_label1.place(x=250, y=190)

        self.btn = Button(mastery, text="Sign in", border=1, command=self.sign_in)
        self.btn.place(x=250, y=230)
        self.label_btn1 = Label(mastery, text="If You Do Not Have An \nAccount Click here.", bg="#3ACF3A",)
        self.label_btn1.place(x=20, y=150)
        self.btn1 = Button(mastery, text="Register?", foreground="#2e8bc0", font="bold",  command=self.listing)
        self.btn1.place(x=50, y=230)

    def sign_in(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_sign_in', auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

        xy = mycursor.execute("Select * from Clientle")
        verified = False
        for i in mycursor:
            print(i)
            if self.username_entry.get() == i[1] and self.password_label1.get() == i[4]:
                verified = TRUE
                timer = "UPDATE Clientle SET Start_in_date = curdate(), Start_in_time = curtime() WHERE Client_id = " + str(i[0])
                mycursor.execute(timer)
                mydb.commit()
        if verified:
            messagebox.showinfo("Successful! Enjoy the day")
        elif not verified:
            messagebox.showinfo("Fail", "The information you typed in is wrong")

    def listing(self):
        root.destroy()
        import register


x = MainScreen(root)
root.mainloop()
