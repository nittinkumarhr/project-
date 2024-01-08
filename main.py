from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
from cocurse import RMS1
from students import STUDENT
from result import Result
from viewresults import Result_View
import os
class  RMS_main:
    def __init__(self, root):
        self.root =root
        self.root.title("STUDENTS RESULT MANAGEMENT SYSTEM ")
        self.root.geometry("1250x650+0+0")
        self.root.resizable(False, False)
        self.root.config(bg="white")
        self.root.iconbitmap("P:\hr\project\images\std.ico")
        # -----Icons--------------------
        self.logo = ImageTk.PhotoImage(file="P:\hr\project\images\logo_p.png")

        # -----Title--------------
        l={"Red","Yellow","Violet","MediumSlateBlue","Lime","Aqua","Blue","white","BlanchedAlmond","HoneyDew"}
        for i in l:
          title_main = Label(self.root, text="Students Result Management System", fg=i ,font=("goudy old style", 20, "bold"),
                      bg="#033055", padx=25, compound=LEFT, image=self.logo)
          title_main.place(x=0, y=0, relwidth=1, height=50)
        self.lo = ImageTk.PhotoImage(file="P:\hr\project/images/srm.png")
        self.bg_lb_login = Label(self.root, image=self.lo,bg="white")
        self.bg_lb_login.place(x=10,y=175,width=550,height=425)         

        # -------Menu---------------

        mf = LabelFrame(self.root, text="Menu", font=("times new roman ", 10), bg="white", border="2px", borderwidth=2)
        mf.place(x=10, y=100, width=1225, height=70)

        # -------BUTTIONS -----------

        mb = Button(mf, text="Student", cursor="hand2",font=("goudy old style", 15, "bold"), relief="solid",
                    activeforeground="BlueViolet", bg="MediumSlateBlue", fg="white",command=self.student_main)
        mb.place(x=10, y=4, height=40, width=200)

        # B-----Students-----------

        mb1 = Button(mf, text="Course", cursor="hand2",font=("goudy old style", 15, "bold"),relief="solid", activeforeground="BlueViolet", bg="MediumSlateBlue", fg="white",command=self.cneew)
        mb1.place(x=220, y=4, height=40, width=200)

        # B--------Result--------------

        mb2 = Button(mf, text="Result", cursor="hand2", font=("goudy old style", 15, "bold"), relief="solid",
                     activeforeground="BlueViolet", bg="MediumSlateBlue", fg="white",command=self.result_main)
        mb2.place(x=430, y=4, height=40, width=200)

        # B------View students resullts-------------

        mb3 = Button(mf, text="View Results", cursor="hand2", font=("goudy old style", 15, "bold"), relief="solid",
                     activeforeground="BlueViolet", bg="MediumSlateBlue", fg="white",command=self.Result_View)
        mb3.place(x=640, y=4, height=40, width=200)
        # B------Logout ------------
        mb4 = Button(mf, text="LogOut", cursor="hand2", font=("goudy old style", 15, "bold"), relief="solid",
                     activeforeground="BlueViolet", bg="MediumSlateBlue", fg="white",command=self.log_out)
        mb4.place(x=850, y=4, height=40, width=200)
        # B-----Exit-------------
        mb5 = Button(mf, text="Exit", cursor="hand2", font=("goudy old style", 15, "bold"), relief="solid",
                     activeforeground="BlueViolet", bg="MediumSlateBlue", fg="white",command=self.exit_f)
        mb5.place(x=1060, y=4, height=40, width=150)
        # ---------conttent window--------
        self.bg_image = ImageTk.PhotoImage(file="P:\hr\project\images\drv.png")
        self.bg_lb = Label(self.root, image=self.bg_image)
        self.bg_lb.place(x=650, y=200, width=500, height=350)
        # -----footer--------------
        footer = Label(self.root,
                       text="SRMS-Students Result Management System \n contact as for any Technical Issue : 6397XXXX08",
                       font=("goudy old style", 12, "bold"), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        # ------update deatils------
        self.labl_c = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 15), bg="#e43b06",
                            fg="white", bd=10, relief=RAISED)
        self.labl_c.place(x=440, y=530, width=250, height=70)
        self.labl_s = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 15), bg="#0676ad",
                            fg="white", bd=10, relief=RAISED)
        self.labl_s.place(x=710, y=530, width=250, height=70)
        self.labl_r = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 15), bg="#038074",
                            fg="white", bd=10, relief=RAISED)
        self.labl_r.place(x=980, y=530, width=250, height=70)
        # ---------add Course-------------
        self.update()
    def update(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("Select * from course")
            cr=curser.fetchall()
            self.labl_c.config(text=f"Total Course\n[{str(len(cr))}]" )
            
            curser.execute("Select * from students")
            cr=curser.fetchall()
            self.labl_s.config(text=f"Total Students\n[{str(len(cr))}]" )
        
            curser.execute("Select * from results")
            cr=curser.fetchall()
            self.labl_r.config(text=f"Total Results \n[{str(len(cr))}]" )
            self.labl_c.after(200,self.update)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def cneew(self):
        self.newq=Toplevel(self.root)
        self.nwobj=RMS1(self.newq)
    def student_main(self):
        self.st=Toplevel(self.root)
        self.newst1=STUDENT(self.st)    
    def result_main(self):
        self.ret=Toplevel(self.root)
        self.newst2=Result(self.ret)
    def Result_View(self):
        self.re_view=Toplevel(self.root)
        self.newst=Result_View(self.re_view)
    def exit_f(self):
        self.res=messagebox.askquestion("Quick Exit","Are you Source to exit ??")
        if self.res=='yes':
            self.root.destroy()

            
    def log_out(self):
        self.lg=messagebox.askquestion("Log Out","Are you Source to Log Out")
        if self.lg=="yes":
            self.root.destroy()
            os.system("python Admin.py") 
if __name__ == "__main__":
    main_ob = Tk()
    obj = RMS_main(main_ob)
    main_ob.mainloop()
 
