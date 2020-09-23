from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
import os
import sys
import pymysql

py = sys.executable


# creating window
class issue(Tk):
    def __init__(self):
        super().__init__()
        self.title('Issue Book')
        self.resizable(width=False, height=False)
        self.geometry('400x300')

        self.configure(bg="#343a40")

        c = StringVar()
        d = StringVar()

        # verifying input
        def isb():
            if (len(c.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            elif (len(d.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select availability from book where availability = 'YES' and book_id = %s",
                                          [c.get()])
                    self.pc = self.mycursor.fetchall()
                    try:
                        if self.pc:
                            print("success")
                            book = c.get()
                            stud = d.get()
                            now = datetime.now()
                            idate = now.strftime('%Y-%m-%d %H:%M:%S')
                            self.mycursor.execute(
                                "Insert into issue_book(book_id,stud_id,issue_date,return_date) values (%s,%s,%s,%s)",
                                [book, stud, idate, ''])
                            self.conn.commit()
                            self.mycursor.execute("Update book set availability = 'NO' where book_id = %s", [book])
                            self.conn.commit()
                            messagebox.showinfo("Success", "Successfully Issue!")
                            ask = messagebox.askyesno("Confirm", "Do you want to add another?")
                            if ask:
                                self.destroy()
                                os.system('%s %s' % (py, 'issueTable.py'))
                            else:
                                self.destroy()
                        else:
                            messagebox.showinfo("Oop's", "Book id " + c.get() + " is not available")
                    except:
                        messagebox.showerror("Error", "Check The Details")
                except:
                    messagebox.showerror("Error", "Something goes wrong")

        # label and input box
        Label(self, text='Book Issuing', fg='black', bg="#20c997", font=("Helvetica Neue", 20, 'bold')).place(x=130, y=40)
        Label(self, text='Book ID:', bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 15, 'bold')).place(x=55, y=100)

        e1 = Entry(self, font=("Helvetica Neue", 12), textvariable=c)
        e1.place(x=160, y=105, height=30, width=175)

        Label(self, text='Student ID:', bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 15, 'bold')).place(x=20, y=150)

        e2 = Entry(self, font=("Helvetica Neue", 12), textvariable=d)
        e2.place(x=160, y=152, height=30, width=175)

        b = Button(self, text="Issue", bg='#28a745',fg='#f9f9f9', height=2, width=10, font=("Helvetica Neue", 12, 'bold'), command=isb)
        b.place(x=150, y=220)


issue().mainloop()
