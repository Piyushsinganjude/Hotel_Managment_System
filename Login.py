from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox



class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0") 
        
        self.bg=ImageTk.PhotoImage(file=r"C:\python\New Project\images\login_image.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)        
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)        
        
        img1=Image.open(r"C:\python\New Project\images\img1.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("Microsoft Yahei UI Light",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)
        
        #labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #******Icon Images*******
        img2=Image.open(r"C:\python\New Project\images\img2.png")
        img2=img2.resize((15,15),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=660,y=330,width=15,height=15)
        
        img3=Image.open(r"C:\python\New Project\images\img3.png")
        img3=img3.resize((15,15),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=660,y=400,width=15,height=15)
        
        #Login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="Green")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #register button
        registerbtn=Button(frame,text="New User Register",font=("open sans",12,"bold"),borderwidth=0,relief=RIDGE,fg="red",bg="white",activeforeground="red",activebackground="white")
        registerbtn.place(x=10,y=380,width=160)
        
        #forgot Password button
        frgbtn=Button(frame,text="Forgot Password",font=("open sans",12,"bold"),borderwidth=0,relief=RIDGE,fg="red",bg="white",activeforeground="red",activebackground="white")
        frgbtn.place(x=170,y=380,width=160)
        
        #***********or label************
        orlabel=Label(frame,text="---------------------OR---------------------",font=("open sans",8),fg="firebrick1",bg="white")
        orlabel.place(x=76,y=350)
        
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
        
         
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
         messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome")
        else:
            messagebox.showerror("Invalid","Invalid Ussername & Password")
        
        
       

        
        
if __name__ == "__main__":
    root =Tk()
    app =login_window(root)
    root.mainloop()
    
 