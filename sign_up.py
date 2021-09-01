from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import re
import os
import sqlite3

def tejas(event=None):
    print("Working")



class signup:
    def __init__(self,root):
        self.root=root
        self.root.title("Fitness Tracker")
        self.root.resizable(0,0)
        self.root.geometry("1100x900+0+0")
        self.bg = Image.open("bg2.jpg")
        self.bg1 = self.bg.resize((1450, 1000), Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(self.bg1)
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0)

        def clear_all(event=None):
            v_first_name.set("")
            v_last_name.set("")
            v_gender.set(0)
            v_email.set("")
            v_phone.set("")
            v_username.set("")
            v_password.set("")
            v_con_password.set("")
            b_securityq.set("")
            v_security_ans.set("")



        def checkemail(v_email):
            if len(v_email) > 7:
                if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", v_email):
                    return True
                else:
                    messagebox.showwarning("Hey!", "Enter a valid email !")
                    return False
            else:
                messagebox.showwarning("Whom are you kidding?", "We only take valid email ids ")
                return False

        def call_newscreen1(event=None):
            root.destroy()
            os.system('python login.py')

        def jump_next(event=None):
            event.widget.tk_focusNext().focus()

        def jump_prev(event=None):
            event.widget.tk_focusPrev().focus()

        def phone_val1(v_phone):
            if v_phone.isdigit():
                return True
            elif v_phone == "":
                return True
            else:
                messagebox.showinfo('Which planet are you from?', 'On Earth we only have digits as phone number!')
                return False


        def store():


            conn = sqlite3.connect('attempt6.db')
            c = conn.cursor()
            c.execute(
                "CREATE TABLE IF NOT EXISTS data(name text, lastname text, gender text, email text, phone text, username text, password text, security_q text, security_a text)")
            c.execute("SELECT * FROM data WHERE email=?", (v_email.get(),))
            row_e = c.fetchall()
            c.execute("SELECT * FROM data WHERE phone=?", (v_phone.get(),))
            row_p = c.fetchall()
            c.execute("SELECT * FROM data WHERE username=?", (v_username.get(),))
            row_u = c.fetchall()

            if row_e:
                messagebox.showinfo("Hey buddy!", "Email already in use. Try Again")
            elif row_p:
                messagebox.showinfo("Hey buddy!", "Phone number already in use. Try Again")
            elif row_u:
                messagebox.showinfo("Hey buddy!", "Username already in use. Try Again")
            else:
                print("done")
                v_name_gender = StringVar()
                if v_gender.get() == 1:
                    v_name_gender.set("Male")

                elif v_gender.get() == 2:
                    v_name_gender.set("Female")


                c.execute(
                    "INSERT INTO data VALUES (:first_name, :last_name, :gender, :email, :phone, :username, :password, :security_q, :security_a)",
                    {'first_name': v_first_name.get(),
                     'last_name': v_last_name.get(),
                     'gender': v_name_gender.get(),
                     'email': v_email.get(),
                     'phone': v_phone.get(),
                     'username': v_username.get(),
                     'password': v_password.get(),
                     'security_q': b_securityq.get(),
                     'security_a': v_security_ans.get().lower()})
                messagebox.showinfo("Registration Successful!", "Welcome to the club!")

            conn.commit()
            clear_all()

        #innerframe_signup
        frame_signup = Frame(self.root,bg="white")
        frame_signup.place(x=100,y=75,height=650,width=450)


        title=Label(frame_signup, text="Register", font=("Impact",35,"bold"),fg="#d77337",bg="white" ).place(x=135,y=30)
        #labels

        l_first_name = Label(frame_signup, text="First Name", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=125)
        l_ast_name = Label(frame_signup, text="Last Name", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=175)
        l_gender = Label(frame_signup, text="Gender", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=225)
        l_email = Label(frame_signup, text="Email", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=275)
        l_phone = Label(frame_signup, text="Phone", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=325)
        l_user_name = Label(frame_signup, text="Username", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=375)
        l_password = Label(frame_signup, text="Password", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=425)
        l_password_note = Label(frame_signup, text="Password should have minimum\n8 characters, case sensitive, 1 alphabet, 1 number", font =("Arial", 7, "bold"),fg="black",bg="white").place(x=45,y=447)
        l_con_password = Label(frame_signup, text="Confirm Password", font =("Arial", 15, "bold"),fg="#d77337",bg="white").place(x=45,y=475)
        l_security_question = Label(frame_signup, text="Security Question", font =("Arial", 10, "bold"),fg="#d77337",bg="white").place(x = 45, y = 510)
        l_security_question_answer = Label(frame_signup, text="Your Answer", font=("Arial", 10, "bold"), fg="#d77337", bg="white").place(x=245, y=510)
        # variables
        global v_phone, v_gender, v_first_name, v_last_name, v_gender ,v_phone, v_email, v_username, v_password, v_con_password,b_securityq, v_security_ans
        v_first_name = StringVar()
        v_last_name = StringVar()
        v_gender = IntVar()
        v_email = StringVar()
        v_phone = StringVar()
        v_username = StringVar()
        v_password = StringVar()
        v_con_password = StringVar()
        b_securityq = StringVar()
        v_security_ans = StringVar()





