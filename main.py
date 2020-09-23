from tkinter import *
from tkinter import messagebox
import os
import pymysql

py = sys.executable


# creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.resizable(width=False, height=False)
        self.geometry('600x400')
        self.configure(bg="#343a40")
        self.title("LIBRARY MANAGEMENT SYSTEM")

        # verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ', (user, password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'container.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except:
                    messagebox.showinfo('Error', "Something Goes Wrong,Try restarting")
        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to quit?")
            if conf:
                self.destroy()


        def check():

            self.label = Label(self, text="ADMIN LOGIN", bg='#17a2b8', fg='#f8f9fa', font=("Helvetica Neue", 20, 'bold'))
            self.label.place(x=200, y=110)

            self.label1 = Label(self, text="Username:", bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 18, 'bold'))
            self.label1.place(x=100, y=180)

            self.user_text = Entry(self, font=("Helvetica Neue", 12), textvariable=self.a)
            self.user_text.place(x=250, y=185, height=30, width=175)

            self.label2 = Label(self, text="Password:", bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 18, 'bold'))
            self.label2.place(x=100, y=250)

            self.pass_text = Entry(self, show='*', font=("Helvetica Neue", 12), textvariable=self.b, width=30)
            self.pass_text.place(x=250, y=250, height=30, width=175)

            self.butt = Button(self, text="Login",bg='#007bff',fg='#f9f9f9', font=("Helvetica Neue", 12, 'bold'), width=10, height=2,
                               command=chex)
            self.butt.place(x=160, y=320)

            self.button_quit = Button(self, text="Quit", bg='#dc3545',fg='#f9f9f9', width=10, height=2,
                                      font=("Helvetica Neue", 12, 'bold'), command=log)
            self.button_quit.place(x=310, y=320)

            self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg="#17a2b8",fg='#f8f9fa',
                                font=("Helvetica Neue", 24, 'bold'))
            self.label3.place(x=40, y=30)

        check()


Lib().mainloop()

