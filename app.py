from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkcalendar import Calendar, DateEntry
from datetime import date



class App:
    def __init__(self):
        setUpGui()


def setUpGui():
    #Setting root window:
    root = Tk()
    root.geometry("400x600+450+50")
    root.resizable(False, False)
    root.title('DIU Appointment Management System')
    root.iconbitmap("./assets/diuLogo.png")
    favicon = PhotoImage(file="./assets/diuLogo.png")
    root.iconphoto(False, favicon)

    # used fonts
    helvitika = font.Font(family='Helvetica', size=16)

    # Welcome Screen Code:
    firstFrame = Frame(root, width=400, height=600)
    firstFrame.place(x=0, y=0)

    # Adding DIU logo  in first frame
    diuImg = ImageTk.PhotoImage(Image.open("./assets/diuLogo.png"))
    diuImgLable = Label(firstFrame, image=diuImg)
    diuImgLable.place(x=150, y=50)

    # Adding buttons and text in first frame
    teacherBtn = Button(firstFrame, text="Teacher", padx=8, pady=5, bg='green', fg='#0052cc', font=helvitika)
    teacherBtn.place(x=150, y=250)
    orLabel = Label(firstFrame, text="OR", fg='red', font=helvitika)
    orLabel.place(x=185, y=310)
    studentBtn = Button(firstFrame, text="Student", padx=8, pady=5, bg='#0052cc', fg='green', font=helvitika)
    studentBtn.place(x=150, y=350)

    #Student Login Frame Code
    studentLoginFrame = Frame(root, width=400, height=600)
    studentLoginFrame.place(x=0, y=0)

    # Adding input area, lables & button
    studentIdInputLable = Label(studentLoginFrame, text="Your Student id:", fg='black', font=helvitika)
    studentIdInputLable.place(x=50, y=120)

    studentIdInput = Entry(studentLoginFrame,font=helvitika)
    studentIdInput.place(x=50, y=150, width=300, height=30)

    sectionInputLable = Label(studentLoginFrame, text="Section:", font=helvitika)
    sectionInputLable.place(x=50, y=190)

    sectionInput = Entry(studentLoginFrame,font=helvitika)
    sectionInput.place(x=50, y=220, width=300, height=30)

    departmentInputLable = Label(studentLoginFrame,text="Department:",font=helvitika)
    departmentInputLable.place(x=50,y=260)

    departmentInput = Entry(studentLoginFrame,font=helvitika)
    departmentInput.place(x=50, y=290, width=300, height=30)

    studentLoginButton = Button(studentLoginFrame,text="Login",bg='#0052cc',fg='white',font=helvitika)
    studentLoginButton.place(x=100,y=400,width=200,height=40)

    #Teacher Login frame code:
    teacherLoginFrame = Frame(root, width=400, height=600)
    teacherLoginFrame.place(x=0, y=0)

    # Adding input area, lables & button
    teacherIdInputLable = Label(teacherLoginFrame, text="Your Employee id:", fg='black', font=helvitika)
    teacherIdInputLable.place(x=50, y=120)

    teacherIdInput = Entry(teacherLoginFrame, font=helvitika)
    teacherIdInput.place(x=50, y=150, width=300, height=30)

    departmentInputLable = Label(teacherLoginFrame, text="Department:", font=helvitika)
    departmentInputLable.place(x=50, y=190)

    departmentInput = Entry(teacherLoginFrame, font=helvitika)
    departmentInput.place(x=50, y=220, width=300, height=30)

    teacherLoginButton = Button(teacherLoginFrame, text="Login", bg='#0052cc', fg='white', font=helvitika)
    teacherLoginButton.place(x=100, y=300, width=200, height=40)

    # Teacher's Bookings frame code:
    teacherBookingsFrame = Frame(root, width=400, height=600)
    teacherBookingsFrame.place(x=0, y=0)

    # Adding labels & buttons in Teachers Bookings frame :
    teacherBookingsFrameLabel = Label(teacherBookingsFrame,text="Teacher Appointments",fg="#2e86de",font=helvitika)
    teacherBookingsFrameLabel.place(x=95,y=50)

    currentBookingBtn = Button(teacherBookingsFrame,text="Current Bookings",bg="#192a56",fg="#f5f6fa",font=helvitika)
    currentBookingBtn.place(x=100, y=150, width=200, height=40)

    upComingBtn = Button(teacherBookingsFrame,text="Up Coming",bg="#ee5253",fg='#f5f6fa',font=helvitika)
    upComingBtn.place(x=100, y=230, width=200, height=40)

    previousBookingBtn = Button(teacherBookingsFrame,text="Previous Bookings",bg="#222f3e",fg="#f5f6fa",font=helvitika)
    previousBookingBtn.place(x=100, y=310, width=200, height=40)

    #Adding Students Booking Frame code:
    studentBookingFrame = Frame(root, width=400, height=600)
    studentBookingFrame.place(x=0, y=0)

    #Adding Labels & buttons in Students Booking Frame :
    studentBookingsFrameLabel = Label(studentBookingFrame,text="Students Appointment Booking",fg='#2ecc71',font=helvitika)
    studentBookingsFrameLabel.place(x=60,y=50)

    # Adding labels & buttons in Teachers Bookings frame :
    studentBooingBtn = Button(studentBookingFrame, text="Book An Appointment", bg='#2ecc71', fg='#f5f6fa',
                              font=helvitika)
    studentBooingBtn.place(x=90, y=150, width=220, height=40)

    viewBookingBtn = Button(studentBookingFrame,text="View your bookings",bg="#e74c3c",fg="#f5f6fa",font=helvitika)
    viewBookingBtn.place(x=90, y=220, width=220, height=40)

    #Teacher Appontments Frame code:
    teacherAppointmentFrame = Frame(root, width=400, height=600)
    teacherAppointmentFrame.place(x=0, y=0)

    teacherAppointmentFrameLabel = Label(teacherAppointmentFrame,text="Your Appointments",fg="#e74c3c",font=helvitika)
    teacherAppointmentFrameLabel.place(x=110,y=50)

    #Student Book Appointments Frame code:
    studentBookAppointmentFrame = Frame(root, width=400, height=600)
    studentBookAppointmentFrame.place(x=0, y=0)

    #Adding label , button , input feilds in Student Book Appointments Frame
    facultytIdLabel = Label(studentBookAppointmentFrame,text="Faculty ID :",font=helvitika)
    facultytIdLabel.place(x=50,y=100)

    facultytIdInput = Entry(studentBookAppointmentFrame,font=helvitika)
    facultytIdInput.place(x=50, y=140, width=300, height=30)

    appointmentDateLabel = Label(studentBookAppointmentFrame,text="Date :",font=helvitika)
    appointmentDateLabel.place(x=50,y=200)

    appointmentDatePicker = DateEntry(studentBookAppointmentFrame,selectmode='day')
    appointmentDatePicker.place(x=50, y=240, width=300, height=30)

    timePickerLable = Label(studentBookAppointmentFrame,text="Pick a Time from 9.00 to 19.00",font=helvitika)
    timePickerLable.place(x=50,y=300)

    timePickerInput = Entry(studentBookAppointmentFrame,font=helvitika)
    timePickerInput.place(x=50, y=340, width=300, height=30)

    submitBtn = Button(studentBookAppointmentFrame,text="Book",bg="#2ecc71",fg="#ffffff",font=helvitika)
    submitBtn.place(x=100, y=400, width=220, height=40)

    root.mainloop()
