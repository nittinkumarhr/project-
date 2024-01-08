import imaplib
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
from tkinter import ttk
import sqlite3
import re
import os
import random
from form import fo
from forget_p import forget
class login_class:
    def __init__(self, login_SMS):
        self.login_SMS =login_SMS
        self.login_SMS.geometry("1250x650+0+0")
        self.login_SMS.resizable(False,False)
        self.login_SMS.focus_force()
        self.login_SMS.config(background="white")
        self.login_SMS.iconbitmap("P:\hr\project\images\Login.ico")
        self.login_SMS.title("Login")
        # Image content++++++++++++++++++++
        self.bg_image2 = ImageTk.PhotoImage(file="P:\hr\project/images/1900851.png")
        self.bg_lb2 = Label(self.login_SMS, image=self.bg_image2)
        
        self.bg_lb2.place(x=0,y=0,relheight=1,relwidth=1)
        
 
        #===========================LABELS
        l={"Red","Yellow","Violet","MediumSlateBlue","Lime","Aqua","Blue","white","BlanchedAlmond","HoneyDew"}
        for i in l:
            self.lo = ImageTk.PhotoImage(file="P:\hr\project\images\login_icon_176905.png")
            self.bg_lb_login = Label(self.login_SMS, image=self.lo,bg=i)
            self.bg_lb_login.place(x=50,y=175,width=450,height=400)
            self.b_t=Label(self.login_SMS,text="STUDENTS MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),fg=i,bg="DarkSeaGreen")
            self.b_t.place(x=380,y=25)
            titl=Label(self.login_SMS,text="LOGIN HERE",font=("times new roman",25,"bold"),fg=i,bg="DarkSeaGreen").place(x=510,y=88)
        #=================labels======================
        self.email=Label(self.login_SMS,text="Email",font=("goudy old style",19,"bold"),fg="white",bg="DarkSeaGreen").place(x=610,y=200,width=120 )
        self.em = ImageTk.PhotoImage(file="P:\hr\project\images\email1.png")
        self.em_lb = Label(self.login_SMS, image=self.em,bg="DarkSeaGreen",fg="white")
        self.em_lb.place(x=580,y=200)
        password=Label(self.login_SMS,text="Password",font=("goudy old style",19,"bold"),fg="white",bg="DarkSeaGreen",).place(x=610,y=300)
        self.p= ImageTk.PhotoImage(file="P:\hr\project\images\password.png")
        self.p_lb = Label(self.login_SMS, image=self.p,bg="DarkSeaGreen",fg="white")
        self.p_lb.place(x=580,y=300)
        #=========varibles=======================
        self.var_p=StringVar()
        self.var_e=StringVar()
        
        #=====================================Entryes+++++++++++++++++++++
        self.entery_email=Entry(self.login_SMS,textvariable=self.var_e,font=("goudy old style",15,"bold"),bg="DarkSeaGreen")
        self.entery_email.bind("<FocusIn>",lambda e: self.entery_email.configure(background="BlACK",fg="DarkSeaGreen"))
        self.entery_email.bind("<FocusOut>",lambda e: self.entery_email.configure(background="DarkSeaGreen",fg="black"))
        self.entery_email.place(x=765,y=200,width=220,height=35)
        self.entery_pass=Entry(self.login_SMS,textvariable=self.var_p,font=("goudy old style",15,"bold"),bg="DarkSeaGreen",show="*")
        self.entery_pass.bind("<FocusIn>",lambda e: self.entery_pass.configure(background="BlACK",fg="DarkSeaGreen"))
        self.entery_pass.bind("<FocusOut>",lambda e: self.entery_pass.configure(background="DarkSeaGreen",fg="black"))
        self.entery_pass.place(x=765,y=300,width=220,height=35)
        #================buttons==========================
        self.ct=Button(self.login_SMS,text="Create New Account ?",bg="darkSeaGreen",fg='red',font=("times new roman",15),bd=0,cursor="hand2",justify=CENTER,activebackground="darkSeaGreen",command=self.register)
        self.ct.place(x=570,y=400,)
        self.ft=Button(self.login_SMS,text="Forgat Password",bg="darkSeaGreen",fg='red',font=("times new roman",15),bd=0,cursor="hand2",justify=CENTER,activebackground="darkSeaGreen",command=self.forget_pass)
        self.ft.place(x=835,y=400)
        self.bt_image = ImageTk.PhotoImage(file="P:\hr\project/images/bt2.png")
        self.bt=Button(self.login_SMS,image=self.bt_image,bd=0,cursor="hand2",bg="DarkSeaGreen",activebackground="DarkSeaGreen",command=(self.conform))
        self.bt.bind("<Enter>",lambda e :move() )
        self.bt.place(x=680,y=490)
        def move():
            if self.var_e.get() =="" or self.var_p.get()=="": 
             self.ch=random.randint(500,850)
             self.bt.place(x=self.ch,y=490)
    
        
    
                  
    def conform(self):
        if   self.var_e.get()=="" or self.var_p.get()=="" :
            messagebox.showerror("Error","Colum is Empty  Please Enter the Required Value",parent=self.login_SMS)
        else:
            self.bg_lb_login.place(x=50,y=175,width=450,height=400)
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            s=re.search(regex,self.var_e.get())
            p=self.var_p.get()
            if s==None:
               messagebox.showerror("Error","invalid Email please Enter the valid email",parent=self.login_SMS)
            elif (len(p)<=8 and p!=""):
                messagebox.showerror("Error",f"-->Password Minimum Length  8 ")
            else:
                con=sqlite3.connect(database="rms.db")
                c=con.cursor()
                c.execute("Select * from reg where Email=? and password =?",(self.var_e.get(),self.var_p.get(),))
                r=c.fetchone()  
                if r!=None:
                    messagebox.showinfo("Success","login Conform\n welcome to  SRMS",parent=self.login_SMS)
                    self.login_SMS.destroy()
                    os.system("python main.py")
                    
                else:
                    messagebox.showerror("Error",f"Wrong Email and Password Please Enter the Valid Details")

    def register(self):
        self.reg=Toplevel(self.login_SMS)
        self.re_new=fo(self.reg) 
    def forget_pass(self):
        self.pss=Toplevel(self.login_SMS)
        self.pss_new=forget(self.pss)     
                                            
                
if __name__ == "__main__":
    login_ob = Tk()
    obj_login = login_class(login_ob)
    login_ob.mainloop()        
               
