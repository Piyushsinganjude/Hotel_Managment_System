from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from  tkinter import messagebox

class Support_win:
    def __init__(self,root):    #__init__ for construction calling & root is window 
        self.root=root
        self.root.title("Report")
        self.root.geometry("1295x550+230+220") 

        img1=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\help_desk.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=140,width=1550,height=620) 
        
        img3=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\Untitled-design-1-1.webp")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg2=Label(main_frame,image=self.photoimage3,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=1310,height=590)
        
        lbl_support=Label(main_frame,text="SUPPORT",font=("times new roman",30,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_support.place(x=500,y=0,width=300)
        
        lbl_Help=Label(main_frame,text="piyushsinganjude007@gmail.com",font=("times new roman",20,"bold"),fg="black",bg="White",bd=4,relief=RIDGE)
        lbl_Help.place(x=450,y=100,width=400)
        
if __name__ == "__main__":
    root=Tk()
    obj=Support_win(root)
    root.mainloop()
     