import imaplib
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
from tkinter import ttk
import sqlite3
import re
from form import fo
import os
import random
class forget:
    def __init__(self, forget_Form):
        self.forget_Form =forget_Form
        self.forget_Form.geometry("825x500+200+118")
        self.forget_Form.resizable(False,False)
        self.forget_Form.focus_force()
        self.forget_Form.config(background="white")
        self.forget_Form.iconbitmap("P:\hr\project/images/forget.ico")
        self.forget_Form.title("Forget Password")
        self.forget_Form.configure(background="black")
        #===============title==========================================
        l={"Red","Violet","MediumSlateBlue","Lime","Blue","Fuchsia","LimeGreen","DarkGoldenrod","DarkSlateGray"}
        for i in l:
         self.title=Label(self.forget_Form,text="FORGET PASSWORD",font=("times new roman",25,"bold"),fg=i)
         self.title.place(x=250,y=20)
         self.p2= ImageTk.PhotoImage(file="P:\hr\project/images/back_re.jpg")
         self.p_lb2 = Label(self.forget_Form, image=self.p2,bg=i)
         self.p_lb2.place(x=100,y=70)
        #============================labels===============================================================
        lb_phone=Label(self.forget_Form,text="Phone number",font=("goudy old style",15,"bold"),bg="black",fg="white")
        lb_phone.place(x=220,y=180)
        lb_email=Label(self.forget_Form,text="Register Email",font=("goudy old style",15,"bold"),bg="black",fg="white")
        lb_email.place(x=220,y=235)
        lb_email=Label(self.forget_Form,text="New password",font=("goudy old style",15,"bold"),bg="black",fg="white")
        lb_email.place(x=220,y=290)
        #====varibles==================================================================================
        self.var_old_phone=StringVar()
        self.var_old_email=StringVar()
        self.var_new_password=StringVar()
        #==================Entry=========================================================
        self.entry_old_phone=Entry(self.forget_Form,textvariable=self.var_old_phone,font=("goudy old style",15,"bold"),bg="black")
        self.entry_old_phone.bind("<FocusIn>",lambda e: self.entry_old_phone.configure(background="white",fg="black"))
        self.entry_old_phone.bind("<FocusOut>",lambda e: self.entry_old_phone.configure(background="black",fg="white"))
        self.entry_old_phone.place(x=380,y=180,width=200)
        self.entry_old_email=Entry(self.forget_Form,textvariable=self.var_old_email,font=("goudy old style",15,"bold"),bg="black")
        self.entry_old_email.bind("<FocusIn>",lambda e: self.entry_old_email.configure(background="white",fg="black"))
        self.entry_old_email.bind("<FocusOut>",lambda e: self.entry_old_email.configure(background="black",fg="white"))
        self.entry_old_email.place(x=380,y=235,width=200)
        self.entry_new_passorwd=Entry(self.forget_Form,textvariable=self.var_new_password,font=("goudy old style",15,"bold"),bg="black")
        self.entry_new_passorwd.bind("<FocusIn>",lambda e: self.entry_new_passorwd.configure(background="white",fg="black"))
        self.entry_new_passorwd.bind("<FocusOut>",lambda e: self.entry_new_passorwd.configure(background="black",fg="white"))
        self.entry_new_passorwd.place(x=380,y=290,width=200)
        #================Button================================================
        
        self.bt_change=Button(self.forget_Form,text="Change password",bg="black",fg='RoyalBlue',font=("times new roman",15),bd=0,cursor="hand2",justify=CENTER,activebackground="RoyalBlue",activeforeground="black",command=self.check_password)
        self.bt_change.bind("<Enter>",lambda e :move() )
        #self.bt_change.bind("<Leave>",lambda e: self.bt_change.place(x=540,y=348))
        self.bt_change.place(x=540,y=348)
        self.bt_register=Button(self.forget_Form,text="Again Register",bg="black",fg='Fuchsia',font=("times new roman",15),bd=0,cursor="hand2",justify=CENTER,activebackground="Fuchsia",activeforeground="black",command=self.again_register)
        self.bt_register.place(x=148,y=80)
        def move():
            if self.var_old_phone.get() =="" or self.var_old_email.get()=="":
             self.ch=random.randint(150,550)
             self.bt_change.place(x=self.ch,y=348)
    
    def again_register(self):
        self.forget_Form.destroy()
        os.system("python form.py")
    def check_password(self):
        if self.var_old_email.get()=="" or self.var_old_phone.get()=="":
            messagebox.showerror("Error","Colum is Empty  Please Enter the Required Value",parent=self.forget_Form)

        else:
            self.bt_change.place(x=540,y=348)
            if not(self.var_old_phone.get().isdigit()):
                messagebox.showerror("Error","Enter only Digits",parent=self.forget_Form)
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            s=re.search(regex,self.var_old_email.get())
            if s==None:
               messagebox.showerror("Error","invalid Email please Enter the valid email",parent=self.forget_Form)
            elif (len(self.var_new_password.get())<=8 and self.var_new_password.get()!=""):
                messagebox.showerror("Error",f"-->Password Minimum Length  8",parent=self.forget_Form) 
            else:
                con=sqlite3.connect(database="rms.db")
                c=con.cursor()
                c.execute("Select * from reg where Email=? and  Contact =?",(self.var_old_email.get(),self.var_old_phone.get(),))
                r=c.fetchone()
                if r==None:
                    messagebox.showerror("Error",f"NOt Match \n Email and Password ",parent=self.forget_Form)
                else:
                    c.execute("update reg set password=?",(self.var_new_password.get(),))   
                    messagebox.showinfo("Success","Password  UPDATE Successfully",parent=self.forget_Form)
                    con.commit()
                    self.forget_Form.destroy()
                    os.system("python Admin.py")
                    
                    
                        
                                    
        
if __name__ == "__main__":
    ob_form = Tk() 
    obj_form = forget(ob_form)
    ob_form.mainloop()        

