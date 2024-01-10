from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img23 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph9.jpg")
        img23 = img23.resize((1530, 720))
        self.photoimg23 = ImageTk.PhotoImage(img23)

        f_lbl = Label(self.root, image=self.photoimg23)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img24 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph8.jpg")
        img24 = img24.resize((200, 200))
        self.photoimg24 = ImageTk.PhotoImage(img24)

        f_lbl = Label(main_frame, image=self.photoimg24)
        f_lbl.place(x=300, y=0, width=200, height=200)

        dev_label=Label(main_frame,text="Hello My Name is Pratham",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am a full stack Developer",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=40)

        img25 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph9.jpg")
        img25 = img25.resize((500, 390))
        self.photoimg25 = ImageTk.PhotoImage(img25)

        f_lbl = Label(main_frame, image=self.photoimg25)
        f_lbl.place(x=0, y=210, width=500, height=390)



        

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()                