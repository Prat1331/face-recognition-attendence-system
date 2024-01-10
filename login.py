from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Login")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bd=2, bg="#FFD700")
        frame.place(x=610, y=170, width=340, height=450)

        img26 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph12.jpeg")
        img26 = img26.resize((100, 100))
        self.photoimg26 = ImageTk.PhotoImage(img26)

        f_lbl = Label(image=self.photoimg26, bg="#FFD700", borderwidth=0)
        f_lbl.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="#FFD700")
        get_str.place(x=95,y=110)
        
        # label
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="#FFD700")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="#FFD700")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=255,width=270)

        # icon image
        img27 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph13.jpeg")
        img27 = img27.resize((25, 25))
        self.photoimg27 = ImageTk.PhotoImage(img27)

        f_lbl = Label(image=self.photoimg27, bg="#FFD700", borderwidth=0)
        f_lbl.place(x=650, y=323, width=25, height=25)

        img28 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph14.png")
        img28 = img28.resize((25, 25))
        self.photoimg28 = ImageTk.PhotoImage(img28)

        f_lbl = Label(image=self.photoimg28, bg="#FFD700", borderwidth=0)
        f_lbl.place(x=650, y=395, width=25, height=25)

        # Login Button
        loginbtn = Button(frame,command=self.login, text="Login",font=("times new roman", 15, "bold"),bd=3,relief=RIDGE, bg="red", fg="white",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register Button
        registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0, bg="#FFD700", fg="black")
        registerbtn.place(x=0,y=350,width=160)

        # Forgetpassbtn
        registerbtn = Button(frame, text="forget password",command=self.forgot_password_window,font=("times new roman", 10, "bold"),borderwidth=0, bg="#FFD700", fg="black")
        registerbtn.place(x=10,y=370,width=120)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")  
        elif   self.txtuser.get()=="prat" and self.txtpass.get()=="9821":
            messagebox.showinfo("success","welcome to face Recognition system")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                                 ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")    
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return    
            conn.commit()            
            conn.close()
            
    # ======================reset password=============
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question0",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Select enter the answer",parent=self.root2)    
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Select enter the new password",parent=self.root2)        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                 messagebox.showerror("Error","Please enter correct answer",parent=self.root2)        
            else:
                 query=("update register set password=%s where email=%s")
                 value=(self.txt_newpass.get(),self.txtuser.get())
                 my_cursor.execute(query,value)

                 conn.commit()            
                 conn.close()
                 messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)        
                 self.root2.destroy()
            
            
                
                
               
    # ======================forgot password============
    def forgot_password_window(self):
        if self.txtuser.get()=="":
             messagebox.showerror("Error","Please write the Email address to reset password")        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            if row == None:
                 messagebox.showerror("Error","Please enter the valid username")        
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")    

                l=Label(self.root2,text="Forget Password",font=("times new roman", 10, "bold"),borderwidth=0, bg="white", fg="red")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2, text=" Select Security Questions", font=("times new roman",15,"bold"),bg="white", fg="black") 
                security_Q.place(x=50,y=80)
        
                self.combo_securiy_Q = ttk.Combobox(self.root2, font=("times new roman", 12, "bold"), state="readonly",width=15)
                self.combo_securiy_Q["values"]=("Select ","Your Birth Place","Your Girlfriend name","Your Pet name")
                self.combo_securiy_Q.place(x=50,y=110, width=250) 
                self.combo_securiy_Q.current(0)

                security_A=Label(self.root2, text="Security Answer", font=("times new roman",15,"bold"),bg="white", fg="black") 
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2, font=("times new roman",15)) 
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2, text="New Password", font=("times new roman",15,"bold"),bg="white", fg="black") 
                new_password.place(x=50,y=150)

                self.txt_newpass=ttk.Entry(self.root2, font=("times new roman",15)) 
                self.txt_newpass.place(x=50,y=250,width=250)

                btn = Button(self.root2,text="Reset",font=("times new roman", 15, "bold"), bg="green", fg="white")
                btn.place(width=100,height=290)

                


class Register:   
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Register")
        
        # ==========variables===========
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        # ==========bg image===========
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph16.jpeg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =============left image============
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph1.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ============main frame==============
        frame = Frame(self.root, bd=2, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl=Label(frame, text="REGISTER HERE", font=("times new roman",20,"bold"), fg="red",bg="white") 
        register_lbl.place(x=50,y=20)

        # ===============label and entry=======

        # --row1

        fname=Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white") 
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold")) 
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15)) 
        self.txt_lname.place(x=370,y=130,width=250)

        # -------------row2

        contact=Label(frame, text="Contact No", font=("times new roman", 15, "bold"),bg="white", fg="black") 
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame, text="Email", font=("times new roman", 15, "bold"),bg="white", fg="black") 
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #  ---------row3
        security_Q=Label(frame, text=" Select Security Questions", font=("times new roman",15,"bold"),bg="white", fg="black") 
        security_Q.place(x=50,y=240)
        
        self.combo_securiy_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 12, "bold"), state="readonly",width=15)
        self.combo_securiy_Q["values"]=("Select ","Your Birth Place","Your Girlfriend name","Your Pet name")
        self.combo_securiy_Q.place(x=50,y=270, width=250) 
        self.combo_securiy_Q.current(0)

        security_A=Label(frame, text="Security Answer", font=("times new roman",15,"bold"),bg="white", fg="black") 
        security_A.place(x=370,y=248)

        self.txt_security=ttk.Entry(frame ,textvariable=self.var_securityA, font=("times new roman",15)) 
        self.txt_security.place(x=370,y=270,width=250)

        # --row4

        pswd=Label(frame, text="Password ",font=("times new roman",15, "bold"), bg="white", fg="black") 
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman",15)) 
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ======checkbutton===========

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"),onvalue=1,offvalue=0) 
        self.checkbtn.place(x=50,y=380)

        # ========buttons=======

        img=Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph17.jpeg")
        img=img.resize((100,70))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data, borderwidth=0,cursor="hand2", font=("times new roman", 15, "bold"),fg="white")
        b1.place(x=50,y=420,width=140)
        
        img1=Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph18.png")
        img1=img1.resize((200,70))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2", font=("times new roman", 15, "bold"),fg="white")
        b1.place(x=370,y=420,width=220)
        
        # =========function declaration===========
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Plaese agree our terms ane condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                 messagebox.showerror("Error", "user already exist please try another email")
            else:
                 my_cursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)",(
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
            messagebox.showinfo("Success"," Register Successfully")
        

if __name__ == "__main__":
    main()
