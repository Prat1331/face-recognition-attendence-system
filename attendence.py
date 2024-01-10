from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ============variables===========
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()

        img19 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph7.png")
        img19 = img19.resize((600, 200))
        self.photoimg19 = ImageTk.PhotoImage(img19)

        f_lbl = Label(self.root, image=self.photoimg19)
        f_lbl.place(x=0, y=0, width=800, height=200)

        img20 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph6.jpeg")
        img20 = img20.resize((600, 200))
        self.photoimg20 = ImageTk.PhotoImage(img20)

        f_lbl = Label(self.root, image=self.photoimg20)
        f_lbl.place(x=800, y=0, width=600, height=200)
        
        # ====bg image=======

        img21 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph1.jpg")
        img21 = img21.resize((1530, 710))
        self.photoimg21 = ImageTk.PhotoImage(img21)

        bg_img = Label(self.root, image=self.photoimg21)
        bg_img.place(x=0, y=200, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="Attendance Management System", font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530,height=52)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=580)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=480)

        img22 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph2.png")
        img22 = img22.resize((320, 150))
        self.photoimg22 = ImageTk.PhotoImage(img22)

        f_lbl = Label(Left_frame, image=self.photoimg22)
        f_lbl.place(x=5, y=0, width=320, height=150)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        # Labeled entry
        # attendence id
        AttendenceId=Label(left_inside_frame,text="AttendenceID:",font=("times new roman",12,"bold"),bg="white")
        AttendenceId.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendenceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        AttendenceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky= W)

        # Name
        rollLabel=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky= W)

        # date
        nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_name_entry.grid(row=1,column=1,padx=10,pady=5,sticky= W)
        
        # Department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky= W)

        # time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time_entry.grid(row=2,column=1,padx=10,pady=5,sticky= W)

        # Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        atten_date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date_entry.grid(row=2,column=3,padx=10,pady=5,sticky= W)

        # attendence
        attendenceId=Label(left_inside_frame,text="Attendence Status:",font=("times new roman",12,"bold"),bg="white")
        attendenceId.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendence, font=("times new roman", 12, "bold"), state="readonly",width=18)
        self.atten_status["values"]=("status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=280,width=715,height=40)

        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data ,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)

        # Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=480)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        # =========== scroll bar table========== 

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # =========fetch data=========
        
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    
    # ======== import csv
    def importCsv(self): 
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 
            
    # =========Export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)   
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)    
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")    
        except Exception as es: 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
               
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()       
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")
    
if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop() 
