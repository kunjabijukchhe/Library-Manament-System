from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Book")

        self.resizable(width=False, height=False)
        self.geometry('780x350')

        self.configure(bg="#343a40")

        lableOne = Label(self, text="Search Book", fg='black', bg="#20c997", font=("Helvetica Neue", 20, 'bold'))
        lableOne.place(x=300, y=40)
        lableTwo = Label(self, text="Search By:", bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 15, 'bold'))
        lableTwo.place(x=180, y=100)

        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))

        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the ' + g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where name LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's", "Either Book Name is incorrect or it is not available")
                except:
                    messagebox.showerror("Error", "Something goes wrong")
            elif g.get() == 'Author Name':
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where author LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's", "Author Name not found")
                except:
                    messagebox.showerror("Error", "Something goes wrong")
            elif g.get() == 'Book Id':
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.mycursor = self.conn.cursor()
                    # self.mycursor.execute("Select * from book where book_id LIKE %s", ['%' + f.get() + '%'])
                    self.mycursor.execute("Select * from book where book_id  =%s", [f.get()])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's", "Either Book Id is incorrect or it is not available")
                except:
                    messagebox.showerror("Error", "Something goes wrong")

        b = Button(self, text="Find", bg='#28a745',fg='#f9f9f9', height=2, width=10,  font=("Helvetica Neue", 12, 'bold'), command=ge)
        b.place(x=520, y=115)

        c = ttk.Combobox(self, font=("Helvetica Neue", 12), textvariable=g, values=["Book Name", "Author Name", "Book Id"], width=40,
                         state="readonly")
        c.place(x=310, y=105, height=30, width=175)

        en = Entry(self, font=("Helvetica Neue", 12), textvariable=f)
        en.place(x=310, y=145, height=30, width=175)
        la = Label(self, text="Enter:", bg="#343a40",fg='#f8f9fa', font=("Helvetica Neue", 15, 'bold'))
        la.place(x=180, y=140)


        self.listTree = ttk.Treeview(self, height=5, columns=('Book Name', 'Book Author', 'Availability'))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Book ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='Book Author')
        self.listTree.column("Book Author", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.place(x=40, y=200)

        ttk.Style().configure("Treeview", font=('Times new Roman', 15))


Search().mainloop()