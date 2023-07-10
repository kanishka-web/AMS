from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk

from tkinter import messagebox
import re #re stands for regular expression
import mysql.connector
from keyboard import press
import tkinter.font as font
from student import login_page
from tkcalendar import Calendar, DateEntry
from attendance import att_sys
from attendance import capture_img
from attendance import chatbot_faq
import tkinter

class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("ATTENDANCE MANAGEMENT SYSTEM")
        bg_img=Image.open("images/img1.jpg")
        img_resize=bg_img.resize((1200,600),Image.ANTIALIAS)
        self.final_img=ImageTk.PhotoImage(img_resize)
        img_label=Label(self.root,image=self.final_img,bd=0)
        img_label.place(x=0,y=0)

#tkFont.Font(family="Times", size=12, weight=tkFont.BOLD)
        myfont=font.Font(family="Helvetica", size=22, weight=font.BOLD,slant=font.ITALIC)
        button_font=font.Font(family="Helvetica", size=12,weight=font.BOLD)

        head_label=Label(self.root,text="                     FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE                               ",font=myfont,bg="lightblue",fg="white")
        head_label.place(x=0,y=0)

        stu_img=Image.open("images/img2.jpg")
        stu_img_res=stu_img.resize((150,150),Image.ANTIALIAS)
        self.stu_img_fin=ImageTk.PhotoImage(stu_img_res)
        stu_detail_but=Button(self.root,image=self.stu_img_fin,command=self.student_details,cursor="hand2")
        stu_detail_but.place(x=120,y=100)
        stu_details=Button(self.root,text="STUDENT DETAILS",command=self.student_details,bg='lightblue',fg="white",font=button_font,cursor="hand2")
        stu_details.place(x=120,y=250,width=156,height=30)

        face_img=Image.open("images/img3.jpg")
        face_img_res=face_img.resize((150,150),Image.ANTIALIAS)
        self.face_img_fin=ImageTk.PhotoImage(face_img_res)
        face_detect_but=Button(self.root,image=self.face_img_fin,cursor="hand2",command=capture_img)
        face_detect_but.place(x=400,y=100)
        face_detect=Button(self.root,text="UPLOAD IMAGE",bg='lightblue',fg="white",font=button_font,cursor="hand2",command=capture_img)
        face_detect.place(x=400,y=250,width=156,height=30)

        att_img=Image.open("images/img4.jpg")
        att_img_res=att_img.resize((150,150),Image.ANTIALIAS)
        self.att_img_fin=ImageTk.PhotoImage(att_img_res)
        att_but=Button(self.root,image=self.att_img_fin,cursor="hand2",command=att_sys)
        att_but.place(x=680,y=100)
        att_text_but=Button(self.root,text="ATTENDANCE",bg='lightblue',fg="white",font=button_font,cursor="hand2",command=att_sys)
        att_text_but.place(x=680,y=250,width=156,height=30)

        help_img=Image.open("images/img5.jpg")
        help_img_res=help_img.resize((150,150),Image.ANTIALIAS)
        self.help_img_fin=ImageTk.PhotoImage(help_img_res)
        help_img_but=Button(self.root,image=self.help_img_fin,cursor="hand2",command=chatbot_faq)
        help_img_but.place(x=120,y=330)
        help_text_but=Button(self.root,text="HELP DESK",bg='lightblue',fg="white",font=button_font,cursor="hand2",command=chatbot_faq)
        help_text_but.place(x=120,y=480,width=156,height=30)


        #train_img=Image.open("images/img6.jpg")
        #train_img_res=train_img.resize((150,150),Image.ANTIALIAS)
        #self.train_img_fin=ImageTk.PhotoImage(train_img_res)
        #train_img_but=Button(self.root,image=self.train_img_fin,cursor="hand2")
        #train_img_but.place(x=120,y=300)
        #train_text_but=Button(self.root,text="TRAIN DATA",bg='lightblue',fg="white",font=button_font,cursor="hand2")
        #train_text_but.place(x=120,y=450,width=156,height=30)



        #photos_img=Image.open("images/img8.jpg")
        #photos_img_res=photos_img.resize((150,150),Image.ANTIALIAS)
        #self.photos_img_fin=ImageTk.PhotoImage(photos_img_res)
        #photos_img_but=Button(self.root,image=self.photos_img_fin,cursor="hand2")
        #photos_img_but.place(x=340,y=300)
        #photos_text_but=Button(self.root,text="PHOTOS",bg='lightblue',fg="white",font=button_font,cursor="hand2")
        #photos_text_but.place(x=340,y=450,width=156,height=30)


        #developer_img=Image.open("images/img9.jpg")
        #developer_img_res=developer_img.resize((150,150),Image.ANTIALIAS)
        #self.developer_img_fin=ImageTk.PhotoImage(developer_img_res)
        #developer_img_but=Button(self.root,image=self.developer_img_fin,cursor="hand2")
        #developer_img_but.place(x=555,y=300)
        #developer_text_but=Button(self.root,text="DEVELOPER",bg='lightblue',fg="white",font=button_font,cursor="hand2")
        #developer_text_but.place(x=555,y=450,width=156,height=30)

        exitt_img=Image.open("images/img11.jpg")
        exitt_img_res=exitt_img.resize((150,150),Image.ANTIALIAS)
        self.exitt_img_fin=ImageTk.PhotoImage(exitt_img_res)
        exitt_img_but=Button(self.root,image=self.exitt_img_fin,cursor="hand2",command=self.isExit)
        exitt_img_but.place(x=400,y=330)
        exitt_text_but=Button(self.root,text="EXIT",bg='lightblue',fg="white",font=button_font,cursor="hand2",command=self.isExit)
        exitt_text_but.place(x=400,y=480,width=156,height=30)

        #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=login_page(self.new_window)

    def isExit(self):
        self.isExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.isExit>0:
            self.root.destroy()
        else:
            return




if __name__=='__main__':
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
