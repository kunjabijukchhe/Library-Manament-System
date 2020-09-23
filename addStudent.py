from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys
import pymysql

py = sys.executable


# creating window
class Add(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)
        self.geometry('400x400')

        self.configure(bg="#343a40")
        self.title('Add Student')

        n = StringVar()
        p = StringVar()
        a = StringVar()
        email = StringVar()
        def send_message():
            msg = MIMEMultipart()
            msg['From'] = 'systemlibrarymgmt@gmail.com'
            msg['To'] = email.get()
            msg['Subject'] = 'Student'
            body = f"Hi, You have been added as Student\n\t\tStudent Name:{n.get()}\n\t\tPhone No.{p.get()}\n\t\tAddress:{a.get()}"
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            address_info = email.get()
            print(address_info, text)
            sender_email = "systemlibrarymgmt@gmail.com"
            sender_password = "library2020"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            print("Login successful")
            server.sendmail(sender_email, address_info, text)
            print("Message sent")

        # verifying input
        def asi():
            if len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Name")
            elif len(p.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Phone Number")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Address")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")

                    self.myCursor = self.conn.cursor()
                    name1 = n.get()
                    pn1 = p.get()
                    add1 = a.get()
                    self.myCursor.execute("Insert into student(name,phone_number,address,email) values (%s,%s,%s,%s)",
                                          [name1, pn1, add1,email.get()])
                    self.conn.commit()
                    messagebox.showinfo("Done", "Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm", "Do you want to add another student?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'addStudent.py'))
                    else:
                        self.destroy()
                        self.myCursor.close()
                        self.conn.close()
                except:
                    messagebox.showerror("Error", "Something goes wrong")

        # label and input box
        Label(self, text='Student Details', fg='black', bg="#20c997", font=('Helvetica Neue', 20, 'bold')).place(x=110, y=22)
        Label(self, text='Name:', bg="#343a40",fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50, y=82)
        e1 = Entry(self, font=("Helvetica Neue", 12), textvariable=n, width=30)
        e1.place(x=160, y=80, height=30, width=175)

        Label(self, text='Phone No.', bg="#343a40",fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50, y=130)
        e2 = Entry(self, font=("Helvetica Neue", 12), textvariable=p, width=30)
        e2.place(x=160, y=130, height=30, width=175)

        Label(self, text='Address:', bg="#343a40",fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50, y=180)
        e3 = Entry(self, font=("Helvetica Neue", 12), textvariable=a, width=30)
        e3.place(x=160, y=180, height=30, width=175)

        Label(self, text='Email:', bg="#343a40", fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50, y=230)
        e = Entry(self, font=("Helvetica Neue", 12), textvariable=email, width=30)
        e.place(x=160, y=230, height=30, width=175)

        Button(self, text="Submit", bg='#28a745',fg='#f9f9f9', height=2, width=10, font=("Helvetica Neue", 12, 'bold'), command=lambda:[asi(), send_message()]).place(
            x=150, y=300)


Add().mainloop()
