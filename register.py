from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 

        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x800+0+0")
        
       #***********variables*********
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar() 
        
        #************bg image***********
        self.bg=ImageTk.PhotoImage(file=r"C:\python\New Project\images\register_page.jpg")
        
        lbl_bg1=Label(self.root,image=self.bg)
        lbl_bg1.place(x=0,y=0,relwidth=1,relheight=1)
        
        #********main frame********
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("Microsoft Yahei UI Light",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)
        

         #********Label & Entry*****************
       
       
       #***********row1
        fname=Label(frame,text="First Name",font=("Microsoft Yahei UI Light",15,"bold"),bg="white")
        fname.place(x=50,y=100)
       
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Microsoft Yahei UI Light",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
       
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Microsoft Yahei UI Light",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #************row2
        contact=Label(frame,text="Contact No.",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Microsoft Yahei UI Light",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_email,font=("Microsoft Yahei UI Light",15))
        self.txt_contact.place(x=370,y=200,width=250)
        
        #************row3
        security_Q=Label(frame,text="Select Security Questions",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
    
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Microsoft Yahei UI Light",15))
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text="Security Answer",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("Microsoft Yahei UI Light",15))
        self.txt_security_A.place(x=370,y=270,width=250)
        
        #************row4
        pswd=Label(frame,text="Password",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Microsoft Yahei UI Light",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Microsoft Yahei UI Light",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        #**************Check Button*************
        self.var_check= IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("Microsoft Yahei UI Light",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)
        
        #*************buttons************
        img=Image.open(r"C:\python\New Project\images\button1.jpg")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1= Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        b1.place(x=10,y=420,width=200)
        
        img5=Image.open(r"C:\python\New Project\images\button.png")
        img5=img5.resize((200,55),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        b2= Button(frame,image=self.photoimage5,borderwidth=0,cursor="hand2",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        b2.place(x=370,y=420,width=200)
        
   #**************Function Declaration*****************
   
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and Conditions")
        else:
            conn=mysql.connector.connect(user="root",password="1042$Devashri",host="localhost",database="mydata",port="3306")
            cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            
            row=cur.fetchone()
            if row!= None:
                messagebox.showerror("Error","User already Exist,Please try with Another Email")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                 self.var_fname.get(),
                                                                                 self.var_lname.get(),
                                                                                 self.var_contact.get(),
                                                                                 self.var_email.get(),
                                                                                 self.var_securityQ.get(),
                                                                                 self.var_securityA.get(),
                                                                                 self.var_pass.get()
                                                                                        
                                                                                  ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")
            
        
if __name__ == "__main__":
    root =Tk()
    app =Register(root)
    root.mainloop()
    
 