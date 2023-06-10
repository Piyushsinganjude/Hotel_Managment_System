from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from  tkinter import messagebox
from time import strftime
from datetime import datetime


class Roombooking:
    def __init__(self,root): #__init__ for construction calling & root is window 
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1295x550+230+220") 
        
        #*************** Variables **************
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        
        
               #************* Title **************
        
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)    
        
        #*********** Logo **************
        
        img2=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\Hotel_Logo.jpg")  # r is to convert single slash into double back slash
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(self.root,image=self.photoimage2,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=100,height=50)  
        
                #************* Label frame***********
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        #********* labels & entry *******************
        #Cust_Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,width=17,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        #check_in_date
        check_in_date=Label(labelframeleft,text="Check_in Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        
        txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("times new roman",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)
        
        #Check_out Date
        lbl_Check_out=Label(labelframeleft,text="Check_out Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("times new roman",13,"bold"))
        txt_Check_out.grid(row=2,column=1)
        
        #Room Type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select RoomType from details")
        Ide=cur.fetchall()
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        #Available Room
        lbl_AvailableRoom=Label(labelframeleft,text="Available Room:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_AvailableRoom.grid(row=4,column=0,sticky=W)
        #txt_AvailableRoom=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomavailable,font=("times new roman",13,"bold"))
        #txt_AvailableRoom.grid(row=4,column=1)
        
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select RoomNo from details where RoomNo =any(select RoomNo where RoomType='Single')")
        row1=cur.fetchall()
        
        combo_RoomNo_S=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=8,state="readonly")
        combo_RoomNo_S["value"]=row1
        
        combo_RoomNo_S.grid(row=4,column=1,sticky=W)
        
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select RoomNo from details where RoomNo =any(select RoomNo where RoomType='Double')")
        row2=cur.fetchall()
        
        combo_RoomNo_D=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=8,state="readonly")
        combo_RoomNo_D["value"]=row2
        
        combo_RoomNo_D.place(x=220,y=145)
        
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select RoomNo from details where RoomNo =any(select RoomNo where RoomType='Luxury')")
        row3=cur.fetchall()
        
        combo_RoomNo_L=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=8,state="readonly")
        combo_RoomNo_L["value"]=row3
        
        combo_RoomNo_L.place(x=310,y=145)
        
        S_label=Label(labelframeleft,text="S",font=("open sans",8),fg="firebrick1",bg="white")
        S_label.place(x=180,y=145)
        
        D_label=Label(labelframeleft,text="D",font=("open sans",8),fg="firebrick1",bg="white")
        D_label.place(x=280,y=145)
        
        L_label=Label(labelframeleft,text="L",font=("open sans",8),fg="firebrick1",bg="white")
        L_label.place(x=370,y=145)

        
         #Meal
        lbl_Meal=Label(labelframeleft,text="Meal:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Meal.grid(row=5,column=0,sticky=W)
        #txt_Meal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("times new roman",13,"bold"))
        #txt_Meal.grid(row=5,column=1)
        combo_Meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_Meal["value"]=("Breakfast","Lunch","Dinner")
        combo_Meal.current(0)
        combo_Meal.grid(row=5,column=1)
        
         #No of Days
        lbl_NoofDays=Label(labelframeleft,text="No. of Days:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_NoofDays.grid(row=6,column=0,sticky=W)
        txt_NoofDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("times new roman",13,"bold"))
        txt_NoofDays.grid(row=6,column=1)
        
         #Paid Tax
        lbl_PaidTax=Label(labelframeleft,text="Paid Tax:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_PaidTax.grid(row=7,column=0,sticky=W)
        txt_PaidTax=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("times new roman",13,"bold"))
        txt_PaidTax.grid(row=7,column=1)
        
        #Sub Total
        lbl_SubTotal=Label(labelframeleft,text="Sub Total:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_SubTotal.grid(row=8,column=0,sticky=W)
        txt_SubTotal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("times new roman",13,"bold"))
        txt_SubTotal.grid(row=8,column=1)
        
        #Total cost
        lbl_TotalCost=Label(labelframeleft,text="Total Cost:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_TotalCost.grid(row=9,column=0,sticky=W)
        txt_TotalCost=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("times new roman",13,"bold"))
        txt_TotalCost.grid(row=9,column=1)
        
        #Fetch Data Button
        btnFetch=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contact,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnFetch.place(x=295,y=4)
        
        # Bill Button
        btnBill=Button(labelframeleft,text="Bill",command=self.total ,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        
                #**********btn***********8
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.Reset_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
        #***************** RightSide Image**************
        img3=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\bed.jpg")  # r is to convert single slash into double back slash
        img3=img3.resize((520,200),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimage3,bd=2,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200) 
        
         #************ Table Frame & Search System*******
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=435,y=280,width=860,height=260)
        
        lblSearchBy=Label(Table_frame,text="search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        
        txtsearch=ttk.Entry(Table_frame,width=29,textvariable=self.txt_search,font=("times new roman",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_frame,text="Search",comman=self.Search_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnSearch.grid(row=0,column=3,padx=2)
        
        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnShowAll.grid(row=0,column=4,padx=2)
        
        #************* Show Data Table *************8
        
        details_table=LabelFrame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal",
                                                                   "noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        # Adding Scroll bar
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        #adding table & its headings into the Frame 
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No. Of Days")

        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        #********************* Add Data to database ************
        
    def add_data(self):   
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
                cur=conn.cursor()
                cur.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                          self.var_contact.get(),
                                                                          self.var_checkin.get(),
                                                                          self.var_checkout.get(),
                                                                          self.var_roomtype.get(),
                                                                          self.var_roomavailable.get(),
                                                                          self.var_meal.get(),
                                                                          self.var_noofdays.get()
                                                                            
                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                    messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)
    
     # Showing Data in the table on Frame which stored into the database       
    def fetch_data(self):
        
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select * from room")
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
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
        
         # Update data
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            cur.execute("update room set check_in=%s,check_out=%s,roomtype=%s,RoomAvailable=%s,meal=%s,noOfdays=%s where contact=%s",(
                                                                                                                                self.var_checkin.get(),
                                                                                                                                self.var_checkout.get(),
                                                                                                                                self.var_roomtype.get(),
                                                                                                                                self.var_roomavailable.get(),
                                                                                                                                self.var_meal.get(),
                                                                                                                                self.var_noofdays.get(),
                                                                                                                                self.var_contact.get()
                                                                            
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
            query=("delete from room where contact=%s")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
        else:
            if not Delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    # To Reset the text fields of Customer Details
    def Reset_data(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")
        
         
        #***************** All Data Fetch ************
        
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","This Number is Not Found",parent=self.root)
            else:
                conn.commit()
            conn.close()
            
            showDataFrame=Frame(self.root,bd=4,relief=RIDGE)
            showDataFrame.place(x=455,y=55,width=300,height=180)
            
            #***********Fetch Name***********
            lblName=Label(showDataFrame,text="Name:",font=("times new roman",11,"bold"))
            lblName.place(x=0,y=0)
            
            lbl=Label(showDataFrame,text=row,font=("times new roman",11,"bold"))
            lbl.place(x=90,y=0)
            
            #************ Fetch Gender********
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
 
            lblGender=Label(showDataFrame,text="Gender:",font=("times new roman",11,"bold"))
            lblGender.place(x=0,y=30)
            
            lbl_G=Label(showDataFrame,text=row,font=("times new roman",11,"bold"))
            lbl_G.place(x=90,y=30)
            
            #************ Fetch Email********
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            query=("select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
 
            lblEmail=Label(showDataFrame,text="Email:",font=("times new roman",11,"bold"))
            lblEmail.place(x=0,y=60)
            
            lbl_E=Label(showDataFrame,text=row,font=("times new roman",11,"bold"))
            lbl_E.place(x=90,y=60) 
            
            #************ Fetch Nationality********
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
 
            lblNationality=Label(showDataFrame,text="Nationality:",font=("times new roman",11,"bold"))
            lblNationality.place(x=0,y=90)
            
            lbl_N=Label(showDataFrame,text=row,font=("times new roman",11,"bold"))
            lbl_N.place(x=90,y=90) 
            
            #************ Fetch Address********
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            query=("select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
 
            lblAddress=Label(showDataFrame,text="Address:",font=("times new roman",11,"bold"))
            lblAddress.place(x=0,y=120)
            
            lbl_Address=Label(showDataFrame,text=row,font=("times new roman",11,"bold"))
            lbl_Address.place(x=90,y=120)            
    
    # To search information of Room
    def Search_data(self):
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cur.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
                
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y") 
        outDate=datetime.strptime(outDate,"%d/%m/%Y")     
        self.var_noofdays.set(abs(outDate-inDate).days) 
        
        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            
            q1=float(200)
            q2=float(700) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            
            q1=float(200)
            q2=float(1400) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
                
            q1=float(200)
            q2=float(2000) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
                
            q1=float(300)
            q2=float(700) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            
            q1=float(300)
            q2=float(1400) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
                
            q1=float(300)
            q2=float(2000) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
                
            q1=float(400)
            q2=float(700) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            
            q1=float(400)
            q2=float(1400)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
                
            q1=float(400)
            q2=float(2000) 
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.02))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.02)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()