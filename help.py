from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img23 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph10.jpg")
        img23 = img23.resize((1530, 720))
        self.photoimg23 = ImageTk.PhotoImage(img23)

        f_lbl = Label(self.root, image=self.photoimg23)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        dev_label=Label(f_lbl,text="Email:help@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=625,y=520)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()                        