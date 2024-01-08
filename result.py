from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
class Result:
    def __init__(self, new_win):
        self.new_win =new_win
        self.new_win.geometry("1250x450+0+200")
        self.new_win.resizable(False,False)
        self.new_win.focus_force()
        self.new_win.config(background="white")
        self.new_win.iconbitmap("P:\hr\project/images/ri.ico")
        self.new_win.title(" RESULTS MANAGEMENT SYSTEMS")
        #------------------------------------Title _---------------------------------------------------
        l={"Red","Yellow","Violet","MediumSlateBlue","Lime","Aqua","Blue","white","BlanchedAlmond","HoneyDew"}
        for i in l:
         title = Label(self.new_win, text="Add Student Result", font=("goudy old style", 20, "bold"),bg="#033055", fg=i)
         title.place(x=15, y=15, width=1215, height=50)
         #---------------------------image contetnt=================================================
         self.bg_image = ImageTk.PhotoImage(file="P:\hr\project/images/results-out-featured-image.jpg")
         self.bg_lb = Label(self.new_win, image=self.bg_image,bg=i)
         self.bg_lb.place(x=650, y=100,width=575,height=300)
        #-----------------------------------LABELS------------------------------------------
        lbl_sele_student=Label(self.new_win,text="Select Student",font=("goudy old style",15,"bold"),bg="white").place(x=40,y=100)
        lbl_name=Label(self.new_win,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=40,y=150)
        lbl_course=Label(self.new_win,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=40,y=200)
        lbl_mark_obt=Label(self.new_win,text="Marks",font=("goudy old style",15,"bold"),bg="white").place(x=40,y=250)
        lbl_full_maks=Label(self.new_win,text="Full marks",font=("goudy old style",15,"bold"),bg="white").place(x=40,y=300)
#------------------------varibles----------------------------------------------------------------------------
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_cousre=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.featch_roll()
        #---------------------------------------------entrys--------------------------------------------------------------
        self.eny_sele_stud=ttk.Combobox(self.new_win,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.eny_sele_stud.place(x=215,y=100,width=250)
        self.eny_sele_stud.set("Select")
        self.eny_name=Entry(self.new_win,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="light yellow",state="readonly")
        self.eny_name.bind("<FocusIn>",lambda e: self.eny_name.configure(background="BlACK",fg="light yellow"))
        self.eny_name.bind("<FocusOut>",lambda e: self.eny_name.configure(background="light yellow",fg="black"))
        self.eny_name.place(x=215,y=150,width=405,height=30)
        self.eny_course=Entry(self.new_win,textvariable=self.var_cousre,font=("goudy old style",15,"bold"),bg="light yellow",state="readonly")
        self.eny_course.bind("<FocusIn>",lambda e:self.eny_course.configure(background="BlACK",fg="light yellow"))
        self.eny_course.bind("<FocusOut>",lambda e:self.eny_course.configure(background="light yellow",fg="black"))
        self.eny_course.place(x=215,y=200,width=405,height=30)
        self.eny_mark=Entry(self.new_win,textvariable=self.var_marks,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_mark.bind("<FocusIn>",lambda e: self.eny_mark.configure(background="BlACK",fg="light yellow"))
        self.eny_mark.bind("<FocusOut>",lambda e: self.eny_mark.configure(background="light yellow",fg="black"))
        self.eny_mark.place(x=215,y=250,width=405,height=30)
        self.eny_full_marks=Entry(self.new_win,textvariable=self.var_full_marks,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_full_marks.bind("<FocusIn>",lambda e:self.eny_full_marks.configure(background="BlACK",fg="light yellow"))
        self.eny_full_marks.bind("<FocusOut>",lambda e:self.eny_full_marks.configure(background="light yellow",fg="black"))
        self.eny_full_marks.place(x=215,y=300,width=405,height=30)
        #-------------------Butttions---------------------------------------------------------------------
        self.bt_ser_students=Button(self.new_win,text="Search",font=("goudy old style ",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",activebackground="#2196f3",command=self.serach)
        self.bt_ser_students.place(x=500,y=100,width=120,height=35)
        self.bt_sumbit=Button(self.new_win,text="Submit",font=("goudy old style ",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",activebackground="#4caf50",command=self.add)
        self.bt_sumbit.place(x=350,y=360,width=120,height=40)
        self.btc=Button(self.new_win,text="Clear",font=("goudy old style ",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",activebackground="#607d8b",command=self.clear)
        self.btc.place(x=500,y=360,width=120,height=40)

        #-----------------featch students details------------------------
    def featch_roll(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("Select roll from students")
            rows=curser.fetchall()
            if len(rows)>0:
                for i in rows: 
                    self.roll_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.new_win)
    def serach(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("select Name,course from students where roll=?",(self.var_roll.get(),))
            row=curser.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_cousre.set(row[1])
            else:
                messagebox.showerror("Error","NO Record Found",parent=self.new_win)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def add(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please First Search Student  record",parent=self.new_win)
            else: 
                curser.execute("Select * from results where roll=? and course=?",(self.var_roll.get(),self.var_cousre.get(),))
                row=curser.fetchone()
                if row != None:
                    messagebox.showerror("Error","results already present",parent=self.new_win)
                else:
                    curser.execute("insert into results (roll,Name,course,marks,full_marks)values(?,?,?,?,?)",(self.var_roll.get(),self.var_name.get(),self.var_cousre.get(),self.var_marks.get(),self.var_full_marks.get()))
                    con.commit()
                    messagebox.showinfo("Success","Results Added Successfully",parent=self.new_win)     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.new_win)      
    def clear(self):
        self.var_roll.set("Select"),self.var_name.set(""),self.var_cousre.set(""),self.var_marks.set(""),self.var_full_marks.set("")                     

if __name__ == "__main__":
    ob = Tk()
    obj = Result(ob)
    ob.mainloop()
         
