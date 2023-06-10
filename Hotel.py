from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom
from report import Support_win

class HotelManagementSystem:
    def __init__(self,root):    #__init__ for construction calling & root is window 
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0") 
        
        #************ 1st Upper Image***********
        
        img1=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\img1.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #*********** Logo **************
        
        img2=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\Hotel_Logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(self.root,image=self.photoimage2,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=230,height=140)
        
        #************* Title **************
        
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)    
        
        #*********Frame***************
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)      
        
        #*********** MENU *************
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)  
        
        #*********btn Frame***************
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)    
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,font=("times new roman",14,"bold"),fg="gold",bg="black",bd=0,cursor="hand2",width=22)
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",command=self.Room_details,font=("times new roman",14,"bold"),fg="gold",bg="black",bd=0,cursor="hand2",width=22)
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,font=("times new roman",14,"bold"),fg="gold",bg="black",bd=0,cursor="hand2",width=22)
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",command=self.Report_data,font=("times new roman",14,"bold"),fg="gold",bg="black",bd=0,cursor="hand2",width=22)
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,font=("times new roman",14,"bold"),fg="gold",bg="black",bd=0,cursor="hand2",width=22)
        logout_btn.grid(row=4,column=0,pady=1)
        
        
        #************ Right side image ************8
         
        img3=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\internal_slide3.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg2=Label(main_frame,image=self.photoimage3,bd=4,relief=RIDGE)
        lblimg2.place(x=225,y=0,width=1310,height=590)
        
        #************Down images************
        img4=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\down_img1.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg3=Label(main_frame,image=self.photoimage4,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=225,width=230,height=210)
        
        img5=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\down_img2.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        lblimg3=Label(main_frame,image=self.photoimage5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=420,width=230,height=190)
   
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)
        
    def Room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
        
    def Report_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Support_win(self.new_window)
        
    def logout(self):
        self.root.destroy()
           
if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
     
        