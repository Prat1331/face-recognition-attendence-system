from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        img17 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph1.jpg")
        img17 = img17.resize((1530, 710))
        self.photoimg17 = ImageTk.PhotoImage(img17)

        f_lbl = Label(self.root, image=self.photoimg17)
        f_lbl.place(x=0, y=0, width=1530, height=710)

        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img16 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\th11.png")
        img16 = img16.resize((1530, 325))
        self.photoimg16 = ImageTk.PhotoImage(img16)

        f_lbl = Label(self.root, image=self.photoimg16)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # button
        b1_1 = Button(self.root, text="Train Data",command=self.train_classifier , cursor="hand2", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1_1.place(x=400,y=380,width=700,height=60)

    def train_classifier(self):
        try:
           data_dir=(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\data") 
           path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

           faces=[]
           ids=[]

           for image in path:
               img=Image.open(image).convert('L')
               imageNp = np.array(img, 'uint8')
               id=int(os.path.split(image)[1].split('.')[1])

               faces.append(imageNp)
               ids.append(id)
               cv2.imshow("Training",imageNp)
               cv2.waitKey(1)==13
           ids=np.array(ids)    

    #    ===========train the classifier and save=======

           print(dir (cv2.face))
           clf = cv2.face.LBPHFaceRecognizer_create()
           clf.train(faces,ids)
           clf.write(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\classifier.xml")
           cv2.destroyAllWindows()
           messagebox.showinfo("Result","Training datasets completed!!")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()           