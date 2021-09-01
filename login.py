from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import re
import os

def call_newscreen2(event=None):
    root.destroy()
    os.system('python sign_up.py')

def call_newscreen3(event=None):
    root.destroy()

    os.system('python project.py')


def call_newscreen5(event=None):
    root.destroy()
    os.system('python forgot_password.py')

def jump_next(event=None):
    event.widget.tk_focusNext().focus()

def jump_prev(event=None):
    event.widget.tk_focusPrev().focus()

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Fitness Tracker")
        self.root.resizable(0,0)
        self.root.geometry("1100x900+0+0")
        self.bg = Image.open("bg2.jpg")
        self.bg1 = self.bg.resize((1450, 1000), Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(self.bg1)
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0)

        #innerframe_signup
        frame_signup = Frame(self.root,bg="white")
        frame_signup.place(x=100,y=75,height=500,width=400)

        label1 = Label(frame_signup, text="Login Here", font=('impact', 32, 'bold'),
                       fg="black", bg='white')
        label1.place(x=95, y=50)

        label2 = Label(frame_signup, text="Email/Username/Phone ", font=("Goudy old style", 20, "bold"),
                       fg='orangered', bg='white')
        label2.place(x=30, y=145)

        #variables
        # global  v_email, v_password
        v_email = StringVar()
        v_password = StringVar()

        def login_val(event=None):
            conn = sqlite3.connect('attempt6.db')
            c = conn.cursor()

            find_user = ("SELECT * FROM data WHERE email=? or username=? or phone=? or password=?")
            c.execute(find_user, [(v_email.get()), (v_email.get()), (v_email.get()), (v_password.get())])
            row_e = c.fetchall()



            if row_e:

                name = row_e[0][0]
                call_newscreen3()
                messagebox.showinfo("Welcome", f"Hi {name}! Sup!")


            else:
                messagebox.showinfo("Hey buddy!", "Invalid Credentials")

        e_email = Entry(frame_signup, textvariable=v_email, font=("times new roman", 15),
                               bg='lightgray')
        e_email.place(x=30, y=195, width=270, height=35)

        label3 = Label(frame_signup, text="Password", font=("Goudy old style", 20),
                       fg='orangered', bg='white')
        label3.place(x=30, y=245)

        e_password = Entry(frame_signup, textvariable=v_password, font=("times new roman", 15, "bold"), show="*", bg='lightgray')
        e_password.place(x=30, y=295, width=270, height=35)

        btn1 = Button(frame_signup, command=login_val, text="Login", cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
        btn1.place(x=30, y=375)
        btn1.config(command=login_val)
        btn1.bind('<Return>', login_val, add=True)
        # btn1.bind('<Button-1>', login_val, add=True)

        btn2 = Button(frame_signup, command= call_newscreen5, text="Forgot Password?", cursor='hand2', font=('calibri', 10), bg='white', fg='black', bd=0)
        btn2.place(x=200, y=440)
        btn2.config(command=call_newscreen5)
        btn2.bind('<Return>', call_newscreen5, add=True)

        btn3 = Button(frame_signup, command=call_newscreen2, text="Sign Up" , cursor="hand2", font=("calibri", 10), bg='white', fg="black", bd=0)
        btn3.place(x=50, y=440)
        btn3.config(command=call_newscreen2)
        btn3.bind('<Return>', call_newscreen2, add=True)

        #navigation
        e_email.bind('<Down>', jump_next)
        e_email.bind('<Return>', jump_next)
        e_password.bind('<Return>', jump_next)
        e_password.bind('<Down>', jump_next)
        btn1.bind('<Down>', jump_next, add=True)
        btn2.bind('<Down>', jump_next, add=True)

        e_password.bind('<Up>', jump_prev)
        btn2.bind('<Up>', jump_prev, add=True)
        btn1.bind('<Up>', jump_prev, add=True)
        btn1.bind('<Up>', jump_prev, add=True)
        btn3.bind('<Up>', jump_prev, add=True)
        btn2.bind('<Left>', jump_next, add=True)
        btn3.bind('<Right>', jump_prev, add=True)


root=Tk()
obj=login(root)
root.mainloop()

