from tkinter import *
from tkinter import messagebox
import os
import sys
import pymysql

py = sys.executable


# creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)
        self.geometry('400x275')

        self.configure(bg="#343a40")

        self.title('Add Book')

        a = StringVar()
        b = StringVar()
        c = StringVar()

        # verifying Input
        def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("Error", "Please Enter The Details")
            else:
                g = 'YES'
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(name,author,availability) values (%s,%s,%s)",
                                          [b.get(), c.get(), g])
                    self.conn.commit()

                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'addBook.py'))
                    else:
                        self.destroy()
                except:
                    messagebox.showerror("Error", "Check The Details")

        # creating input box and label

        Label(self, text='Book Details', fg='black', bg="#20c997", font=('Helvetica Neue', 20, 'bold')).place(x=130, y=22)

        Label(self, text='Book Name:', bg="#343a40",fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=40, y=82)
        e1 = Entry(self, font=("Helvetica Neue", 12), textvariable=b, width=30)
        e1.place(x=180, y=80, height=30, width=175)
        Label(self, text='Book Author:', bg="#343a40",fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=40, y=130)
        e2 = Entry(self, font=("Helvetica Neue", 12), textvariable=c, width=30)
        e2.place(x=180, y=130, height=30, width=175)
        Button(self, text="Submit", bg='#28a745',fg='#f9f9f9',  height=2, width=10, font=("Helvetica Neue", 12, 'bold'), command=b_q).place(
            x=150, y=200)


Add().mainloop()