from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ========variables========

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        img_path = r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph1.jpg"
        img = Image.open(img_path)
        img = img.resize((1530, 710))
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1) 

        title_lbl = Label(bg_img, text="Student management system", font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title_lbl.place(relx=0.5, rely=0.1, anchor="center")

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img12 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph2.png")
        img12 = img12.resize((320, 150))
        self.photoimg12 = ImageTk.PhotoImage(img12)

        f_lbl = Label(Left_frame, image=self.photoimg12)
        f_lbl.place(x=5, y=0, width=320, height=150)

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep , font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course , font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"]=("Select Course","FE","CE","BE","DE","TE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year , font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester , font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id ,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky= W)

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name ,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky= W)

        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div , font=("times new roman", 12, "bold"), state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll ,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky= W)

        # gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender , font=("times new roman", 12, "bold"), state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob ,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky= W)

        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email ,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky= W)

        phone_label=Label(class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone ,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky= W)

        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address ,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky= W)

        # Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher ,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky= W)
        
        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        # buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=40)

        save_btn = Button(btn_frame, text="Save",command=self.add_data ,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update", command=self.Update_data , width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data , width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17,command=self.reset_data , font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)


        take_photo_btn = Button(btn_frame1, command=self.generate_dataset , text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1,column=1)


        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img13 = Image.open(r"C:\Users\prath\OneDrive\Documents\face recognition attendence system\images\ph3.jpeg")
        img13 = img13.resize((320, 150))
        self.photoimg13 = ImageTk.PhotoImage(img13)

        f_lbl = Label(Right_frame, image=self.photoimg13)
        f_lbl.place(x=5, y=0, width=320, height=150)

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="readonly",width=15)
        search_combo["values"]=("Select Semester","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky= W)

        search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","phone","roll","gender","dob","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ==========fenction declaration======    

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                           self.var_dep.get(),
                                                                                                           self.var_course.get(),
                                                                                                           self.var_year.get(),
                                                                                                           self.var_semester.get(),
                                                                                                           self.var_std_id.get(),
                                                                                                           self.var_std_name.get(),
                                                                                                           self.var_div.get(),
                                                                                                           self.var_roll.get(),
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_dob.get(),
                                                                                                           self.var_email.get(),
                                                                                                           self.var_phone.get(),
                                                                                                           self.var_address.get(),
                                                                                                           self.var_teacher.get(),
                                                                                                           self.var_radio1.get()                                                                                                                                                                
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

     # =========fetch Data==========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()    
        conn.close() 
        
    #    ========get cursor=======
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
         
    # ==========Update Function======    

    def Update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try: 
                update=messagebox.askyesno("Update","Do You want to Update this Student data", parent=self.root)    
                if update > 0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",(
                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                    self.var_semester.get(),                                                                                                                                                                                                                               
                                                                                                                                                                                                    # self.var_std_name.get(),
                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                    self.var_radio1.get(), 
                                                                                                                                                                                                    self.var_std_id.get()     
                                                                                                                                                                                                ))
                else:
                    if not update:
                        return   
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)        
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es: 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   

    # =======delete function=======
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Page Delete","Do You want to delete this Student data", parent=self.root)    
                if delete > 0:    
                    conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)        
            except Exception as es: 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

    # =======reset function=======
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # =======generate data setby Taking Photo Samples=======
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="prat1331",database="face_recognizer")   
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",(
                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                    self.var_semester.get(),                                                                                                                                                                                                                               
                                                                                                                                                                                                    # self.var_std_name.get(),
                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                    self.var_radio1.get(), 
                                                                                                                                                                                                    self.var_std_id.get()==id+1     
                                                                                                                                                                                                ))    
                conn.commit()
                self.fetch_data()                                                                                                                                                                                
                self.reset_data()
                conn.close()
                
                # ======= Load Predefined data on face frontals from opencv =========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # min. neighbour=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)    
                img_id=0
                # while True:
                #     ret,my_frame=cap.read()
                #     if face_cropped(my_frame) is not None:
                #         img_id+=1
                #         face=cv2.resize(face_cropped(my_frame),(450,450))    
                #         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                #         file_name_path="C:/Users/prath/OneDrive/Documents/face recognition attendence system/data/user."+str(id)+"."+str(img_id)+".jpg"
                #         cv2.imwrite(file_name_path)
                #         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                #         cv2.imshow("Cropped Face",face)

                #     if cv2.waitKey(1)==13 or int(img_id)==100:
                #         break
                # Inside the generate_dataset function
                while True:
                    ret, my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)
    
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "C:/Users/prath/OneDrive/Documents/face recognition attendence system/data/user." + str(id) + "." + str(img_id) + ".jpg"
        
        # Check if face is not None before writing to the file
                        if face is not None:
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()    
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es: 
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
    

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()        