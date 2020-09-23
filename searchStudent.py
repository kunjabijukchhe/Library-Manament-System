from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Student")

        self.resizable(width=False, height=False)
        self.geometry('780x350')

        self.configure(bg="#343a40")

        self.lableOne = Label(self, text="Search Student", fg='black', bg="#20c997", font=("Helvetica Neue", 20, 'bold'))
        self.lableOne.place(x=290, y=40)

        self.lableTwo = Label(self, text="Search By:", bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 15, 'bold'))
        self.lableTwo.place(x=180, y=100)

        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))

        def ge():
            if (len(self.entry.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(self.combo.get())) == 0:
                messagebox.showinfo('Error', 'Enter the ' + self.combo.get())
            elif self.combo.get() == 'Name':
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.mycursor = self.conn.cursor()
                    name = self.entry.get()
                    self.mycursor.execute("Select * from student where name like %s", ['%' + name + '%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Name not found")
                except:
                    messagebox.showerror("Error", "Something goes wrong")
            elif self.combo.get() == 'ID':
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.mycursor = self.conn.cursor()
                    id = self.entry.get()
                    self.mycursor.execute("Select * from student where stud_id like %s", ['%' + id + '%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Id not found")
                except:
                    messagebox.showerror("Error", "Something goes wrong")

        self.b = Button(self, text="Find", bg='#28a745',fg='#f9f9f9', height=2, width=10, font=("Helvetica Neue", 12, 'bold'), command=ge)
        self.b.place(x=520, y=115)
        self.combo = ttk.Combobox(self, font=("Helvetica Neue", 12), textvariable=g, values=["Name", "ID"], state="readonly")
        self.combo.place(x=310, y=102, height=30, width=175)
        self.entry = Entry(self, font=("Helvetica Neue", 12), textvariable=f)
        self.entry.place(x=310, y=144, height=30, width=175)

        self.la = Label(self, text="Enter:", bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 15, 'bold'))
        self.la.place(x=180, y=140)



        self.listTree = ttk.Treeview(self, height=5, columns=('Student Name', 'Phone Number', 'Address'))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Student ID', anchor='w')
        self.listTree.column("#0", width=100, anchor='w')
        self.listTree.heading("Student Name", text='Student Name')
        self.listTree.column("Student Name", width=200, anchor='center')
        self.listTree.heading("Phone Number", text='Phone Number')
        self.listTree.column("Phone Number", width=200, anchor='center')
        self.listTree.heading("Address", text='Address')
        self.listTree.column("Address", width=200, anchor='center')
        self.listTree.place(x=40, y=200)

        ttk.Style().configure("Treeview", font=('Times new Roman', 15))


Search().mainloop()