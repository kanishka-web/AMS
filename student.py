
from tkinter import ttk
from tkinter import *      # star ka mtlb ki sari libraries tkinter se import ho jayngi
from PIL import Image,ImageTk  #agar hum star nahi import krte to hme ye likhne kii zroorat thi
from tkinter import messagebox
import re #re stands for regular expression
import mysql.connector
from keyboard import press
import tkinter.font as font
from tkcalendar import Calendar, DateEntry
import cv2

class login_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("STUDENT DETAILS")
        bg_img = Image.open("images/img12.jpg")
        img_resize = bg_img.resize((1200, 600), Image.ANTIALIAS)
        self.final_img = ImageTk.PhotoImage(img_resize)
        img_label = Label(self.root, image=self.final_img, bd=0)
        img_label.place(x=0, y=0)

    #=========================variables==================================#
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name = StringVar()
        self.var_std_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.photo_sample=StringVar()


    #------------------font declaration and labels----------------------------
        myfont = font.Font(family="Helvetica", size=22, weight=font.BOLD, slant=font.ITALIC)
        stu_label=Label(self.root,text="                STUDENT MANAGEMENT SYSTEM                        ",font=myfont,bg="lightgreen",fg="white")
        stu_label.place(x=0,y=0,width=1200,height=30)

