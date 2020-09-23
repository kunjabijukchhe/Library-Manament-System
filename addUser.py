from tkinter import *
from tkinter import messagebox
import os, sys
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

py = sys.executable


# creating window
class reg(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)
        self.geometry('400x400')

        self.configure(bg="#343a40")
        self.title('Add Librarian')

        # creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()
        email = StringVar()

        def send_message():
            msg = MIMEMultipart()
            msg['From'] = 'systemlibrarymgmt@gmail.com'
            msg['To'] = email.get()
            msg['Subject'] = 'System User'

            body = f"Hi, You have been added as Librarian\n\t\tUsername:{u.get()}\n\t\tName:{n.get()}\n\t\tPassword:{p.get()}"
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
            server.quit()

        def insert():
            try:
                self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,email,password) values (%s,%s,%s,%s)",
                                      [u.get(), n.get(), email.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'addUser.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except:
                messagebox.showinfo("Error", "Something Goes Wrong")

        # label and input
        Label(self, text='User Details', fg='black', bg="#20c997", font=('Helvetica Neue', 20, 'bold')).place(x=130,
                                                                                                              y=22)
        Label(self, text='Name:', bg="#343a40", fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50, y=82)
        e1 = Entry(self, font=("Helvetica Neue", 12), textvariable=n, width=30)
        e1.place(x=160, y=80, height=30, width=175)
        Label(self, text='Username:', bg="#343a40", fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50,
                                                                                                             y=130)
        e2 = Entry(self, font=("Helvetica Neue", 12), textvariable=u, width=30)
        e2.place(x=160, y=130, height=30, width=175)

        Label(self, text='Email:', bg="#343a40", fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50, y=180)
        e = Entry(self, font=("Helvetica Neue", 12), textvariable=email, width=30)
        e.place(x=160, y=180, height=30, width=175)

        Label(self, text='Password:', bg="#343a40", fg='#f8f9fa', font=('Helvetica Neue', 15, 'bold')).place(x=50,
                                                                                                             y=230)
        e3 = Entry(self, font=("Helvetica Neue", 12), show='*', textvariable=p, width=30)
        e3.place(x=160, y=230, height=30, width=175)
        Button(self, text="Submit", bg='#28a745', fg='#f9f9f9', height=2, width=10, font=("Helvetica Neue", 12, 'bold'),
               command=lambda: [insert(), send_message()]).place(x=150, y=300)


reg().mainloop()
