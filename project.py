from tkinter import *
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Fitness Tracker")
        self.root.resizable(0,0)
        self.root.geometry("1100x900+0+0")

root=Tk()
obj=login(root)
root.mainloop()
