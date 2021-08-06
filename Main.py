from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import MySQLdb


#Code For Main Window :
def open_window():
    def insertdata():
        if name.get() =="" or year.get() =="" or stream.get() =="":
            messagebox.showerror("Error","Please Filled All Mantory Fields ",parent=top)
        else:
            db=MySQLdb.connect("localhost","root","","school")
            cursor=db.cursor()
            sql="INSERT INTO student VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name.get(),year.get(),stream.get(),number.get(),sub1.get(),sub2.get(),sub3.get(),marks.get(),percent.get())
            cursor.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo(top,"Data Entry Successful",parent=top)
    #Clear All fields after clicked save button
        name.set("")
        year.set("")
        stream.set("")
        number.set("")
        sub1.set("")
        sub2.set("")
        sub3.set("")
        marks.set("")
        percent.set("")
    #Main Window starting from here :
    top=Toplevel()
    top.geometry("1366x697+-8+0")  # Set size of the window
    top.minsize(1366, 697)  # Set Minimun Size of window
    top.maxsize(1366, 697)  # set maximum size of window
    top.title("SCHOOL MANAGEMENT SYSTEM....(INSERT DATA)")  # title of the project
    top.configure(bg="#17202A")  # change tkinter window color using cunfigure fun

    # Creating variables for accesing all entry boxes :
    name = StringVar()
    year = StringVar()
    stream = StringVar()
    number = StringVar()
    sub1 = StringVar()
    sub2 = StringVar()
    sub3 = StringVar()
    marks = StringVar()
    percent = StringVar()

    # Panel for Project name :
    panel=PanedWindow(top,orient="horizontal", height=70, width=1363, bg="#E5E4E2").place(x=0,y=20)
    # label for Project Name :p
    label = Label(top,panel, text="SCHOOL MANAGEMENT SYSTEM", fg="#17202A", bg="#E5E4E2", font=("Century", 28, "bold"))
    label.place(x=350, y=25)

    # insert Frame :
    frame = Frame(top,bg="palegoldenrod", height=500, width=800,relief=RIDGE,bd=5).place(x=270, y=140)

    # for Student Name :
    labname = Label(top,frame, text="Student Name", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360,y=160)
    entname= Entry(top,frame,width=25, font=("Cambria", 16), bg="#98AFC7", fg="black",textvariable=name).place(x=660, y=160)

    # Label and  entry box for Year
    labyear = Label(top,frame, text="Year", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360, y=210)
    entyear = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=year).place(x=660, y=210)

    # Label and entry box for Stream
    labstream = Label(top,frame, text="Stream", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360, y=260)
    entstream = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=stream).place(x=660, y=260)

    # Label and entry box for Phone Number :
    labnumber = Label(top,frame, text="Phone Number", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360,
                                                                                                                y=310)
    entnumber = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=number).place(x=660, y=310)

    # For Subjects 1:
    labsub1 = Label(top,frame, text="Subject-1", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360, y=360)
    entsub1 = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=sub1).place(x=660, y=360)
    # For Subject 2 :
    labsub2 = Label(top,frame, text="Subject-2", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360, y=410)
    entsub2 = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=sub2).place(x=660, y=410)
    # For Subject 3 :
    labsub3 = Label(top,frame, text="Subject-3", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360, y=460)
    entsub3 = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=sub3).place(x=660, y=460)

    # For Marks :
    labmarks = Label(top,frame, text="Marks", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360, y=510)
    entmarks = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=marks).place(x=660, y=510)

    # For Percentage :
    labpercent = Label(top,frame, text="Percentage", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=360,
                                                                                                               y=560)
    entpercent = Entry(top,frame, width=25, font=("Cambria", 16), bg="#98AFC7",textvariable=percent).place(x=660, y=560)

    # For Submit Button :
    buttonsave = Button(top,frame, width=20, text="   Submit  ---->", font=("Cambria", 15), bg="#4CC417", fg="black",command=insertdata).place(x=580, y=620)

    # Design on frame :
    paneldesign = PanedWindow(top,orient='vertical', height=260, width=20, bg="#E67E22").place(x=259, y=140)
    paneldesign2 = PanedWindow(top,orient='vertical', height=260, width=20, bg="#E67E22").place(x=1059, y=381)

    # school name Label :
    labschoolname = Label(top,text="Dr. Kakasaheb Purnapatre Madhyamik Vidyalay,Chalisgaon", font=("Rapier", 9, "italic"),
                      bg="#17202A", fg="white").place(x=1030, y=-1)

    # lower line and upper two lines:
    paneldesign3 = PanedWindow(top,orient='horizontal', height=5, width=1390, bg="#E67E22").place(x=0, y=694)
    # Upper lines :

    paneldesign4 = PanedWindow(top,orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=0, y=20)
    paneldesign5 = PanedWindow(top,orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=334, y=87)
