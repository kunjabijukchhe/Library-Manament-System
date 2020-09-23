from tkinter import *
from tkinter import messagebox
import os
import sys
import pymysql
from tkinter import ttk

py = sys.executable


# creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)
        self.geometry('780x525')
        self.configure(bg="#343a40")
        self.title("LIBRARY MANAGEMENT SYSTEM")

        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)

        # calling scripts
        def a_s():
            os.system('%s %s' % (py, 'addStudent.py'))

        def a_b():
            os.system('%s %s' % (py, 'addBook.py'))

        def r_b():
            os.system('%s %s' % (py, 'removeBook.py'))

        def r_s():
            os.system('%s %s' % (py, 'removeStudent.py'))

        def ib():
            os.system('%s %s' % (py, 'issueBook.py'))

        def ret():
            os.system('%s %s' % (py, 'returnBook.py'))

        def sea():
            os.system('%s %s' % (py, 'searchBook.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to quit?")
            if conf:
                self.destroy()
                os.system('%s %s' % (py, 'main.py'))


        def add_user():
            os.system('%s %s' % (py, 'addUser.py'))

        def rem_user():
            os.system('%s %s' % (py, 'removeUser.py'))

        def sest():
            os.system('%s %s' % (py, 'searchStudent.py'))

        # creating table

        self.listTree = ttk.Treeview(self, height=6, columns=('Student', 'Book', 'Issue Date', 'Return Date'))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self, orient="horizontal", command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='Issue ID')
        self.listTree.column("#0", width=50, minwidth=50, anchor='center')
        self.listTree.heading("Student", text='Student')
        self.listTree.column("Student", width=200, minwidth=200, anchor='center')
        self.listTree.heading("Book", text='Book')
        self.listTree.column("Book", width=200, minwidth=200, anchor='center')
        self.listTree.heading("Issue Date", text='Issue Date')
        self.listTree.column("Issue Date", width=108, minwidth=108, anchor='center')
        self.listTree.heading("Return Date", text='Return Date')
        self.listTree.column("Return Date", width=108, minwidth=108, anchor='center')
        self.listTree.place(x=50, y=350)
        # self.vsb.place(x=720, y=350, height=145)
        # self.hsb.place(x=50,y=650,width=700)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        list1 = Menu(self, bg='#495057', fg='#f9f9f9', font=('Helvetica Neue', 12, 'bold'))
        list1.add_command(label="Add Book", command=a_b)
        list1.add_command(label="Remove Book", command=r_b)

        list2 = Menu(self, bg='#495057', fg='#f9f9f9', font=('Helvetica Neue', 12, 'bold'))
        list2.add_command(label="Add Student", command=a_s)
        list2.add_command(label="Remove Student", command=r_s)

        list3 = Menu(self, bg='#495057', fg='#f9f9f9', font=('Helvetica Neue', 12, 'bold'))
        list3.add_command(label="Add Librarian", command=add_user)
        list3.add_command(label="Remove Librarian", command=rem_user)

        self.mymenu.add_cascade(label='Book', menu=list1)
        self.mymenu.add_cascade(label='Student', menu=list2)
        self.mymenu.add_cascade(label='Admin Tools', menu=list3)

        self.config(menu=self.mymenu)

        def ser():
            if (len(self.studid.get()) == 0):
                messagebox.showinfo("Error", "Empty Field!")
            else:

                try:
                    conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    cursor = conn.cursor()
                    change = int(self.studid.get())
                    cursor.execute(
                        "Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id and s.stud_id = %s",
                        [change])
                    pc = cursor.fetchall()
                    if pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in pc:
                            self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
                    else:
                        messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
                except:
                    # print(Error)
                    messagebox.showerror("Error", "Something Goes Wrong")

        def ent():
            if (len(self.bookid.get()) == 0):
                messagebox.showinfo("Error", "Empty Field!")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.myCursor = self.conn.cursor()
                    book = int(self.bookid.get())
                    self.myCursor.execute(
                        "Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id and b.book_id = %s",
                        [book])
                    self.pc = self.myCursor.fetchall()
                    if self.pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in self.pc:
                            self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
                    else:
                        messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued")
                except:
                    messagebox.showerror("Error", "Something Goes Wrong")

        def check():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm", "Do you want to register a user")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'addUser.py'))
                else:
                    # label and input box
                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM', fg='black', bg="#20c997",
                                        font=('Helvetica Neue', 20, 'bold'))
                    self.label3.place(x=180, y=22)
                    self.label4 = Label(self, text="ENTER STUDENT ID:", bg="#343a40", fg='#f8f9fa',
                                        font=('Helvetica Neue', 15, 'bold'))
                    self.label4.place(x=50, y=100)

                    self.studid = Entry(self, font=("Helvetica Neue", 12), textvariable=self.a)
                    self.studid.place(x=280, y=100, height=30, width=175)

                    self.srt = Button(self, text='Search', bg='#28a745', fg='#f9f9f9', height=1, width=10,
                                      font=('Helvetica Neue', 12, 'bold'), command=ser).place(x=500, y=98)
                    self.label5 = Label(self, text="ENTER THE BOOK ID:", bg="#343a40", fg='#f8f9fa',
                                        font=('Helvetica Neue', 15, 'bold'))
                    self.label5.place(x=50, y=150)

                    self.bookid = Entry(self, font=("Helvetica Neue", 12), textvariable=self.b)
                    self.bookid.place(x=280, y=150, height=30, width=175)

                    self.brt = Button(self, text='Find', bg='#28a745', fg='#f9f9f9', height=1, width=10,
                                      font=('Helvetica Neue', 12, 'bold'), command=ent).place(x=500, y=148)
                    self.label6 = Label(self, text="INFORMATION DETAILS", bg='#17a2b8',
                                        font=('Helvetica Neue', 15, 'underline', 'bold'))
                    self.label6.place(x=250, y=300)

                    self.button = Button(self, text='Search Student', bg='#428bca', fg='#f9f9f9', height=2, width=12,
                                         font=('Helvetica Neue', 12, 'bold'), command=sest).place(x=50, y=220)
                    self.button = Button(self, text='Search Book', bg='#428bca', fg='#f9f9f9', height=2, width=10,
                                         font=('Helvetica Neue', 12, 'bold'), command=sea).place(x=215, y=220)
                    self.brt = Button(self, text="Issue Book", bg='#428bca', fg='#f9f9f9', height=2, width=10,
                                      font=('Helvetica Neue', 12, 'bold'), command=ib).place(x=360, y=220)
                    self.brt = Button(self, text="Return Book", bg='#428bca', fg='#f9f9f9', height=2, width=10,
                                      font=('Helvetica Neue', 12, 'bold'), command=ret).place(x=500, y=220)
                    self.brt = Button(self, text="Quit", bg='#dc3545', fg='#f9f9f9', height=2, width=10,
                                      font=('Helvetica Neue', 12, 'bold'), command=log).place(x=640, y=115)
            except:
                messagebox.showerror("Error", "Something Goes Wrong")

        check()


MainWin().mainloop()
