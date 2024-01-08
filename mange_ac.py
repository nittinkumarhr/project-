from tkinter import *
from PIL import Image, ImageTk  # pip install pillow 
from tkinter import ttk,messagebox

class  my_Account:
    def __init__(self, root):
        self.root =root
        self.root.title("Mange Account")
        self.root.geometry("1250x450+0+200")
        self.root.resizable(False,False)
              
if __name__ == "__main__":
    main_ob = Tk()
    obj = my_Account(main_ob)
    main_ob.mainloop()         