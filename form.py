import imaplib
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
from tkinter import ttk
import sqlite3
import re
import os
import random
class fo:
    def __init__(self, form_SMS):
        self.form_SMS =form_SMS
        self.form_SMS.geometry("1250x450+0+200")
        self.form_SMS.resizable(False,False)
        self.form_SMS.focus_force()
        self.form_SMS.config(background="white")
        self.form_SMS.iconbitmap("P:\hr\project/images/regis.ico")
        self.form_SMS.title("Registration From")
        #---------------------------image content=================================================
        # image background============================================
        self.bg_image = ImageTk.PhotoImage(file="P:\hr\project/images/169860bbc6e55afa2f6ba2ec4f064ae2.jpg")
        self.bg_lb = Label(self.form_SMS, image=self.bg_image)
        self.bg_lb.place(x=250,y=0,relheight=1,relwidth=1)
        # image background ++++++++++++++++++++++++++++++++++++++
        self.bg_image1 = ImageTk.PhotoImage(file="P:\hr\project/images/1732235.webp")
        self.bg_lb1 = Label(self.form_SMS, image=self.bg_image1)
        self.bg_lb1.place(x=0,y=0,width=475,relheight=1)
        #==================Frame============================================
        frame1=Frame(self.form_SMS,bg="white")
        frame1.place(x=460,y=30,width=750,height=380)
        l={"Red","Yellow","Violet","MediumSlateBlue","Lime","Aqua","Blue","white","BlanchedAlmond","HoneyDew"}
        for i in l: 
   
         self.titl=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg=i).place(x=25,y=10)
         self.bg_image2 = ImageTk.PhotoImage(file="P:\hr\project\images\side.png")
         self.bg_lb2 = Label(self.form_SMS, image=self.bg_image2,bg=i)
         self.bg_lb2.place(x=20,y=20,height=400)
        #====================labels=================================================================
        lbl_First_name=Label(frame1,text="First Name",font=("goudy old style",15,"bold"),bg="white").place(x=25,y=60)
        lbl_name=Label(frame1,text="Last Name",font=("goudy old style",15,"bold"),bg="white").place(x=380,y=60)
        lbl_contact=Label(frame1,text="Contact No",font=("goudy old style",15,"bold"),bg="white").place(x=25,y=120)
        lbl_gender=Label(frame1,text="Security",font=("goudy old style",15,"bold"),bg="white").place(x=25,y=170)
        lbl_state=Label(frame1,text="Password",font=("goudy old style",15,"bold"),bg="white").place(x=25,y=220)
        lbl_email=Label(frame1,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=380,y=120)
        lbl_secu_Anser=Label(frame1,text="Security Answer",font=("goudy old style",15,"bold"),bg="white").place(x=380,y=170)
        lbl_conform_pass=Label(frame1,text="Confirm Password",font=("goudy old style",15,"bold"),bg="white").place(x=380,y=225)
        #================variables================================
        self.var_First_name=StringVar()
        self.var_last_name=StringVar()
        self.var_sey_question=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_pass_2=StringVar()
        self.var_s_a=StringVar()
        self.var_btn_chk=IntVar()
        #=========Entrys+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.eny_First_Name=Entry(frame1,textvariable=self.var_First_name,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_First_Name.bind("<FocusIn>",lambda e: self.eny_First_Name.configure(background="BlACK",fg="light yellow"))
        self.eny_First_Name.bind("<FocusOut>",lambda e: self.eny_First_Name.configure(background="light yellow",fg="black"))
        self.eny_First_Name.place(x=150,y=60,width=200)
        self.eny_last_Name=Entry(frame1,textvariable=self.var_last_name,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_last_Name.bind("<FocusIn>",lambda e: self.eny_last_Name.configure(background="BlACK",fg="light yellow"))
        self.eny_last_Name.bind("<FocusOut>",lambda e: self.eny_last_Name.configure(background="light yellow",fg="black"))
        self.eny_last_Name.place(x=500,y=60,width=200)
        self.eny_contact=Entry(frame1,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_contact.bind("<FocusIn>",lambda e: self.eny_contact.configure(background="BlACK",fg="light yellow"))
        self.eny_contact.bind("<FocusOut>",lambda e: self.eny_contact.configure(background="light yellow",fg="black"))
        self.eny_contact.place(x=150,y=120,width=200)
        self.eny_email=Entry(frame1,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_email.bind("<FocusIn>",lambda e: self.eny_email.configure(background="BlACK",fg="light yellow"))
        self.eny_email.bind("<FocusOut>",lambda e: self.eny_email.configure(background="light yellow",fg="black"))
        self.eny_email.place(x=500,y=120,width=200)
        self.sey_question=ttk.Combobox(frame1,textvariable=self.var_sey_question,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.sey_question['values']=('Select Question','Your First Name','Your D.O.B','Your Friends Name','Your Favorite Play')
        self.sey_question.place(x=150,y=170,width=200)
        self.sey_question.current(0)
        self.eny_pass=Entry(frame1,textvariable=self.var_pass,font=("goudy old style",15,"bold"),bg="light yellow",show="*")
        self.eny_pass.bind("<FocusIn>",lambda e: self.eny_pass.configure(background="BlACK",fg="light yellow"))
        self.eny_pass.bind("<FocusOut>",lambda e: self.eny_pass.configure(background="light yellow",fg="black"))
        self.eny_pass.place(x=150,y=225,width=200)
        self.eny_s_a=Entry(frame1,textvariable=self.var_s_a,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_s_a.bind("<FocusIn>",lambda e: self.eny_s_a.configure(background="BlACK",fg="light yellow"))
        self.eny_s_a.bind("<FocusOut>",lambda e: self.eny_s_a.configure(background="light yellow",fg="black"))
        self.eny_s_a.place(x=550,y=170,width=150)
        self.eny_pass_2=Entry(frame1,textvariable=self.var_pass_2,font=("goudy old style",15,"bold"),bg="light yellow",show="*")
        self.eny_pass_2.bind("<FocusIn>",lambda e: self.eny_pass_2.configure(background="BlACK",fg="light yellow"))
        self.eny_pass_2.bind("<FocusOut>",lambda e: self.eny_pass_2.configure(background="light yellow",fg="black"))
        self.eny_pass_2.place(x=568,y=225,width=130)
        #======================Buttions+++++++++++++++++++++++++++++++++++++++++++++++
        self.chk=Checkbutton(frame1,text='I Agree Terms & Conditions',variable=self.var_btn_chk,activebackground="white",font=("times new roman",12),bg="white",onvalue=1,offvalue=0)
        self.chk.place(x=25,y=275)
        self.bt_image = ImageTk.PhotoImage(file="P:\hr\project/images/register.png")
        self.bt=Button(frame1,image=self.bt_image,bd=0,cursor="hand2",command=self.register)
        self.bt.bind("<Enter>",lambda e :move() )
        self.bt.place(x=25,y=330)
        def move():
            if self.var_First_name.get()=="" or self.var_last_name.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="" or self.var_pass_2.get()=="" or self.var_sey_question.get()=="" or self.var_s_a.get()=="":
                sr=random.randint(50,400)
                self.bt.place(x=sr,y=330)
            
    def clear(self):
        self.var_First_name.set("")
        self.var_last_name.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_pass.set("")
        self.var_pass_2.set("") 
        self.var_sey_question.set("Select Question") 
        self.var_s_a.set("")
      
    def register(self):
        if self.var_First_name.get()=="" or self.var_last_name.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="" or self.var_pass_2.get()=="" or self.var_sey_question.get()=="" or self.var_s_a.get()=="":
            messagebox.showerror("Error","Colum is Empty  Please Enter the Required Value",parent=self.form_SMS)
        else:    
            for char in self.var_First_name.get():
               if not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") ):
                  if  ("1"<=char and char <="9")or(char=="_" or char=="@"):
                    messagebox.showerror("Error",f"Do Not Enter This Name -> [{char}]",parent=self.form_SMS)
                    break
                   
            for char in self.var_last_name.get():
                if not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") ):
                  if  ("1"<=char and char <="9")or(char=="_" or char=="@"):
                    messagebox.showerror("Error",f"Do Not Enter This Name -> [{char}]",parent=self.form_SMS)
                    break
            c=self.var_contact.get()
            if  c.isalpha():
              messagebox.showerror("Error",f"only Enter the Number NO Enter the [{c}]  ->",parent=self.form_SMS)
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            s=re.search(regex,self.var_email.get())
            if s==None:
                messagebox.showerror("Error","invalid Email please Enter the valid email",parent=self.form_SMS)
                
              

            p=self.var_pass.get()
            p1=self.var_pass_2.get()
            if (len(p)<=8 and p!="")or (len(p1)<=8 and p!=""):
                messagebox.showerror("Error",f"-->Password Maximum Length  8 ")
            elif p!=p1:
                messagebox.showerror("Error",f"-->Password & Conform Password Deferent {p1}",parent=self.form_SMS)
            elif self.var_btn_chk.get()==0:
                messagebox.showerror("Error","Please Agree Our terms and Conditions",parent=self.form_SMS)   
            else:
                con=sqlite3.connect(database="rms.db")
                c=con.cursor()
                c.execute("Select * from reg  where Email=?",(self.var_email.get(),))
                r=c.fetchone()
                c.execute("Select * from reg  where password=?",(self.var_pass.get(),))
                p=c.fetchone()
                if r!=None:
                    messagebox.showerror("Error","User Already Exits , Please try With Another Email",parent=self.form_SMS)
                elif p!=None:
                    messagebox.showerror("Error","password Already Exits , Please Enter to Another password",parent=self.form_SMS)
                else:
                    try:
                        c.execute("insert into reg (F_Name,L_Name,Contact,Email,question,ans ,password)values(?,?,?,?,?,?,?)",(self.var_First_name.get(),self.var_last_name.get(),self.var_contact.get(),self.var_email.get(),self.var_sey_question.get(),self.var_s_a.get(),self.var_pass.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","  register Successfully",parent=self.form_SMS)
                        os.system("python Admin.py")
                        self.form_SMS.destroy()
                    except Exception as es:
                        messagebox.showerror("Error",f"Error due to  {str(es)}",parent=self.form_SMS) 
        
if __name__ == "__main__":
    ob_form = Tk() 
    obj_form = fo(ob_form)
    ob_form.mainloop()        
