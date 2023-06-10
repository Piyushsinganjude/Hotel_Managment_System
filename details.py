from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from  tkinter import messagebox
from time import strftime
from datetime import datetime


class DetailsRoom:
    def __init__(self,root): #__init__ for construction calling & root is window 
        self.root=root
        self.root.title("Room Details")
        self.root.geometry("1295x550+230+220") 
        
        
                  #************* Title **************
        
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)    
        
        #*********** Logo **************
        
        img2=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\Hotel_Logo.jpg")  # r is to convert single slash into double back slash
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(self.root,image=self.photoimage2,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=100,height=50)  
        
        #variables
        
        self.var_floor=StringVar()
        self.var_roomNo=StringVar()
        self.var_roomType=StringVar()
        
                #************* Label frame***********
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)
        
        #********* labels & entry *******************
        #Floor
        lbl_Floor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Floor.grid(row=0,column=0,sticky=W)
        
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=17,font=("times new roman",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)
        
         #RoomNo
        lbl_RoomNo=Label(labelframeleft,text="Room No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=17,font=("times new roman",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)
        
         #Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_roomType,width=17,font=("times new roman",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)
        
        
        #**********btn***********8
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.Reset_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
         #************ Table Frame & Search System*******
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=600,y=55,width=600,height=350)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(Table_frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        # Adding Scroll bar
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
         #adding table & its headings into the Frame 
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No.")
        self.room_table.heading("roomType",text="Room Type")
    
        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
      
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    #********************* Add Data to database ************
        
    def add_data(self):   
        if self.var_floor.get()=="" or self.var_roomType.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
                cur=conn.cursor()
                cur.execute("insert into details values(%s,%s,%s)",(
                                                                          self.var_floor.get(),
                                                                          self.var_roomNo.get(),
                                                                          self.var_roomType.get()
                                                            
                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully!",parent=self.root)
            except Exception as es:
                    messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)
    
    
     # Showing Data in the table on Frame which stored into the database       
    def fetch_data(self):
        
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select * from details")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('',END,values=i)
            conn.commit()
        conn.close()
    
    
    #Retriving Data For Use and Update into text fields   **Get Cursor**
     
    def get_cursor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_roomType.set(row[2])
        
     # Update data
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor No",parent=self.root)
        else:
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            cur.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                                self.var_floor.get(),
                                                                                                                                self.var_roomType.get(),
                                                                                                                                self.var_roomNo.get(),
                                                                                                                                
                                                                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details Has Been Updated Successfully!",parent=self.root)
            
     # Delete The Customer Details
    def Delete_data(self):
        Delete_data=messagebox.askyesno("Hotel Management System","Do You Want Delete This Room Details?",parent=self.root)
        if Delete_data>0:
            
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            query=("delete from details where RoomNo=%s")
            value=(self.var_roomNo.get(),)
            cur.execute(query,value)
        else:
            if not Delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    # To Reset the text fields of Customer Details
    def Reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_roomType.set(""),
        
        
           
if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()