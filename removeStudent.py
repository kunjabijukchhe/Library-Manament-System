from tkinter import *
from tkinter import messagebox
import pymysql



# creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)
        self.geometry('380x180')

        self.configure(bg="#343a40")
        self.title("Remove Student")

        a = StringVar()

        def ent():
            if len(a.get()) == 0:
                messagebox.showinfo("Error", "Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the student?")
                if d:
                    try:
                        self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from student where stud_id = %s", [a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm", "Student Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error", "Something goes wrong")

        l1 = Label(self, text='Remove Student', fg='black', bg="#20c997", font=("Helvetica Neue", 20, 'bold')).place(x=80, y=25)
        Label(self, text="Enter Student Id: ", bg="#343a40",fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=10, y=100)
        e = Entry(self, font=("Helvetica Neue", 12), textvariable=a, width=37)
        e.place(x=180, y=100, height=30, width=40)
        Button(self, text='Remove', bg='#d9534f',fg='#f9f9f9', height=1, width=10, font=("Helvetica Neue", 12, 'bold'), command=ent).place(
            x=240, y=98)


Rem().mainloop()