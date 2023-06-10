from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from Hotel import HotelManagementSystem

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0") 
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Project\Hotel management sysytem\images\login_image.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)        
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)        
        
        img1=Image.open(r"C:\Project\Hotel management sysytem\images\img1.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="USER LOGIN",font=("open sans",20,"bold"),fg="black",bg="white")
        get_str.place(x=87,y=100)
        
           #labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=50,y=155)
        
        self.var_username=StringVar()
        self.var_pass1=StringVar()
        self.txtuser=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=50,y=225)
        
        self.txtpass=ttk.Entry(frame,textvariable=self.var_pass1,font=("times new roman",15,"bold"))
        self.txtpass.place(x=30,y=250,width=270)
        
        new_userLabel=Label(frame,text="Don't have an account?",font=("open sans",10,"bold"),fg="black",bg="white")
        new_userLabel.place(x=40,y=350)
        
        
          #******Icon Images*******
        img2=Image.open(r"C:\Project\Hotel management sysytem\images\img2.png")
        img2=img2.resize((15,15),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=640,y=330,width=15,height=15)
        
        img3=Image.open(r"C:\Project\Hotel management sysytem\images\img3.png")
        img3=img3.resize((15,15),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=640,y=400,width=15,height=15)
        
        
          #Login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="Green")
        loginbtn.place(x=30,y=310,width=270,height=35)
        
           #register button
        registerbtn=Button(frame,text="Create New One",command=self.register_window,font=("open sans",10,"bold underline"),borderwidth=0,relief=RIDGE,fg="red",bg="white",activeforeground="red",activebackground="white")
        registerbtn.place(x=192,y=349)
        
           #forgot Password button
        frgbtn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("open sans",8,"bold"),borderwidth=0,relief=RIDGE,fg="red",bg="white",activeforeground="red",activebackground="white")
        frgbtn.place(x=170,y=280,width=160)
        
         #***********or label************
        #orlabel=Label(frame,text="--------------------------------OR-------------------------------",font=("open sans",8),fg="firebrick1",bg="white")
        #orlabel.place(x=30,y=350)
        
           #************logos**********
        
        #fb_img=Image.open(r"C:\python\New Project\images\facebook.jpg")
        #fb_img=fb_img.resize((25,25),Image.ANTIALIAS)
        #self.photoimage5=ImageTk.PhotoImage(fb_img)
        #bF= Button(frame,image=self.photoimage5,borderwidth=0,cursor="hand2",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        #bF.place(x=90,y=400,width=20,height=20)
        
        #G_img=Image.open(r"C:\python\New Project\images\google.jpg")
        #G_img=G_img.resize((25,25),Image.ANTIALIAS)
        #self.photoimage6=ImageTk.PhotoImage(G_img)
        #bG= Button(frame,image=self.photoimage6,borderwidth=0,cursor="hand2",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        #bG.place(x=160,y=400,width=20,height=20)
        
        #T_img=Image.open(r"C:\python\New Project\images\twitter.png")
        #T_img=T_img.resize((25,25),Image.ANTIALIAS)
        #self.photoimage7=ImageTk.PhotoImage(T_img)
        #bT= Button(frame,image=self.photoimage7,borderwidth=0,cursor="hand2",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        #bT.place(x=230,y=400,width=20,height=20)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
           #************* Login **************
  
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
         messagebox.showerror("Error","all field required")
        else:
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="mydata",port="3306")
            my_cursor=conn.cursor()  
            my_cursor.execute("select * from register where Email=%s and Pass=%s",(
                                                                                 self.var_username.get(),
                                                                                 self.var_pass1.get()
                                                                            ))
        
        
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","InvalidUsername & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
                
            
                        
            #******************** Reset Password *************
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please Enter The Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="mydata",port="3306")
            my_cursor=conn.cursor() 
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                    messagebox.showerror("Error","Please Enter the Correct Answer",parent=self.root2 )
            else:
                query=("update register set pass=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                
                my_cursor.execute(query,value) 
                
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Info","Your password has be reset ,please login with new password",parent=self.root2)
            self.root2.destroy()
            
               #*****************forgot password Window****************
                     
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="mydata",port="3306")
            my_cursor=conn.cursor()  
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),) 
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)
            
            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forgot Password" ,font =("times new roman",20,"bold"),fg="red",bg="white",activeforeground="red",activebackground="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q=Label(self.root2,text="Select Security Questions",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
                security_Q.place(x=40,y=80)
    
                self.combo_security_Q=ttk.Combobox(self.root2,font=("Microsoft Yahei UI Light",15))
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
        
        
                security_A=Label(self.root2,text="Security Answer",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
                security_A.place(x=40,y=150)
        
                self.txt_security_A=ttk.Entry(self.root2,font=("Microsoft Yahei UI Light",15))
                self.txt_security_A.place(x=40,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
                new_password.place(x=40,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("Microsoft Yahei UI Light",15))
                self.txt_newpass.place(x=40,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("Microsoft Yahei UI Light",15,"bold"),fg="white",bg="green")
                
                btn.place(x=130 ,y=290)
                
        
            
                
                #************ Register New User Window 2 ******************
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
        self.bg=ImageTk.PhotoImage(file=r"C:\Project\Hotel management sysytem\images\register_page.jpg")
        
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
        img=Image.open(r"C:\Project\Hotel management sysytem\images\button1.jpg")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1= Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="black")
        b1.place(x=10,y=420,width=200)
        
        img5=Image.open(r"C:\Project\Hotel management sysytem\images\button.png")
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
            conn=mysql.connector.connect(user="root",password="0000",host="localhost",database="mydata",port="3306")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            
            row=my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","User already Exist,Please try with Another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
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
   main()