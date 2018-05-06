#!/usr/bin/python

#Developed by Kamlesh Silag

#Project Topic on Personal Assistant 


from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3

conn = sqlite3.connect('testnew.sqlite')

top = tkinter.Tk()
global cnt
cnt=0

#adding enter task
var1 = StringVar()
label1 = Label(top, textvariable=var1, relief=RAISED )
var1.set("----Enter Your Task Details------")
label1.pack()


var = IntVar()

def sel():
        selection = "Your Priority for This task is " + str(var.get())
        label_radio.config(text=selection)
        var5.set(selection)



varPrio = StringVar()
label_Prio = Label(top, textvariable=varPrio, relief=RAISED )
varPrio.set("Priority:")
label_Prio.pack()


R1 = Radiobutton(top,text="1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(top, text="2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(top, text="3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)



varTime = StringVar()
label_Time = Label(top, textvariable=varTime, relief=RAISED )
varTime.set("Time:")
label_Time.pack()


L1 = Label(top,text="HH:")
L2 = Label(top,text="MM:")
L1.pack()
E1 = Entry(top,bd=5)
E1.pack()
E2 = Entry(top,bd=5)
L2.pack()
E2.pack()

tastname = Label(top,text="Task Name:-")
tastname.pack();

text = Text(top,bd=5,height=10)
text.insert(INSERT, "")
text.insert(END, "")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")


def helloCallBack():

    a=str(var.get())
    task = text.get("1.0",END)
    hour = str(E1.get())
    minutes = str(E2.get())

    print(hour+""+minutes)

    global cnt
    cnt=cnt+1

    print(a+"")
    print("task is "+task)
    print("Global :"+str(cnt));
    conn.execute("INSERT INTO Assistant (ID,NAME,PRIORITY,Hour,Minutes) VALUES (?,?,?,?,?)",(cnt,task,a,hour,minutes));
    print("Successfully Inserted")
    messagebox.showinfo( "!", "Task Submitted")
    conn.commit();


    cursor = conn.execute("  SELECT * FROM Assistant ")
    for row in cursor:
        print("ID :",row[0])
        print("Task :",row[1])
        print("Priority :",row[2])
        print("Hour:",row[3])
        print("Minutes:",row[4])


def viewwindow():
    window = tkinter.Toplevel(top)
    lb1 = Listbox(window,width=50,height=20)

    m1 = Label(window, text="Serial No      Task        Priority        Hour        Min                                ",)
    m1.pack();



    cursor = conn.execute("  SELECT * FROM Assistant ")
    for row in cursor:
        data=str(str(row[0])+"              "+str(row[1])+"          "+str(row[2])+"            "+str(row[3])+ "                "+str(row[4]))
        lb1.insert(1,data)


        #print("Hour:", row[3])
        #print("Minutes:", row[4])

    lb1.pack();


B = Button(top, text ="Submit ",command=helloCallBack)
B.pack();

View= Button(top,text="View",command=viewwindow)
View.pack();



var5 = StringVar()
var5.set("")
label_radio = Label(top, textvariable=var5, relief=RAISED)
#label_radio.pack()





top.mainloop()