#left frames
        left_frame=LabelFrame(self.root,bd=4,bg="lightgreen",text="student details")
        left_frame.place(x=140,y=60,width=420,height=480)
        left_frame_label=Label(left_frame,text='current course details',font="Algerian 12 bold",fg="green",bg="white")
        left_frame_label.place(x=0,y=0,width=420,height=30)
    #current course label frame
        curr_course_frame=LabelFrame(left_frame,bd=2,bg="lightgreen",text="current course")
        curr_course_frame.place(x=0,y=30,width="414",height="100")
    #department label
        dept_label=Label(curr_course_frame,text="Department",font=("times new roman",12,"bold"),fg="green",bg="white",padx=2)
        dept_label.grid(row=0,column=0)
    #department combo box--------------------------
        dept_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width="12",state="read only")
        dept_combo["values"]=("Select Department","CIVIL","CSE","ELECTRICAL","ELECTRONICS","IT","MECHANICAL")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=4)
    #course label
        course_label = Label(curr_course_frame, text="Course", font=("times new roman", 12, "bold"), fg="green",bg="white", padx=2)
        course_label.grid(row=0, column=2,sticky=W)
    #course combobox
        course_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), width="12", state="read only")
        course_combo["values"] = ("Select course", "AI", "ML", "AI+ML", "DS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=6,sticky=W)
    #year label
        year_label=Label(curr_course_frame,text="     Year     ",font=("times new roman", 12, "bold"),fg="green",bg="white",padx=2)
        year_label.grid(row=4,column=0,sticky=W)
    #year combobox
        year_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), width="12", state="read only")
        year_combo["values"] = ("Select year", "2018", "2019", "2020", "2021")
        year_combo.current(0)
        year_combo.grid(row=4, column=1, padx=4,pady=20, sticky=W)
    #semester label
        sem_label = Label(curr_course_frame, text="Semester", font=("times new roman", 12, "bold"), fg="green",bg="white", padx=2)
        sem_label.grid(row=4, column=2, sticky=W)
    #semester combobox
        sem_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_sem, font=("times new roman", 12, "bold"), width="12", state="read only")
        sem_combo["values"] = ("Select semester", "1", "2", "3", "4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=4, column=3, padx=4, pady=20, sticky=W)



#-------------------------------------------------------------------------------------------------

    #class student information label
        heading_label=Label(left_frame, text='Class Student Info', font="Algerian 12 bold", fg="green", bg="white")
        heading_label.place(x=0, y=135, width=420, height=30)

    #class student information labelframe
        class_stu_frame = LabelFrame(left_frame, bd=2, bg="lightgreen", text="Class Student Info")
        class_stu_frame.place(x=0, y=160, width="414", height="300")

    #student_Id label
        stu_id_label=Label(class_stu_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white",fg="green")
        stu_id_label.grid(row=0,column=0,padx=4,sticky=W)
    #student-id entry
        stuid_entry=Entry(class_stu_frame,textvariable=self.var_std_id,width=10,font=("times new roman",12,"bold"))
        stuid_entry.grid(row=0,column=1,padx=4,sticky=W)

    #class division label
        class_div_label = Label(class_stu_frame, text="Class DIV:", font=("times new roman", 12, "bold"), bg="white",fg="green")
        class_div_label.grid(row=1, column=0, padx=4,pady=4, sticky=W)
    #class division entry
        class_div_combo = ttk.Combobox(class_stu_frame,textvariable=self.var_std_div, width=7, font=("times new roman", 12, "bold"),state="read only")
        class_div_combo["values"]=("select division","N1","N2")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=4,pady=4, sticky=W)

    #gender_label
        gender_label = Label(class_stu_frame, text="Gender:",width=9, font=("times new roman", 12, "bold"), bg="white",fg="green")
        gender_label.grid(row=2, column=0, padx=4, pady=4, sticky=W)
    #gender_entry
        gender_combo = ttk.Combobox(class_stu_frame,textvariable=self.var_gender, font=("times new roman", 12, "bold"), width="7", state="read only")
        gender_combo["values"] = ( "select gender","Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=4,pady=4,sticky=W)


    #email_label
        email_label = Label(class_stu_frame, text="E-mail:",width=9, font=("times new roman", 12, "bold"), bg="white",fg="green")
        email_label.grid(row=3, column=0, padx=4, pady=4, sticky=W)
    #email_entry
        email_entry = Entry(class_stu_frame,textvariable=self.var_email, width=10, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=4, pady=4, sticky=W)

    #address_label
        add_label = Label(class_stu_frame, text="Address:",width=9, font=("times new roman", 12, "bold"), bg="white",fg="green")
        add_label.grid(row=4, column=0, padx=2, pady=4, sticky=W)
    #address_entry
        add_entry = Entry(class_stu_frame,textvariable=self.var_address, width=10, font=("times new roman", 12, "bold"))
        add_entry.grid(row=4, column=1, padx=4, pady=4, sticky=W)

    #name label
        name_label=Label(class_stu_frame,text="Name",fg="green",width=8,bg="white",font=("times new roman",12,"bold"))
        name_label.grid(row=0,column=2,padx=1,pady=4,sticky=W)
    #name entry
        name_entry=Entry(class_stu_frame,textvariable=self.var_std_name,width=9,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,sticky=W)

    #rollno_label
        rollno_label = Label(class_stu_frame, text="RollNO.", fg="green", bg="white", font=("times new roman", 12, "bold"),width=8)
        rollno_label.grid(row=1, column=2, padx=1, pady=4, sticky=W)
    # rollno_entry
        rollno_entry = Entry(class_stu_frame,textvariable=self.var_rollno, width=9, font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=3,sticky=W)

    #dob_label
        dob_label = Label(class_stu_frame, text=" DOB: ", fg="green", width=8,bg="white", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=2, padx=1, pady=4, sticky=W)
    # dob_entry
        dob_entry= DateEntry(class_stu_frame, textvariable=self.var_dob,width=9, background="magenta3", foreground="white", bd=2)
        dob_entry.grid(row=2, column=3, sticky=W)

    # phone_label
        phone_label = Label(class_stu_frame, text="Phone No:",width=8, fg="green", bg="white", font=("times new roman", 12, "bold"))
        phone_label.grid(row=3, column=2, padx=1, pady=4, sticky=W)
    # phone_entry
        phone_entry = Entry(class_stu_frame,textvariable=self.var_phone, width=9, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3,sticky=W)

    # teacher_label
        teacher_label = Label(class_stu_frame, text="Teach.name",width=8, fg="green", bg="white", font=("times new roman", 12, "bold"))
        teacher_label.grid(row=4, column=2, padx=1, pady=4, sticky=W)
    #teacher_entry
        teacher_entry = Entry(class_stu_frame,textvariable=self.var_teacher, width=9, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, sticky=W)

    #radio buttons
        self.var_radio1=StringVar()
        radio_button1=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="Have Picture",value="Yes")
        radio_button1.grid(row=7,column=0)
        radio_button2 = ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="Have No picture", value="No")
        radio_button2.grid(row=7, column=2)

    #BUTOONS FRAME
        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=405,height=80)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=10,font=("times new roman",12,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update", width=10,command=self.update_data,font=("times new roman", 12, "bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="delete", width=10,command=self.delete_data, font=("times new roman", 12, "bold"), bg="green", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="reset", width=10,command=self.reset_data,font=("times new roman", 12, "bold"), bg="green", fg="white")
        reset_btn.grid(row=0, column=3)

    #again btn_frame1
        btn_frame1 = Frame(btn_frame, bd=2, relief=RIDGE, bg="lightgreen")
        btn_frame1.place(x=0, y=30, width=405, height=48)

    #take_photo_btn
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=21,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
    #update_photo_btn
        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=21, font=("times new roman", 12, "bold"),bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

    #rightframes-----------------------------------------------------------------------------------
        right_frame = LabelFrame(self.root, bd=4, bg="lightgreen", text="student details")
        right_frame.place(x=600, y=60, width=420, height=480)
        right_frame_label = Label(right_frame, text='Search System', font="Algerian 12 bold", fg="green",bg="white")
        right_frame_label.place(x=0, y=0, width=420, height=30)
    # SEARCH SYSTEM_________________________________________________________________________
        search_frame=LabelFrame(right_frame,bd=2,bg="lightgreen",text="search system")
        search_frame.place(x=0,y=31,width=415,height=60)

    #search_label
        search_label=Label(search_frame,text="Search By:",width=8,font=("times new roman",12,"bold"),bg="white",fg="green")
        search_label.grid(row=0,column=1,sticky=W)
    #search_combo
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=12)
        search_combo['values']=('select',"roll_no","phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=2,padx=4,sticky=W)
    #search_btn
        search_btn = Button(search_frame, text="Search", width=8, font=("times new roman", 12, "bold"), bg="blue",fg="white")
        search_btn.grid(row=0, column=3)
    #showall_btn
        showall_btn=Button(search_frame,text="Show All",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

    # table_frame
        table_frame = LabelFrame(right_frame, bd=2, bg="lightgreen", relief=RIDGE, text="search system")
        table_frame.place(x=0,width=415,y=90,height=360)

    #scroll_x and scroll_y
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    #student_table
        self.student_table=ttk.Treeview(table_frame,column=('dep','course','year','sem','id','name','division','roll','gender','dob','email','phone','address','teacher','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('dep',text="Department")
        self.student_table.heading('course',text="Course")
        self.student_table.heading('year',text="Year")
        self.student_table.heading('sem',text="Semester")
        self.student_table.heading('id',text="Student-ID")
        self.student_table.heading('name',text="Name")
        self.student_table.heading('division',text="Division")
        self.student_table.heading('roll', text="RollNo")
        self.student_table.heading('gender', text="Gender")
        self.student_table.heading('dob', text="DOB")
        self.student_table.heading('email',text="E-Mail")
        self.student_table.heading('phone',text="Phone")
        self.student_table.heading('address',text="Address")
        self.student_table.heading('teacher',text="Teacher")
        self.student_table.heading('photo',text="PhotoSample status")
        self.student_table['show']='headings'

        self.student_table.column("dep", width=80)
        self.student_table.column("course", width=80)
        self.student_table.column("year", width=80)
        self.student_table.column("sem", width=80)
        self.student_table.column("id", width=80)
        self.student_table.column("name", width=80)
        self.student_table.column("division", width=80)
        self.student_table.column("roll", width=80)
        self.student_table.column("gender", width=80)
        self.student_table.column("dob", width=80)
        self.student_table.column("email", width=80)
        self.student_table.column("phone", width=80)
        self.student_table.column("address", width=80)
        self.student_table.column("teacher", width=80)
        self.student_table.column("photo", width=80)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ####################function declaration#################
    def add_data(self):
        if self.var_dept.get()=="select department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("ERROR","All fields are required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="school",port='3306')
                my_cursor=conn.cursor()

                my_cursor.execute("insert into information values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dept.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_std_div.get(),self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))
                #q = "insert into information(dep,course,year,sem,id,name,division,roll,gender,dob,email,phone,address,teacher,photo) ,values(self.var_dept.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_std_div.get(),self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))"
                  #my_cursor.execute(q)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Sucess',"student details has been updated successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)
     #fetch data in the table function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="school", port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from information")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
      #___________________get cursor function_______________________________
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_std_div.set(data[6])
        self.var_rollno.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #__________update function_____________________
    def update_data(self):
        if self.var_dept.get() == "select department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("ERROR", "All fields are required!", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update student details?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="school",port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update information set dep=%s,course=%s,year=%s,sem=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where id=%s",(self.var_dept.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_std_name.get(),self.var_std_div.get(),self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Students detail successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#DELETE FUNCTION FOR DELETE AND RESET BUTTON
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student-Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete student details?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="school",port='3306')
                    my_cursor = conn.cursor()
                    sql="delete from information where id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successfully!","Successflly deleted details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
      #RESET FUNCTION
    def reset_data(self):
        self.var_sem.set("select semester")
        self.var_dob.set("")
        self.var_std_id.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_radio1.set("")
        self.var_gender.set("select gender")
        self.var_dob.set("")
        self.var_teacher.set("")
        self.var_dept.set("select department")
        self.var_rollno.set("")
        self.var_address.set("")
        self.var_std_div.set("select division")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_std_name.set("")

    def generate_dataset(self):
        if self.var_dept.get() == "select department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("ERROR", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="school",port='3306')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from information")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update information set dep=%s,course=%s,year=%s,sem=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where id=%s",(self.var_dept.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(),self.var_std_name.get(), self.var_std_div.get(), self.var_rollno.get(),self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(),self.var_std_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
       #Load predefine data on frontal face from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                      #scaling factor=1.3
                      #minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets completed successfully !!! ")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
if __name__=='__main__':
    root=Tk()
    obj=login_page(root)
    root.mainloop()







# -__________________Generate Dataset and Take Photo Samples___________