#********************************************************************************************************************

### For Display:
def display_data():
    def display():
        db=MySQLdb.connect("localhost","root","","school")
        cursor=db.cursor()
        sql="SELECT * FROM student "
        cursor.execute(sql)
        list0 = cursor.fetchall()
        db.close()
        output=" "
        for i in list0:
            output= output+i[0]+'       '+str(i[1])+'       '+i[2]+'       '+str(i[3])+'       '+i[4]+'       '+i[5]+'       '+i[6]+'           '+str(i[7])+'       '+str(i[8])+'       '+'\n'  + '\n'
        return output

    disp = Toplevel()
    disp.geometry("1366x697+-8+0")  # Set size of the window
    disp.minsize(1366, 697)  # Set Minimun Size of window
    disp.maxsize(1366, 697)  # set maximum size of window
    disp.title("SCHOOL MANAGEMENT SYSTEM....(DISPLAY DATA)")  # title of the project
    disp.configure(bg="#17202A")  # change tkinter window color using cunfigure fun

    # Panel for Project name :
    panel = PanedWindow(disp, orient="horizontal", height=70, width=1363, bg="#E5E4E2").place(x=0, y=20)
    # label for Project Name :
    label = Label(disp, panel, text="SCHOOL MANAGEMENT SYSTEM", fg="#17202A", bg="#E5E4E2",
                      font=("Century", 28, "bold"))
    label.place(x=350, y=25)

    # insert Frame :
    frame = Frame(disp, bg="palegoldenrod", height=530, width=1050, relief=RIDGE, bd=5).place(x=150, y=140)

    # creating text box for display datap:
    text = Text(disp, frame, height=27, width=121)
    text.place(x=190, y=160)

    # For Display Button :
    buttonDisplay = Button(disp, frame, width=20, text="Display", font=("Cambria", 15), bg="#4CC417",
                            fg="black",command=lambda: text.insert(END, display())).place(x=550, y=640)

    # Design on frame :
    paneldesign = PanedWindow(disp, orient='vertical', height=260, width=20, bg="#E67E22").place(x=143, y=140)
    paneldesign2 = PanedWindow(disp, orient='vertical', height=260, width=20, bg="#E67E22").place(x=1188, y=381)

    # school name Label :
    labschoolname = Label(disp, text="Dr. Kakasaheb Purnapatre Madhyamik Vidyalay,Chalisgaon",
                              font=("Rapier", 9, "italic"),
                              bg="#17202A", fg="white").place(x=1030, y=-1)

    # lower line and upper two lines:
    paneldesign3 = PanedWindow(disp, orient='horizontal', height=5, width=1390, bg="#E67E22").place(x=0, y=694)
    # Upper lines :

    paneldesign4 = PanedWindow(disp, orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=0, y=20)
    paneldesign5 = PanedWindow(disp, orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=334, y=87)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def update():
    def updatedata():
        if name.get() =="" or year.get() =="" or stream.get() =="":
            messagebox.showerror("Error","Please Filled All Mantory Fields ",parent=updt)
        else:
            db=MySQLdb.connect("localhost","root","","school")
            cursor=db.cursor()
            sql="UPDATE student SET name=%s"
            cursor.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo(updt,"Data Updated Successful",parent=updt)



    updt = Toplevel()
    updt.geometry("1366x697+-8+0")  # Set size of the window
    updt.minsize(1366, 697)  # Set Minimun Size of window
    updt.maxsize(1366, 697)  # set maximum size of window
    updt.title("SCHOOL MANAGEMENT SYSTEM....(UPDATE DATA)")  # title of the project
    updt.configure(bg="#17202A")  # change tkinter window color using cunfigure fun

    # Creating variables for accesing all entry boxes :
    name = StringVar()
    year = StringVar()
    stream = StringVar()
    number = StringVar()
    sub1 = StringVar()
    sub2 = StringVar()
    sub3 = StringVar()
    marks = StringVar()
    percent = StringVar()

    # Panel for Project name :
    panel = PanedWindow(updt, orient="horizontal", height=70, width=1363, bg="#E5E4E2").place(x=0, y=20)
    # label for Project Name :
    label = Label(updt, panel, text="SCHOOL MANAGEMENT SYSTEM", fg="#17202A", bg="#E5E4E2", font=("Century", 28, "bold"))
    label.place(x=350, y=25)

    # insert Frame :
    frame = Frame(updt, bg="palegoldenrod", height=290, width=1300, relief=RIDGE, bd=5).place(x=20, y=100)
    frame2=Frame(updt,height=280,width=1300,relief= RIDGE,bd=6).place(x=20,y=400)

    # for Student Name :
    labname = Label(updt, frame, text="Student Name", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(
        x=100, y=120)
    entname = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", fg="black", textvariable=name).place(
        x=310, y=120)

    # Label and  entry box for Year
    labyear = Label(updt, frame, text="Year", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=750, y=120)
    entyear = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=year).place(x=950, y=120)

    # Label and entry box for Stream
    labstream = Label(updt, frame, text="Stream", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=100,
                                                                                                               y=170)
    entstream = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=stream).place(x=310, y=170)

    # Label and entry box for Phone Number :
    labnumber = Label(updt, frame, text="Phone Number", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(
        x=750,
        y=170)
    entnumber = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=number).place(x=950, y=170)

    # For Subjects 1:
    labsub1 = Label(updt, frame, text="Subject-1", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=100,
                                                                                                                y=220)
    entsub1 = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=sub1).place(x=310, y=220)
    # For Subject 2 :
    labsub2 = Label(updt, frame, text="Subject-2", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=750,
                                                                                                                y=220)
    entsub2 = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=sub2).place(x=950, y=220)
    # For Subject 3 :
    labsub3 = Label(updt, frame, text="Subject-3", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=100,
                                                                                                                y=270)
    entsub3 = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=sub3).place(x=310, y=270)

    # For Marks :
    labmarks = Label(updt, frame, text="Marks", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(x=750,
                                                                                                             y=270)
    entmarks = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=marks).place(x=950, y=270)

    # For Percentage :
    labpercent = Label(updt, frame, text="Percentage", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(
        x=100,
        y=320)
    entpercent = Entry(updt, frame, width=25, font=("Cambria", 16), bg="#98AFC7", textvariable=percent).place(x=310,
                                                                                                             y=320)

    # For Update Button :
    buttonupdate = Button(updt, frame, width=20, text=" Update", font=("Cambria", 15), bg="#4CC417", fg="black",
                        command="").place(x=750, y=320)

    # For Scroll Bar :
    scroll_y=Scrollbar(updt,frame2,orient=VERTICAL)
    records=ttk.Treeview(frame2,height=12,columns=("FIRST_NAME","YEAR","STREAM","PHONE_NUMBER","SUBJECT_1","SUBJECT_2","SUBJECT_3","MARKS","PERCENTAGE"),yscrollcommand=scroll_y.set)
    scroll_y.pack(side=BOTTOM, fill=Y)
    records.heading("FIRST_NAME",text="First_Name")
    records.heading("YEAR",text="Year")
    records.heading("STREAM",text="Stream")
    records.heading("PHONE_NUMBER",text="Phone_Number")
    records.heading("SUBJECT_1",text="Subject-1")
    records.heading("SUBJECT_2",text="Subject-2")
    records.heading("SUBJECT_3",text="Subject-3")
    records.heading("MARKS",text="Marks")
    records.heading("PERCENTAGE",text="Percentage")

    records['show']='headings'

    records.column("FIRST_NAME",width=50)
    records.column("YEAR", width=50)
    records.column("STREAM", width=50)
    records.column("PHONE_NUMBER", width=50)
    records.column("SUBJECT_1", width=50)
    records.column("SUBJECT_2", width=50)
    records.column("SUBJECT_3", width=50)
    records.column("MARKS", width=50)
    records.column("PERCENTAGE", width=50)
    records.pack(fill = BOTH, expand=1)

    # Design on frame :
    paneldesign = PanedWindow(updt, orient='vertical', height=260, width=20, bg="#E67E22").place(x=13, y=100)
    paneldesign2 = PanedWindow(updt, orient='vertical', height=260, width=20, bg="#E67E22").place(x=1338, y=430)

    # school name Label :
    labschoolname = Label(updt, text="Dr. Kakasaheb Purnapatre Madhyamik Vidyalay,Chalisgaon",
                          font=("Rapier", 9, "italic"),
                          bg="#17202A", fg="white").place(x=1030, y=-1)

    # lower line and upper two lines:
    paneldesign3 = PanedWindow(updt, orient='horizontal', height=5, width=1390, bg="#E67E22").place(x=0, y=694)
    # Upper lines :

    paneldesign4 = PanedWindow(updt, orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=0, y=20)
    paneldesign5 = PanedWindow(updt, orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=334, y=87)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def delete():
    def deldata():
        db=MySQLdb.connect("localhost","root","","school")
        cursor=db.cursor()
        sql="DELETE FROM student WHERE STUDENT_NAME=%s"%(name.get())
        cursor.execute(sql)
        db.commit()
        db.close()

    topdel = Toplevel()
    topdel.geometry("1366x697+-8+0")  # Set size of the window
    topdel.minsize(1366, 697)  # Set Minimun Size of window
    topdel.maxsize(1366, 697)  # set maximum size of window
    topdel.title("SCHOOL MANAGEMENT SYSTEM....(INSERT DATA)")  # title of the project
    topdel.configure(bg="#17202A")  # change tkinter window color using cunfigure fun

    # Creating variables for accesing all entry boxes :
    name = StringVar()

    # Panel for Project name :
    panel = PanedWindow(topdel, orient="horizontal", height=70, width=1363, bg="#E5E4E2").place(x=0, y=20)
    # label for Project Name :p
    label = Label(topdel, panel, text="SCHOOL MANAGEMENT SYSTEM", fg="#17202A", bg="#E5E4E2", font=("Century", 28, "bold"))
    label.place(x=350, y=25)

    # insert Frame :
    frame = Frame(topdel, bg="palegoldenrod", height=500, width=800, relief=RIDGE, bd=5).place(x=270, y=140)

    # for Student Name :
    labname = Label(topdel, frame, text="Student Name", font=("Cambria", 18), bg="palegoldenrod", fg="#17202A").place(
        x=360, y=160)
    entname = Entry(topdel, frame, width=25, font=("Cambria", 16), bg="#98AFC7", fg="black", textvariable=name).place(
        x=660, y=160)


    # For Delete Button :
    buttonsave = Button(topdel, frame, width=20, text=" Delete ", font=("Cambria", 15), bg="#4CC417", fg="black",
                        command=deldata).place(x=580, y=620)

    # Design on frame :
    paneldesign = PanedWindow(topdel, orient='vertical', height=260, width=20, bg="#E67E22").place(x=259, y=140)
    paneldesign2 = PanedWindow(topdel, orient='vertical', height=260, width=20, bg="#E67E22").place(x=1059, y=381)

    # school name Label :
    labschoolname = Label(topdel, text="Dr. Kakasaheb Purnapatre Madhyamik Vidyalay,Chalisgaon",
                          font=("Rapier", 9, "italic"),
                          bg="#17202A", fg="white").place(x=1030, y=-1)

    # lower line and upper two lines:
    paneldesign3 = PanedWindow(topdel, orient='horizontal', height=5, width=1390, bg="#E67E22").place(x=0, y=694)
    # Upper lines :

    paneldesign4 = PanedWindow(topdel, orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=0, y=20)
    paneldesign5 = PanedWindow(topdel, orient='horizontal', height=3, width=1030, bg="#E67E22").place(x=334, y=87)



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Code For Menu Window :-
root=Tk()
root.geometry("1366x650+-8+0")           # Set size of the window
root.minsize(1366,697)                   # Set Minimun Size of window
root.maxsize(1366,697)                   # set maximum size of window
root.title("MENU")                          # title of the project
root.configure(bg="#17202A")                # change tkinter window color using cunfigure fun

#Panel for Project name :
panel=PanedWindow(root,orient="horizontal",height=70,width=1363,bg="#E5E4E2").place(x=0,y=20)

#insert Frame :
frame=Frame(root,bg="palegoldenrod",height=500,width=800,bd=5,relief=RIDGE).place(x=270,y=140)

# For insert Data Button :
labinsert=Label(root,frame,text="For Insert Data",font=("Cambria",18),bg="palegoldenrod",fg="#17202A").place(x=430,y=240)
buttoninsert=Button(root,frame,width=20,text=" Click Here",font=("Cambria",15),bg="#4CC417",fg="black",command=open_window)
buttoninsert.place(x=650,y=240)

# For Display Data Button :
labdisplay=Label(root,frame,text="For Display Data",font=("Cambria",18),bg="palegoldenrod",fg="#17202A").place(x=430,y=300)
buttondisplay=Button(root,frame,width=20,text=" Click Here",font=("Cambria",15),bg="#808B96",fg="black",command=display_data)
buttondisplay.place(x=650,y=300)

# For Update Data Button :
labupdate=Label(root,frame,text="For Update Data",font=("Cambria",18),bg="palegoldenrod",fg="#17202A").place(x=430,y=360)
buttonupdate=Button(root,frame,width=20,text=" Click Here",font=("Cambria",15),bg="#EC7063",fg="black",command=update)
buttonupdate.place(x=650,y=360)

# For Delete Data Button :
labdelete=Label(root,frame,text="For Delete Data",font=("Cambria",18),bg="palegoldenrod",fg="#17202A").place(x=430,y=420)
buttondelete=Button(root,frame,width=20,text=" Click Here",font=("Cambria",15),bg="red",fg="White",command=delete)
buttondelete.place(x=650,y=420)


#label for Project Name :
label1=Label(root,frame,text="SCHOOL MANAGEMENT SYSTEM",fg="#17202A",bg="#E5E4E2",font=("Century",28,"bold"))
label1.place(x=350,y=25)

#School Name Label :
labschoolname=Label(root,text="Dr. Kakasaheb Purnapatre Madhyamik Vidyalay,Chalisgaon",font=("Rapier",9,"italic"),bg="#17202A",fg="white").place(x=1030,y=-1)

#Design on frame :
paneldesign=PanedWindow(root,orient ='vertical',height=260,width=20,bg="#E67E22").place(x=259,y=140)
paneldesign1=PanedWindow(root,orient ='vertical',height=260,width=20,bg="#E67E22").place(x=1059,y=380)

#lower line and upper two lines:
paneldesign2=PanedWindow(root,orient ='horizontal',height=5,width=1390,bg="#E67E22").place(x=0,y=694)
#Upper lines :
paneldesign3 =PanedWindow(root,orient ='horizontal',height=3,width=1030,bg="#E67E22").place(x=0,y=20)
paneldesign4=PanedWindow(root,orient ='horizontal',height=3,width=1030,bg="#E67E22").place(x=334,y=87)

root.mainloop()