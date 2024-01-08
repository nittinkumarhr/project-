from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
class STUDENT:
    def __init__(self, students_SMS):
        self.students_SMS =students_SMS
        self.students_SMS.geometry("1250x450+0+200")
        self.students_SMS.resizable(False,False)
        self.students_SMS.focus_force()
        self.students_SMS.config(background="white")
        self.students_SMS.iconbitmap("P:\hr\project\images\school_students_icon_144607.ico")
        self.students_SMS.title("STUDENTS MANAGEMENT SYSTEM")
        #--------- Title _-------------
        l={"Red","Yellow","Violet","MediumSlateBlue","Lime","Aqua","Blue","white","BlanchedAlmond","HoneyDew"}
        for i in l:
         title = Label(self.students_SMS, text="Manage Students Details", font=("goudy old style", 20, "bold"),bg="#033055", fg=i)
         title.place(x=15, y=15, width=1215, height=35)
         pass
     
        #------Variables--------------
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_state=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_Admission=StringVar()
        self.var_course=StringVar()
        self.var_city=StringVar()
    
        # -------------Widgets-----------------
        #---------------colum 1---------------------
        lbl_roll=Label(self.students_SMS,text="Roll no",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=60)
        lbl_name=Label(self.students_SMS,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=100)
        lbl_email=Label(self.students_SMS,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=140)
        lbl_gender=Label(self.students_SMS,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=180)
        lbl_state=Label(self.students_SMS,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=220)
        lbl_Address=Label(self.students_SMS,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=260)
        #--------------------colum 2---------------------
        lbl_Dob=Label(self.students_SMS,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)
        lbl_contact=Label(self.students_SMS,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)
        lbl_Admission=Label(self.students_SMS,text="Admission",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=140)
        lbl_course=Label(self.students_SMS,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)
        lbl_city=Label(self.students_SMS,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=215)
        #--------------- Widgets Enterys---------------
        self.eny_roll=Entry(self.students_SMS,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_roll.bind("<FocusIn>",lambda e: self.eny_roll.configure(background="BlACK",fg="light yellow"))
        self.eny_roll.bind("<FocusOut>",lambda e: self.eny_roll.configure(background="light yellow",fg="black"))
        self.eny_roll.place(x=150,y=60,width=200)
        self.eny_name=Entry(self.students_SMS,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_name.bind("<FocusIn>",lambda e: self.eny_name.configure(background="BlACK",fg="light yellow"))
        self.eny_name.bind("<FocusOut>",lambda e: self.eny_name.configure(background="light yellow",fg="black"))
        self.eny_name.place(x=150,y=100,width=200)
        self.eny_email=Entry(self.students_SMS,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_email.bind("<FocusIn>",lambda e:self.eny_email.configure(background="BlACK",fg="light yellow"))
        self.eny_email.bind("<FocusOut>",lambda e:self.eny_email.configure(background="light yellow",fg="black"))
        self.eny_email.place(x=150,y=140,width=200)
        self.eny_gender=ttk.Combobox(self.students_SMS,textvariable=self.var_gender,values=("Select","male","Female","other"),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.eny_gender.place(x=150,y=180,width=200)
        self.eny_gender.current(0)
        self.eny_state=Entry(self.students_SMS,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_state.bind("<FocusIn>",lambda e:self.eny_state.configure(background="BlACK",fg="light yellow"))
        self.eny_state.bind("<FocusOut>",lambda e:self.eny_state.configure(background="light yellow",fg="black"))
        self.eny_state.place(x=150,y=215,width=200)
        self.eny_Address=Text(self.students_SMS,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_Address.bind("<FocusIn>",lambda e: self.eny_Address.configure(background="BlACK",fg="light yellow"))
        self.eny_Address.bind("<FocusOut>",lambda e: self.eny_Address.configure(background="light yellow",fg="black"))
        self.eny_Address.place(x=150,y=250,width=530,height=100)
        #====================== entry two +===========================+++++++++++++++++
        self.eny_dob=Entry(self.students_SMS,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_dob.bind("<FocusIn>",lambda e: self.eny_dob.configure(background="BlACK",fg="light yellow"))
        self.eny_dob.bind("<FocusOut>",lambda e: self.eny_dob.configure(background="light yellow",fg="black"))
        self.eny_dob.place(x=480,y=60,width=200)
        self.eny_contact=Entry(self.students_SMS,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_contact.bind("<FocusIn>",lambda e: self.eny_contact.configure(background="BlACK",fg="light yellow"))
        self.eny_contact.bind("<FocusOut>",lambda e: self.eny_contact.configure(background="light yellow",fg="black"))
        self.eny_contact.place(x=480,y=100,width=200)
        self.eny_Admission=Entry(self.students_SMS,textvariable=self.var_Admission,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_Admission.bind("<FocusIn>",lambda e:self.eny_Admission.configure(background="BlACK",fg="light yellow"))
        self.eny_Admission.bind("<FocusOut>",lambda e:self.eny_Admission.configure(background="light yellow",fg="black"))
        self.eny_Admission.place(x=480,y=140,width=200)
        #--------------------------course details-------------------------
        self.course_details=[]
        self.fetch_course()
        self.eny_course=ttk.Combobox(self.students_SMS,textvariable=self.var_course,values=self.course_details,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.eny_course.place(x=480,y=180 ,width=200)
        self.eny_course.set("Empty")
        self.eny_city=Entry(self.students_SMS,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_city.bind("<FocusIn>",lambda e:self.eny_city.configure(background="BlACK",fg="light yellow"))
        self.eny_city.bind("<FocusOut>",lambda e:self.eny_city.configure(background="light yellow",fg="black"))
        self.eny_city.place(x=480,y=215 ,width=200)
        #------------------------Bunions------------------------------------
        self.btc=Button(self.students_SMS,text="Save",font=("goudy old style ",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btc.place(x=10,y=390,width=120,height=50)
        self.btu=Button(self.students_SMS,text="Update",font=("goudy old style ",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.Update)
        self.btu.place(x=150,y=390,width=120,height=50)
        self.btd=Button(self.students_SMS,text="Delete",font=("goudy old style ",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btd.place(x=290,y=390,width=120,height=50)
        self.btc=Button(self.students_SMS,text="Clear",font=("goudy old style ",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btc.place(x=435,y=390,width=120,height=50)
        #---------------search panel------------------------------
        self.var_ser_rollo=StringVar()
        ser_Rollo=Label(self.students_SMS,text="Roll no ",font=("goudy old style",15,"bold"),bg="white").place(x=725,y=60)
        ser_Rollo=Entry(self.students_SMS,textvariable=self.var_ser_rollo,font=("goudy old style",15,"bold"),bg="light yellow")
        ser_Rollo.bind("<FocusIn>",lambda e:ser_Rollo.configure(background="BlACK",fg="light yellow"))
        ser_Rollo.bind("<FocusOut>",lambda e:ser_Rollo.configure(background="light yellow",fg="black"))
        ser_Rollo.place(x=850,y=60,width=240)
        ser_Bution=Button(self.students_SMS,text="Search",font=("goudy old style ",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.serach)
        ser_Bution.place(x=1110,y=60,width=120,height=30)
        #-------------------------content-------------------------------
        self.c_Farame=Frame(self.students_SMS,bd=2,relief=RIDGE)
        self.c_Farame.place(x=720,y=120,width=510,height=300)
        self.scroll_y=Scrollbar(self.c_Farame,orient=VERTICAL)
        self.scroll_x=Scrollbar(self.c_Farame,orient=HORIZONTAL)
        #----------------------table-----------------------
        self.eny_table=ttk.Treeview(self.c_Farame,columns=( "roll","Name","email","gender","dob","contact","admission","course","state","city","adder"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.eny_table.xview)
        self.scroll_y.config(command=self.eny_table.yview)
        self.eny_table.heading("roll",text="Roll no")
        self.eny_table.heading("Name",text="Name")
        self.eny_table.heading("email",text="Email")
        self.eny_table.heading("gender",text="Gender")
        self.eny_table.heading("dob",text="D O B")
        self.eny_table.heading("contact",text="Contact")
        self.eny_table.heading("admission",text="Admission")
        self.eny_table.heading("course",text="Course")
        self.eny_table.heading("state",text="State")
        self.eny_table.heading("city",text="City")
        self.eny_table.heading("adder",text="Address")
        self.eny_table["show"]="headings"

        self.eny_table.column("roll",width=100)
        self.eny_table.column("Name",width=100)
        self.eny_table.column("email",width=100)
        self.eny_table.column("gender",width=100)
        self.eny_table.column("dob",width=100)
        self.eny_table.column("contact",width=100) 
        self.eny_table.column("admission",width=100)
        self.eny_table.column("course",width=100)
        self.eny_table.column("state",width=100)
        self.eny_table.column("city",width=100)
        self.eny_table.column("adder",width=200)
        self.eny_table.pack(fill=BOTH,expand=True)
        self.eny_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #+===============================+++++++++clear data+++++++++++++++++++++++++++++
    def clear(self):
        self.show()
        self.var_roll.set(""),self.var_name.set(""),self.var_email.set(""),self.var_gender.set("Select"),self.var_dob.set(""),self.var_contact.set(""),self.var_Admission.set(""),self.var_course.set("Empty"),self.var_state.set(""),self.var_city.set(""),self.eny_Address.delete("1.0",END)
        self.var_ser_rollo.set("")
#---------------------delete data in table------------------------------
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Roll should be required",parent=self.students_SMS)
            else: 
                curser.execute("Select * from students where roll=?",(self.var_roll.get(),))
                row=curser.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select Student from the list first ",parent=self.students_SMS)
                else:
                    op=messagebox.askyesno("Confirm","DO you want to delete",parent=self.students_SMS)
                    if op==True:
                        curser.execute("delete from students where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student  delete Successfully",parent=self.students_SMS)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")        
#===========================================================get data in table++++++++++++++++
    def get_data(self,ev):
         self.eny_roll.config(state="readonly")
         r=self.eny_table.focus()
         content=self.eny_table.item(r)
         row=content["values"]
         self.var_roll.set(row[0]),self.var_name.set(row[1]),self.var_email.set(row[2]),self.var_gender.set(row[3]),self.var_dob.set(row[4]),self.var_contact.set(row[5]),self.var_Admission.set(row[6]),self.var_course.set(row[7]),self.var_state.set(row[8]),self.var_city.set(row[9]),self.eny_Address.delete("1.0",END),self.eny_Address.insert(END, row[0])
#-----------------------add data In db----------------------------------------_
    def add(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            if self.var_roll.get()=="" or self.var_Admission.get()=="" or self.var_city.get()=="" or self.var_contact.get()=="" or self.var_name.get()==""or self.var_email.get()==""or self.var_gender.get()==""or self.var_dob.get()=="":
                messagebox.showerror("Error","All fields  should be required",parent=self.students_SMS)
            else: 
                curser.execute("Select * from students where roll=?",(self.var_roll.get(),))
                row=curser.fetchone()
                if row != None:
                    messagebox.showerror("Error","Roll number already present",parent=self.students_SMS)
                else:
                    curser.execute("insert into students (roll,Name,email,gender,dob,contact,admission,course,state,city,adder) values(?,?,?,?,?,?,?,?,?,?,?)",
                    (self.var_roll.get(),self.var_name.get(),self.var_email.get(),self.var_gender.get(),self.var_dob.get(),self.var_contact.get(),self.var_Admission.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.eny_Address.get("1.0",END)))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.students_SMS)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#------------------------------update---------------------------------------------------------------------
    def Update(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
                curser.execute("Select * from students where roll=?",(self.var_roll.get(),))
                row=curser.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select students From list",parent=self.students_SMS)
                else:
                    curser.execute("update students set Name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,adder=? where roll=?",
                    (self.var_name.get(),self.var_email.get(),self.var_gender.get(),self.var_dob.get(),self.var_contact.get(),self.var_Admission.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.eny_Address.get("1.0",END),self.var_roll.get()))
                    con.commit()
                    messagebox.showinfo("Success","Student  UPDATE Successfully",parent=self.students_SMS)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#-----------------------Show data in table----------------------------------------      
    def show(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("Select * from students")
            rows=curser.fetchall()
            self.eny_table.delete(*self.eny_table.get_children())
            for row in rows:
                self.eny_table.insert('', END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#--------------------------featch course details---------------------------------------------------
    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("Select name from course")
            rows=curser.fetchall()

            if len(rows)>0:
                for i in rows: 
                    self.course_details.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    #-------------------------Search the data in table --------------------
    def serach(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("Select * from students where roll=?",(self.var_ser_rollo.get(),))
            row=curser.fetchone()
            if row!=None:
             self.eny_table.delete(*self.eny_table.get_children())
             self.eny_table.insert('', END,values=row)
            else:
                messagebox.showerror("Error","NO Record Found",parent=self.students_SMS)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
if __name__ == "__main__":
    ob_student = Tk()
    obj_st = STUDENT(ob_student)
    ob_student.mainloop()
 
