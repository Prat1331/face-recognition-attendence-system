from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img18 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph4.png")
        img18 = img18.resize((650, 700))
        self.photoimg18 = ImageTk.PhotoImage(img18)

        f_lbl = Label(self.root, image=self.photoimg18)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img19 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph5.png")
        img19 = img19.resize((950, 700))
        self.photoimg19 = ImageTk.PhotoImage(img19)

        f_lbl = Label(self.root, image=self.photoimg19)
        f_lbl.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2",command=self.face_recog, font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=340,y=600,width=300,height=60)

        # ==========Attendence===========

    def mark_attendence(self,i,r,n,d):
        with open("Pratham.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                    

        # ==========face Recognition=======
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,mineNeighbors,color,text,clf):    
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,mineNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:    
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]    
            
            return coord    

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)    
            return img

        faceCascade=cv2.CascadeClassifier(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\haarcascade_frontalface_default.xml")    
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()    
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()  