from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from  tkinter import messagebox


class Cust_win:
    def __init__(self,root):    #__init__ for construction calling & root is window 
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1295x550+230+220") 
        
        
        
        #****************variables***********8
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()
                
         #************* Title **************
        
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)    
        
        #*********** Logo **************
        
        img2=Image.open(r"C:\Project\Hotel management sysytem\Hotel_images\Hotel_Logo.jpg")  # r is to convert single slash into double back slash
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(self.root,image=self.photoimage2,bd=2,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=100,height=50)
        
        #************* Label frame***********
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        #********* labels & entry *******************
        #Cust_ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
        
        #Cust_name
        cname=Label(labelframeleft,text="Customer Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
        txtcname.grid(row=1,column=1)
        
        #mother_name
        mname=Label(labelframeleft,text="Mother Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("times new roman",13,"bold"))
        txtmname.grid(row=2,column=1)

        #gender_Combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        
        #postcode
        lblPostCode=Label(labelframeleft,text="PostCode:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("times new roman",13,"bold"))
        txtPostCode.grid(row=4,column=1)
        
        #mobile number
        lblMobile=Label(labelframeleft,text="Mobile:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
        txtMobile.grid(row=5,column=1)
        
        #email
        lblEmail=Label(labelframeleft,text="Email:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
        txtEmail.grid(row=6,column=1)
        
        #Nationality
        lblNationality=Label(labelframeleft,text="Nationality:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_Nationality["value"]=(' Indian',  
                          ' China', 
                          ' Australia', 
                          ' Nigeria', 
                          ' Malaysia', 
                          ' Italy', 
                          ' Turkey', 
                          ' Canada',
                          ' American')
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
       
        #idproof type Combobox
        lblIdProof=Label(labelframeleft,text="Id Proof Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)
        
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_id["value"]=("Adhar Card","Driving Licence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
        
        #id number
        lblIdNumber=Label(labelframeleft,text="Id Number:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("times new roman",13,"bold"))
        txtIdNumber.grid(row=9,column=1)
        
        #address
        lblAddress=Label(labelframeleft,text="Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        
        txtAddress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("times new roman",13,"bold"))
        txtAddress.grid(row=10,column=1)
        
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
        
        #************ Table Frame & Search System*******
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)
        
        lblSearchBy=Label(Table_frame,text="search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        
        txtsearch=ttk.Entry(Table_frame,width=29,textvariable=self.txt_search,font=("times new roman",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_frame,text="Search",command=self.Search_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnSearch.grid(row=0,column=3,padx=2)
        
        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("times new roman",11,"bold"),fg="gold",bg="black",width=10)
        btnShowAll.grid(row=0,column=4,padx=2)

        #************* Show Data Table *************8
        
        details_table=LabelFrame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                                                   "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        # Adding Scroll bar
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        #adding table & its headings into the Frame 
        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
        
        
        
        #*************Creating Database Registration *********
    def add_data(self):
        
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
                cur=conn.cursor()
                cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                          self.var_ref.get(),
                                                                          self.var_cust_name.get(),
                                                                          self.var_mother.get(),
                                                                          self.var_gender.get(),
                                                                          self.var_post.get(),
                                                                          self.var_mobile.get(),
                                                                          self.var_email.get(),
                                                                          self.var_nationality.get(),
                                                                          self.var_id_proof.get(),
                                                                          self.var_id_number.get(),
                                                                          self.var_address.get()
                                                                                      ))
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Success","Customer Has Been Added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)
     
     # Showing Data in the table on Frame which stored into the database       
    def fetch_data(self):
        
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select * from customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert('',END,values=i)
            conn.commit()
        conn.close()
        
     #Retriving Data For Use and Update into text fields 
     
    def get_cursor(self,event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
        
        
        # Update data
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            cur.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                
                                                                                                                                                                
                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_ref.get()
                                                                                                                                                      ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Has Been Updated Successfully!",parent=self.root)
    
    # Delete The Customer Details
    def Delete_data(self):
        Delete_data=messagebox.askyesno("Hotel Management System","Do You Want Delete This Customer?",parent=self.root)
        if Delete_data>0:
            
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
            cur=conn.cursor()
            query=("delete from customer where Ref=%s")
            value=(self.var_ref.get(),)
            cur.execute(query,value)
        else:
            if not Delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    # To Reset the text fields of Customer Details
    def Reset_data(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    
    # To search information of Customer
    def Search_data(self):
        conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="management",port="3306")
        cur=conn.cursor()
        cur.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cur.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
                
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
     