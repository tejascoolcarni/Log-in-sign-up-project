from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import re
import os

def call_newscreen1(event=None):
    root.destroy()
    os.system('python login.py')

def call_newscreen2(event=None):
    root.destroy()
    os.system('python sign_up.py')

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

        #innerframe_forgo_tpassword
        frame_forgot_password = Frame(self.root,bg="white")
        frame_forgot_password.place(x=100,y=75,height=650,width=450)

        label1 = Label(frame_forgot_password, text="1) Verify your credentials.", font=('times new roman', 18, 'bold'), fg="black", bg='white', justify="left")
        label1.place(x=50, y=70)

        label2 = Label(frame_forgot_password, text="Enter email/phone/username", font=('times new roman', 10), fg="black", bg='white', justify="left")
        label2.place(x=50, y=120)

        label3 = Label(frame_forgot_password, text="2) Answer the security question\nand reset your password", font=('times new roman', 15, 'bold'), fg="black", bg='white', justify="left")
        label3.place(x=50, y=250)

        label4 = Label(frame_forgot_password, text="Answer", font=('times new roman', 10), fg="black", bg='white', justify="left")
        label4.place(x=50, y=380)

        l_password = Label(frame_forgot_password, text="New Password", font=('times new roman', 10), fg="black", bg='white', justify="left")
        l_password.place(x=50, y=440)

        l_con_password = Label(frame_forgot_password, text="Confirm New Password", font=('times new roman', 10), fg="black", bg='white', justify="left")
        l_con_password.place(x=50, y=500)

        l_question = Label(frame_forgot_password, text="Your security question is:", font=('times new roman', 10), fg="black", bg='white', justify="left")
        l_question.place(x=50, y=310)

        l_question_line = Label(frame_forgot_password, text=" Complete-the-first-step   ", font=('times new roman', 12 , 'italic'), fg="black", bg='grey', justify="left")
        l_question_line.place(x=50, y=330)

        #variable
        # global v_credential, v_answer, v_password

        v_credential = StringVar()
        v_answer = StringVar()
        v_password = StringVar()
        v_con_password = StringVar()
        # var=v_password.get()

        def verify(event=None):
            conn = sqlite3.connect('attempt6.db')
            c = conn.cursor()

            find_user = ("SELECT * FROM data WHERE email=? or username =? or phone=?")
            c.execute(find_user, [(v_credential.get()), (v_credential.get()), (v_credential.get())])
            verify = c.fetchall()


            if verify:
                a = verify[0][7]
                l_question_line.config(text= f"The name of your {a} is?",font=('times new roman', 18 , 'bold'))

            else:
                messagebox.showinfo("Hey buddy!", "Invalid Crednetials")

        def reset(event=None):

            if v_password.get() == "":
                messagebox.showinfo("Hey buddy!", "You cant leave any field blank dude")

            elif v_password.get().isalpha() or v_password.get().isnumeric() == True:
                messagebox.showinfo("Weak Password", "Passsword must contain numbers and alphabets both.")

            elif v_con_password.get() == "":
                messagebox.showinfo("Hey buddy!", "You can't leave any field blank dude")

            elif v_password.get() != v_con_password.get():
                messagebox.showinfo("Hey buddy!", "Passwords did not match. Try Again")

            elif len(v_password.get()) < 4:
                messagebox.showinfo("Hey buddy!",
                                    "Password should have minimum four characters")

            elif v_answer.get() == "":
                messagebox.showinfo("Hey buddy!", "You can't leave any field blank dude")

            else:

                conn = sqlite3.connect('attempt6.db')
                c = conn.cursor()
                find_user = ("SELECT * FROM data WHERE email=? or username =? or phone=?")
                c.execute(find_user, [(v_credential.get()), (v_credential.get()), (v_credential.get())])
                verify = c.fetchall()
                print(verify[0][8])


                if verify[0][8] == v_answer.get():

                    new_pass = v_password.get()
                    cred = v_credential.get()
                    update=(f"UPDATE data SET password = '{new_pass}' WHERE email = ? or phone = ? or username = ?")
                    c.execute(update, [(v_credential.get()),(v_credential.get()),(v_credential.get())])
                    print("valid")
                    conn.commit()
                    messagebox.showinfo("Congratulations", "Password reset succesfully.")
                    call_newscreen1()

                else:
                    messagebox.showinfo("Invalid", "Answer to the security question doesn't match with user. Please try again.")

#structure
        credentials = Entry(frame_forgot_password, textvariable=v_credential, font=("times new roman", 15), bg='lightgray')
        credentials.place(x=50, y=150, width=270, height=35)

        check = Button(frame_forgot_password, command=verify, text="Verify", cursor="hand2", font=("times new roman", 15), fg="white", bg="orangered", bd=0, width=15, height=1)
        check.place(x=50, y=200)
        check.config(command=verify)
        check.bind('<Return>', verify)


        answer = Entry(frame_forgot_password, textvariable= v_answer, font=("times new roman", 15), bg='lightgray')
        answer.place(x=50, y=400, width=270, height=35)

        new_password = Entry(frame_forgot_password, textvariable=v_password, font=("times new roman", 15), bg='lightgray', show="*")
        new_password.place(x=50, y=460, width=270, height=35)

        con_new_password = Entry(frame_forgot_password, textvariable=v_con_password, font=("times new roman", 15), bg='lightgray')
        con_new_password.place(x=50, y=520, width=270, height=35)

        ver = Button(frame_forgot_password, command=reset, text="Submit", cursor="hand2",
                     font=("times new roman", 15), fg="white", bg="orangered",
                     bd=0, width=15, height=1)
        ver.place(x=50, y=575)
        ver.config(command=reset)
        ver.bind('<Return>', reset)

        btn3 = Button(frame_forgot_password, command=call_newscreen1, text="Log In", cursor="hand2", font=("calibri", 10),
                      bg='white', fg="black", bd=0)
        btn3.place(x=50, y=620)
        btn3.config(command=call_newscreen1)
        btn3.bind('<Return>', call_newscreen1, add=True)

        btn4 = Button(frame_forgot_password, command=call_newscreen2, text="Sign Up", cursor="hand2",
                      font=("calibri", 10),
                      bg='white', fg="black", bd=0)
        btn4.place(x=100, y=620)
        btn4.config(command=call_newscreen2)
        btn4.bind('<Return>', call_newscreen2, add=True)

        #navigations
        credentials.bind('<Down>', jump_next)
        credentials.bind('<Return>', jump_next)
        answer.bind('<Down>', jump_next)
        answer.bind('<Return>', jump_next)
        new_password.bind('<Down>', jump_next)
        new_password.bind('<Return>', jump_next)
        con_new_password.bind('<Down>', jump_next)
        con_new_password.bind('<Return>', jump_next)

        con_new_password.bind('<Up>', jump_prev)
        new_password.bind('<Up>', jump_prev)
        answer.bind('<Up>', jump_prev)
        check.bind('<Down>', jump_next, add=True)
        ver.bind('<Down>', jump_next, add=True)
        ver.bind('<Up>', jump_prev, add=True)
        check.bind('<Up>', jump_prev, add=True)
        btn3.bind('<Up>', jump_prev, add=True)
        btn3.bind('<Down>', jump_next, add=True)
        btn3.bind('<Right>', jump_next, add=True)
        btn4.bind('<Left>', jump_prev, add=True)
        btn4.bind('<Up>', jump_prev, add=True)

root=Tk()
obj=login(root)
root.mainloop()
