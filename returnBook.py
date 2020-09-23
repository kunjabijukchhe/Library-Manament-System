from tkinter import *
from tkinter import messagebox
import os, sys
import pymysql
from datetime import datetime, date

py = sys.executable


class ret(Tk):
    def __init__(self):
        super().__init__()

        self.title("Return Book")

        self.resizable(width=False, height=False)
        self.geometry('350x180')

        self.configure(bg="#343a40")
        # self.canvas = Canvas(width=500, height=417, bg='#343a40')
        # self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def qui():
            if len(a.get()) == '0':
                messagebox.showerror("Error", "Please Enter The Book Id")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_id from issue_book where return_date = '' and book_id = %s",
                                          [a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_id = %s",
                                              [idate, a.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Succesfully Returned')
                        d = messagebox.askyesno("Confirm", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'ret.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except:
                    messagebox.showerror("Error", "Something Goes Wrong")

        Label(self, text='Return Book', fg='black', bg="#20c997", font=("Helvetica Neue", 20, 'bold')).place(x=80, y=25)
        Label(self, text='Enter Book ID:', bg="#343a40",fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=10, y=100)
        e = Entry(self, font=("Helvetica Neue", 12), textvariable=a, width=40)
        e.place(x=160, y=100, height=30, width=40)
        b = Button(self, text="Return", bg='#28a745',fg='#f9f9f9', height=1, width=10, font=("Helvetica Neue", 12, 'bold'), command=qui)
        b.place(x=220, y=98)


ret().mainloop()