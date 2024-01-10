from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        img = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th.jpeg")
        img = img.resize((500, 200))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=200)

        img1 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\i2.jpg")
        img1 = img1.resize((500, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=200)

        img2 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th1.jpeg")
        img2 = img2.resize((500, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=200)
        
        img3 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th2.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # =============time============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=("times new roman", 20, "bold"), bg="white", fg="red")
        lbl.place(x=0, y=0, width=220, height=50)
        time()

        
        # student button 
        img4 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th3.jpeg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=300,width=220,height=40)

        img5 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th4.jpeg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=300,width=220,height=40)
        
        img6 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th5.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=300,width=220,height=40)

        img7 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th6.jpeg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=300,width=220,height=40)

        img8 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th7.jpg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=580,width=220,height=40)
        
        img9 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th8.jpeg")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=500,y=580,width=220,height=40)
        
        img10 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th9.jpg")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=800,y=580,width=220,height=40)
        
        img11 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th10.jpeg")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are u sure exit this Project",parent =self.root)    
        if self.iExit >0:
            self.root.destroy()
        else:
            return    
            
        # =========Functions Buttons=========
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)    

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)    

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)    

        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
