from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox
import sqlite3
class RMS1:
    def __init__(self, new_win):
        self.new_win =new_win
        self.new_win.geometry("1250x450+0+200")
        self.new_win.resizable(False,False)
        self.new_win.focus_force()
        self.new_win.config(background="white")
        self.new_win.iconbitmap("P:\hr\project/images/courseico.ico")
        self.new_win.title("COURSE MANAGEMENT SYSTEM")
        #--------- Title _-------------
        l={"Red","Yellow","Violet","MediumSlateBlue","Lime","Aqua","Blue","white","BlanchedAlmond","HoneyDew"}
        for i in l:
         title = Label(self.new_win, text="Manage Course Details", font=("goudy old style", 20, "bold"),bg="#033055", fg=i)
         title.place(x=15, y=15, width=1215, height=35)
        #------Varibles--------------
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_changes=StringVar()
        # -------------Widgets-----------------
        lbl_cursename=Label(self.new_win,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=60)
        lbl_duration=Label(self.new_win,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=100)
        lbl_Changes=Label(self.new_win,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=140)
        lbl_Description=Label(self.new_win,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=180)
        #--------------- Widgets Enterys---------------
        self.eny_cursename=Entry(self.new_win,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_cursename.bind("<FocusIn>",lambda e: self.eny_cursename.configure(background="BlACK",fg="light yellow"))
        self.eny_cursename.bind("<FocusOut>",lambda e: self.eny_cursename.configure(background="light yellow",fg="black"))
        self.eny_cursename.place(x=150,y=60,width=200)
        self.eny_duration=Entry(self.new_win,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_duration.bind("<FocusIn>",lambda e: self.eny_duration.configure(background="BlACK",fg="light yellow"))
        self.eny_duration.bind("<FocusOut>",lambda e: self.eny_duration.configure(background="light yellow",fg="black"))
        self.eny_duration.place(x=150,y=100,width=200)
        self.eny_Changes=Entry(self.new_win,textvariable=self.var_changes,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_Changes.bind("<FocusIn>",lambda e: self.eny_Changes.configure(background="BlACK",fg="light yellow"))
        self.eny_Changes.bind("<FocusOut>",lambda e: self.eny_Changes.configure(background="light yellow",fg="black"))
        self.eny_Changes.place(x=150,y=140,width=200)
        self.eny_Description=Text(self.new_win,font=("goudy old style",15,"bold"),bg="light yellow")
        self.eny_Description.bind("<FocusIn>",lambda e: self.eny_Description.configure(background="BlACK",fg="light yellow"))
        self.eny_Description.bind("<FocusOut>",lambda e: self.eny_Description.configure(background="light yellow",fg="black"))
        self.eny_Description.place(x=150,y=180,width=400,height=180)
        #------------------------Butions------------------------------
        self.btc=Button(self.new_win,text="Save",font=("goudy old style ",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btc.place(x=10,y=390,width=120,height=50)
        self.btu=Button(self.new_win,text="Update",font=("goudy old style ",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.Update)
        self.btu.place(x=150,y=390,width=120,height=50)
        self.btd=Button(self.new_win,text="Delete",font=("goudy old style ",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btd.place(x=290,y=390,width=120,height=50)
        self.btc=Button(self.new_win,text="Clear",font=("goudy old style ",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btc.place(x=435,y=390,width=120,height=50)
        #---------------serach panel------------------------------
        self.var_ser_course=StringVar()
        ser_cursename1=Label(self.new_win,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=700,y=60)
        ser_cursename=Entry(self.new_win,textvariable=self.var_ser_course,font=("goudy old style",15,"bold"),bg="light yellow")
        ser_cursename.bind("<FocusIn>",lambda e:  ser_cursename.configure(background="BlACK",fg="light yellow"))
        ser_cursename.bind("<FocusOut>",lambda e:  ser_cursename.configure(background="light yellow",fg="black"))
        ser_cursename.place(x=850,y=60,width=240)
        ser_Bution=Button(self.new_win,text="Search",font=("goudy old style ",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.serach)
        ser_Bution.place(x=1110,y=60,width=120,height=30)
        #-------------------------content-------------------------------
        self.c_Farame=Frame(self.new_win,bd=2,relief=RIDGE)
        self.c_Farame.place(x=720,y=120,width=510,height=300)
        self.scroll_y=Scrollbar(self.c_Farame,orient=VERTICAL)
        self.scroll_x=Scrollbar(self.c_Farame,orient=HORIZONTAL)
        #----------------------table-----------------------
        self.eny_table=ttk.Treeview(self.c_Farame,columns=("Cid","Name","duration","charges","description"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.eny_table.xview)
        self.scroll_y.config(command=self.eny_table.yview)
        self.eny_table.heading("Cid",text="Course ID")
        self.eny_table.heading("Name",text="Name")
        self.eny_table.heading("duration",text="Duration")
        self.eny_table.heading("charges",text="Charges")
        self.eny_table.heading("description",text="Description")
        self.eny_table["show"]="headings"

        self.eny_table.column("Cid",width=100)
        self.eny_table.column("Name",width=100)
        self.eny_table.column("duration",width=100)
        self.eny_table.column("charges",width=100)
        self.eny_table.column("description",width=150)
        self.eny_table.pack(fill=BOTH,expand=True)
        self.eny_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #+===============================+++++++++clear data+++++++++++++++++++++++++++++
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("") 
        self.var_changes.set("")
        self.var_ser_course.set("")
        self.eny_Description.delete("1.0",END)
        self.eny_cursename.configure(state=NORMAL)
#---------------------delete data in table------------------------------
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be requerd",parent=self.new_win)
            else: 
                curser.execute("Select * from course where name=?",(self.var_course.get(),))
                row=curser.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select course from the list first ",parent=self.new_win)
                else:
                    op=messagebox.askyesno("Confirm","DO you want to delete",parent=self.new_win)
                    if op==True:
                        curser.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","course delete Successfully",parent=self.new_win)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")        
#===========================================================get data in table++++++++++++++++
    def get_data(self,ev):
         self.eny_cursename.config(state="readonly")
         r=self.eny_table.focus()
         content=self.eny_table.item(r)
         row=content["values"]
         self.var_course.set(row[1])
         self.var_duration.set(row[2])
         self.var_changes.set(row[3])
         self.eny_Description.delete('1.0',END)
         self.eny_Description.insert(END, row[4])
#-----------------------add data In db----------------------------------------
    def add(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.new_win)
            else: 
                curser.execute("Select * from course where name=?",(self.var_course.get(),))
                row=curser.fetchone()
                if row != None:
                    messagebox.showerror("Error","Course name already present",parent=self.new_win)
                else:
                    curser.execute("insert into course (name,duration,charges,description)values(?,?,?,?)",(self.var_course.get(),self.var_duration.get(),self.var_changes.get(),self.eny_Description.get("1.0",END)))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.new_win)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#------------------------------update---------------------------------------------------------------------
    def Update(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
                curser.execute("Select * from course where name=?",(self.var_course.get(),))
                row=curser.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select Course From list",parent=self.new_win)
                else:
                    curser.execute("update course set duration=?,charges=?,description=? where name=?",
                    (self.var_duration.get(),self.var_changes.get(),self.eny_Description.get("1.0",END),self.var_course.get()))
                    con.commit()
                    messagebox.showinfo("Success","Course UPDATE Successfully",parent=self.new_win)    
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#-----------------------Show data in table----------------------------------------      
    def show(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute("Select * from course")
            rows=curser.fetchall()
            self.eny_table.delete(*self.eny_table.get_children())
            for row in rows:
                self.eny_table.insert('', END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    #-------------------------Search the data in table --------------------
    def serach(self):
        con=sqlite3.connect(database="rms.db")
        curser=con.cursor()
        try:
            curser.execute(f"Select * from course where name LIKE '%{self.var_ser_course.get()}%'")
            rows=curser.fetchall()
            self.eny_table.delete(*self.eny_table.get_children())
            for row in rows:
                self.eny_table.insert('', END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
if __name__ == "__main__":
    ob = Tk()
    obj = RMS1(ob)
    ob.mainloop()
 