#function
        def validate_all(event=None ):

            conn = sqlite3.connect('attempt6.db')
            c = conn.cursor()
            c.execute(
                "CREATE TABLE IF NOT EXISTS data(name text, lastname text, gender text, email text, phone text, username text, password text, security_q text, security_a text)")

            find_user_email = ("SELECT * FROM data WHERE email=?")
            c.execute(find_user_email, [(v_email.get())])
            email = c.fetchall()

            find_user_username = ("SELECT * FROM data WHERE username =?")
            c.execute(find_user_username, [(v_username.get())])
            username = c.fetchall()

            find_user_phone = ("SELECT * FROM data WHERE phone=?")
            c.execute(find_user_phone, [(v_phone.get())])
            phone = c.fetchall()

            if email:
                messagebox.showinfo("Hey buddy!", "Email already in use.")

            elif username:
                messagebox.showinfo("Hey buddy!", "Username already in use.")

            elif phone:
                messagebox.showinfo("Hey buddy!", "Phone already in use.")

            elif v_first_name.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You cant leave any field blank dude, we gonna need all your data to sell like zucc.")


            elif v_last_name.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You cant leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False

            elif v_gender.get() == 0:
                messagebox.showinfo("Hey buddy!",
                                    "You cant leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False




            elif len(v_phone.get()) != 10:
                messagebox.showinfo("Oy Foreigner!", "We Indians have 10 digit mobile number only.")
                return False

            elif v_email.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You cant leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False

            elif v_username.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You cant leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False

            elif len(v_username.get()) < 4:
                messagebox.showinfo("Hey buddy!",
                                    "Username should have minimum four characters")
                return False

            elif v_password.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You cant leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False

            elif len(v_password.get()) < 8:
                messagebox.showinfo("Hey buddy!",
                                    "Passwords should have minimum 8 characters")
                return False


            elif v_password.get().isalpha() or v_password.get().isnumeric() == True:
                messagebox.showinfo("Weak Password","Passsword must contain numbers and alphabets both.")
                return False

            elif v_con_password.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You can't leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False

            elif b_securityq.get() == "select":
                messagebox.showinfo("Hey buddy!",
                                    "You can't leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False

            elif b_securityq.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You can't leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False

            elif v_security_ans.get() == "":
                messagebox.showinfo("Hey buddy!",
                                    "You can't leave any field blank dude, we gonna need all your data to sell like zucc.")
                return False



            elif v_password.get() != v_con_password.get():
                messagebox.showinfo("Hey buddy!", "Passwords did not match. Try Again")
                return False




            elif v_email.get() != "":
                status = checkemail(v_email.get())

                if (status):

                    store()
                    print("working")
                    return True

                else:
                    return False

            else:
                return True

        #textboxes
        e_first_name = Entry(frame_signup, width=24, textvariable=v_first_name, bg="light grey")
        e_first_name.place(x=245, y=131)
        e_last_name = Entry(frame_signup, width=24, textvariable=v_last_name, bg="light grey")
        e_last_name.place(x=245, y=181)
        e_gender1 = Radiobutton(frame_signup, text="Male", variable=v_gender, padx=5, bg="white", value=1)
        e_gender1.place(x=245, y=231)
        e_gender2 = Radiobutton(frame_signup, text="Female", variable=v_gender, bg="white", value=2)
        e_gender2.place(x=320, y=231)
        e_email = Entry(frame_signup, width=24, textvariable=v_email, bg="light grey")
        e_email.place(x=245, y=281)
        e_phone = Entry(frame_signup, width=24, textvariable=v_phone, bg="light grey")
        e_phone.place(x=245, y=331)
        e_username = Entry(frame_signup, width=24, textvariable=v_username, bg="light grey")
        e_username.place(x=245, y=381)
        e_password = Entry(frame_signup, width=24, show="*", textvariable=v_password, bg="light grey")
        e_password.place(x=245, y=431)
        e_con_password = Entry(frame_signup, width=24, textvariable=v_con_password, bg="light grey")
        e_con_password.place(x=245, y=481)
        b_securityq = ttk.Combobox(frame_signup, width=14, font=("time new roman", 13))
        b_securityq["values"] = (
        "select", "best friend", "first pet", "favourite school teacher", "favourite singer", "favourite book",
        "favourite sports-person", "favourite movie", "favourite tv show")
        b_securityq.current(0)
        b_securityq.place(x=45, y=531)
        e_security_a = Entry(frame_signup, width=24, textvariable=v_security_ans, bg="light grey")
        e_security_a.place(x=245, y=531)


        #buttons
        submit = Button(frame_signup, text="Submit",cursor="hand2",font=("times new roman", 15),command = validate_all, fg="white", bg="orangered", bd=0, width=15, height=1)
        submit.config(command= validate_all)
        submit.bind('<Return>', validate_all)
        submit.bind('<Button-1>', validate_all, add=True)
        submit.place(x=50, y=570)
        submit.bind('<Return>', tejas, add=True)

        clear = Button(frame_signup, text="Clear", command= clear_all, padx=10, width=10)
        clear.config(command=clear_all)
        clear.bind('<Return>', clear_all)
        clear.bind('<Button-1>', clear_all, add=True)
        clear.place(x=275, y=575)

        existing_user = Button(frame_signup, text="Existing User? Log in.", command= call_newscreen1,font=("calibri", 10), bg='white', fg="black", bd=0)

        existing_user.config(command=call_newscreen1)
        existing_user.bind('<Return>', call_newscreen1)
        existing_user.bind('<Button-1>',call_newscreen1, add=True)
        existing_user.place(x=160, y=620)


        e_first_name.bind('<Return>', jump_next)
        e_last_name.bind('<Return>', jump_next)
        e_gender1.bind('<Return>', jump_next)
        e_gender2.bind('<Return>', jump_next)
        e_email.bind('<Return>', jump_next)
        e_phone.bind('<Return>', jump_next)
        e_username.bind('<Return>', jump_next)
        e_password.bind('<Return>', jump_next)
        e_con_password.bind('<Return>', jump_next)

        e_first_name.bind('<Down>', jump_next)
        e_last_name.bind('<Down>', jump_next)
        e_gender1.bind('<Down>', jump_next)
        e_gender2.bind('<Down>', jump_next)
        e_email.bind('<Down>', jump_next)
        e_phone.bind('<Down>', jump_next)
        e_username.bind('<Down>', jump_next)
        e_password.bind('<Down>', jump_next)
        e_con_password.bind('<Down>', jump_next)
        b_securityq.bind('<Down>', jump_next)
        b_securityq.bind('<Return>', jump_next)
        e_security_a.bind('<Down>', jump_next)
        e_security_a.bind('<Return>', jump_next)
        e_security_a.bind('<Left>', jump_prev)

        submit.bind('<Right>', jump_next, add=True)
        submit.bind('<Down>', jump_next, add=True)
        submit.bind('<Up>', jump_prev, add=True)
        clear.bind('<Left>', jump_prev, add=True)
        clear.bind('<Up>', jump_prev, add=True)
        clear.bind('<Right>', jump_next, add=True)
        clear.bind('<Down>', jump_next, add=True)

        existing_user.bind('<Left>', jump_prev, add=True)
        existing_user.bind('<Up>', jump_prev, add=True)

        e_last_name.bind('<Up>', jump_prev)
        e_gender1.bind('<Up>', jump_prev)
        e_gender2.bind('<Up>', jump_prev)
        e_email.bind('<Up>', jump_prev)
        e_phone.bind('<Up>', jump_prev)
        e_username.bind('<Up>', jump_prev)
        e_password.bind('<Up>', jump_prev)
        e_con_password.bind('<Up>', jump_prev)
        e_security_a.bind('<Up>', jump_prev)
        b_securityq.bind('<Right>', jump_prev)
        e_con_password.bind('<Up>', jump_prev)
        valid_pn1= self.root.register(phone_val1)
        e_phone.config(validate="key", validatecommand=(valid_pn1, "%P"))
    

root = Tk()
obj = signup(root)
root.mainloop()