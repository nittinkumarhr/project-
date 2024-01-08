import sqlite3
def crate_db():
    con=sqlite3.connect(database="rms.db")
    curser=con.cursor()

    curser.execute("CREATE TABLE IF NOT EXISTS course(Cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text)")
    con.commit()

    curser.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT,Name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,adder text)")
    con.commit()
     
    curser.execute("CREATE TABLE IF NOT EXISTS results(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,Name text,course text,marks text,full_marks text,present text)")
    con.commit()
    curser.execute("CREATE TABLE IF NOT EXISTS reg(rid INTEGER PRIMARY KEY AUTOINCREMENT,F_Name text,L_Name text,Contact text,Email text,question text,ans text,password text)")
    con.commit()
    con.close()
    con1=sqlite3.connect(database="form_db.db")
    curser1=con1.cursor()
    curser1.execute("CREATE TABLE IF NOT EXISTS form(rid INTEGER PRIMARY KEY AUTOINCREMENT,F_Name text,L_Name text,Contact text,Email text,question text,ans text,password text)")
    con1.commit()

    

crate_db()    