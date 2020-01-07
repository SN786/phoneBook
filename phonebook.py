##PROJECCT COMPLETED 
import sqlite3  
from Tkinter import *
import splash
import tkMessageBox
root=Tk()
con=sqlite3.Connection('db_phone')
cur=con.cursor()

r=17
name="sohrat"
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("create table if not exists person_deta(P_id INTEGER primary key AUTOINCREMENT,fname varchar(20),mname varchar(10),lname varchar(20),company varchar(20),address varchar(30),city varchar(15),pin INTEGER,website varchar(25),bdate varchar(15))")
cur.execute("create table if not exists person_phones(P_id INTEGER,contact_type VARCHAR(10),ph_no INTEGER,PRIMARY KEY(P_id,ph_no),foreign key(P_id) references person_deta(P_id) on delete cascade)")
cur.execute("create table if not exists person_emails(P_id INTEGER,email_type VARCHAR(10),email_id varchar(25),PRIMARY KEY(P_id,email_id),foreign key(P_id) references person_deta(P_id) on delete cascade)")

##cur.execute("Alter table person_deta add constraint fk1 foreign key(P_id) references person_phones(P_id)")
##cur.execute("Alter table person_deta add constraint fk2 foreign key(P_id) references person_emails(P_id)")
##cur.execute("select * from person_deta")
##pp=cur.fetchall()
##print pp
##
##n="personal"
##p=8340410384
##print m
##
##cur.execute("select * from person_phones")
##k=cur.fetchall()
####Label(root,text=str(k)).grid(row=22,column=3)
##print k




root.title("PhoneBook")
img=PhotoImage(file="phone.gif")
Label(root,image=img).grid(row=4,column=4)
root.geometry("580x600")
v1=IntVar()
v2=IntVar()

Label(root,text="Phone Book",font='times 22 bold',fg='blue').grid(row=5,column=4)
Label(root,text="First Name",font=('verdana 11')).grid(row=6,column=2)
e1=Entry(root,font=('verdana 8'))
e1.grid(row=6,column=4)

Label(root,text="Middle Name",font=('verdana 11')).grid(row=7,column=2)
e2=Entry(root,font=('verdana 8'))
e2.grid(row=7,column=4)

Label(root,text="Last Name",font=('verdana 11')).grid(row=8,column=2)
e3=Entry(root,font=('verdana 8'))
e3.grid(row=8,column=4)

Label(root,text="Company Name",font=('verdana 11')).grid(row=9,column=2)
e4=Entry(root,font=('verdana 8'))
e4.grid(row=9,column=4)

Label(root,text="Address",font=('verdana 11')).grid(row=10,column=2)
e5=Entry(root,font=('verdana 8'))
e5.grid(row=10,column=4)

Label(root,text="City",font=('verdana 11')).grid(row=11,column=2)
e6=Entry(root,font=('verdana 8'))
e6.grid(row=11,column=4)

Label(root,text="Pin Code",font=('verdana 11')).grid(row=12,column=2)
e7=Entry(root,font=('verdana 8'))
e7.grid(row=12,column=4)

Label(root,text="Website Url",font=('verdana 11')).grid(row=13,column=2)
e8=Entry(root,font=('verdana 8'))
e8.grid(row=13,column=4)

Label(root,text="Date of Birth",font=('verdana 11')).grid(row=14,column=2)
e9=Entry(root,font=('verdana 8'))
e9.grid(row=14,column=4)

##def multiple_contacts():
##    
##    global r
##    
##    print r
##    Label(root,text="Select Phone Type:",font=('verdana 12')).grid(row=r,column=2)
##    raduio_button1=Radiobutton(root,text="Office",variable=v1,value=1).grid(row=r,column=4)
##    raduio_button1=Radiobutton(root,text="Home",variable=v1,value=2).grid(row=r,column=5)
##    raduio_button1=Radiobutton(root,text="Mobile",variable=v1,value=3).grid(row=r,column=6)
##    r=r+1
##    Label(root,text="Phone Number").grid(row=r,column=2)
##    Button(root,text="+",command=multiple_contacts).grid(row=r,column=5)
##    em1=Entry(root)
##    em1.grid(row=r,column=4)
##    r=r+1

Label(root,text="Select Phone Type:",font=('verdana 12')).grid(row=15,column=2)
raduio_button1=Radiobutton(root,text="Office",variable=v1,value=1).grid(row=15,column=4)
raduio_button1=Radiobutton(root,text="Home",variable=v1,value=2).grid(row=15,column=5)
raduio_button1=Radiobutton(root,text="Mobile",variable=v1,value=3).grid(row=15,column=6)
Label(root,text="Phone Number").grid(row=16,column=2)
Button(root,text="+").grid(row=16,column=5)
e10=Entry(root,font=('verdana 8'))
e10.grid(row=16,column=4)


Label(root,text="Select Email Type:",font=('verdana 12')).grid(row=21,column=2)
raduio_button1=Radiobutton(root,text="Office",variable=v2,value=1).grid(row=21,column=4)
raduio_button1=Radiobutton(root,text="Personal",variable=v2,value=2).grid(row=21,column=5)
Label(root,text="Email id").grid(row=22,column=2)
Button(root,text="+").grid(row=22,column=5)
e11=Entry(root,font=('verdana 8'))
e11.grid(row=22,column=4)

def save():
    cur.execute("insert into person_deta(fname,mname,lname,company,address,city,pin,website,bdate) values(?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
    cur.execute("SELECT last_insert_rowid()")
    l=cur.fetchall()
    
    m=l[0][0]
    n="Not Available"
    if(int(v1.get())==1):
        n="office"
    elif(int(v1.get())==2):
        n="Home"
    else:
        n="Mobile"
    cur.execute("Insert into person_phones(P_id,contact_type,ph_no) values(?,?,?)",(m,n,e10.get()))
    e_type="Not Available"
    if(int(v2.get())==1):
        e_type="office"
    elif(int(v2.get())==2):
        e_type="Personal"
    cur.execute("Insert into person_emails(P_id,email_type,email_id) values(?,?,?)",(m,e_type,e11.get()))

    cur.execute("select * from person_deta")
    k=cur.fetchall()
    
    cur.execute("select * from person_phones")
    l=cur.fetchall()
    
    cur.execute("select * from person_emails")
    m=cur.fetchall()
    
    

    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    v1.set(0)
    v2.set(0)
    tkMessageBox.showinfo("Saved","Contact Saved Sucessfully")
##    e12.delete(0,END)
##    e13.delete(0,END)
##    e14.delete(0,END)



def search():
    root1=Tk()
    root1.geometry("360x370")
##    scrollbar=Scrollbar(root1)
##    scrollbar.pack(side=RIGHT,fill=Y)
    Label(root1,text="Search contact",font="times 20 bold",fg='Blue').grid(row=0,column=4)
    Label(root1,text="Enter Name",font=('verdana 12')).grid(row=1,column=3)
    lb=Listbox(root1,width=20,height=14,font=('verdana 11'))
    lb.grid(row=2,column=4)
    e12=Entry(root1,width=20,font=('verdana 11'))
    e12.grid(row=1,column=4)
    
    def search_by(event):
        
        li=[0]*2
        b=[0]*5
        
        li[0]=['%'+str(e12.get())+'%']
        b[0]=li[0]*3
        
        lb.delete(0,END)
        cur.execute("select * from person_deta where fname like ? or mname like ? or lname like ? ",b[0])
        temp=cur.fetchall()
        for i in temp:
            lb.insert(END, str(i[1]+' '+i[2]+' '+i[3]))
    
        def CurSelet(evt):
            
            #value=str((lb.get(ACTIVE)))
            #print value
            var=lb.curselection()
            geti=var[0]
            root3=Tk()
            root3.geometry("350x350")
            k2=str(temp[geti][1])
            
            
            Label(root3,text="Person Details",font='times 20 bold',fg='blue').grid(row=1,column=3)
            
            
            Label(root3,text="Name: " + k2 + " " +str(temp[geti][2])+" "+str(temp[geti][3]),font=('verdana 11')).grid(row=2,column=3,sticky=W)
            Label(root3,text="Company Name: " +"  " +str(temp[geti][4]),font=('verdana 11')).grid(row=3,column=3,sticky=W)

            Label(root3,text="Address: " + str(temp[geti][5]),font=('verdana 11')).grid(row=11,column=3,sticky=W)
            Label(root3,text="City: " + str(temp[geti][6]),font=('verdana 11')).grid(row=4,column=3,sticky=W)
            Label(root3,text="Pin Code: " + str(temp[geti][7]),font=('verdana 11')).grid(row=5,column=3,sticky=W)
            Label(root3,text="Website: " + str(temp[geti][8]),font=('verdana 11')).grid(row=6,column=3,sticky=W)
            Label(root3,text="Bdate: " + str(temp[geti][9]),font=('verdana 11')).grid(row=7,column=3,sticky=W)
            p_id_fe=temp[geti][0]
            
            cur.execute("select * from person_phones where P_id={0}".format(p_id_fe))
            phones_list=cur.fetchall()
            
            mobile_no=phones_list[0][2]
            Label(root3,text="Mobile Type: " + str(phones_list[0][1]),font=('verdana 11') ).grid(row=8,column=3,sticky=W)
            Label(root3,text="Mobile Number: " + str(mobile_no),font=('verdana 11')).grid(row=9,column=3,sticky=W)

            ##Fetch email and printing 
            cur.execute("select * from person_emails where P_id={0}".format(p_id_fe))
            email_list=cur.fetchall()
            email_id=email_list[0][2]
            Label(root3,text="Email id Type: " + str(email_id),font=('verdana 11')).grid(row=10,column=3,sticky=W)
            Label(root3,text="Email id: " + str(email_list[0][2]),font=('verdana 11')).grid(row=11,column=3,sticky=W)

            def delete_contact():
                
                
                root3.destroy()
                e12.delete(0,END)
                lb.delete(0,END)
                yesno=tkMessageBox.askyesno("Warning","Are You Sure You Want To DELETE This Contact")
                if(yesno):
                    cur.execute("delete from person_deta where P_id={0}".format(p_id_fe))
                    con.commit()
                    tkMessageBox.showinfo("Deleted","Contact Deleted Sucessfully")
            def close_it():
                    root3.destroy()
                
            Button(root3,text="Delete",command=delete_contact).grid(row=12,column=2,sticky=W)

##edit contact new root window
            def edit_contact_details():
##                e12.delete(0,END)
                root3.destroy()
                root5=Tk()
                v1=IntVar()
                v2=IntVar()
                

                Label(root5,text="Edit Contact Details",font='times 20 bold',fg='blue').grid(row=5,column=4)
                Label(root5,text="First Name",font=('verdana 11')).grid(row=6,column=2)
                e1=Entry(root5,font=('verdana 8'))
                e1.grid(row=6,column=4)

                Label(root5,text="Middle Name",font=('verdana 11')).grid(row=7,column=2)
                e2=Entry(root5,font=('verdana 8'))
                e2.grid(row=7,column=4)

                Label(root5,text="Last Name",font=('verdana 11')).grid(row=8,column=2)
                e3=Entry(root5,font=('verdana 8'))
                e3.grid(row=8,column=4)

                Label(root5,text="Company Name",font=('verdana 11')).grid(row=9,column=2)
                e4=Entry(root5,font=('verdana 8'))
                e4.grid(row=9,column=4)

                Label(root5,text="Address",font=('verdana 11')).grid(row=10,column=2)
                e5=Entry(root5,font=('verdana 8'))
                e5.grid(row=10,column=4)

                Label(root5,text="City",font=('verdana 11')).grid(row=11,column=2)
                e6=Entry(root5,font=('verdana 8'))
                e6.grid(row=11,column=4)

                Label(root5,text="Pin Code",font=('verdana 11')).grid(row=12,column=2)
                e7=Entry(root5,font=('verdana 8'))
                e7.grid(row=12,column=4)

                Label(root5,text="Website Url",font=('verdana 11')).grid(row=13,column=2)
                e8=Entry(root5,font=('verdana 8'))
                e8.grid(row=13,column=4)

                Label(root5,text="Date of Birth",font=('verdana 11')).grid(row=14,column=2)
                e9=Entry(root5,font=('verdana 8'))
                e9.grid(row=14,column=4)
                
                Label(root5,text="Phone Number",font=('verdana 11')).grid(row=15,column=2)
                e10=Entry(root5,font=('verdana 8'))
                e10.grid(row=15,column=4)

                Label(root5,text="Email id",font=('verdana 11')).grid(row=16,column=2)
                e11=Entry(root5,font=('verdana 8'))
                e11.grid(row=16,column=4)
                
                
                cur.execute("select * from person_deta where P_id={0}".format(p_id_fe))
                vae=cur.fetchall()
               
                e1.insert(0,vae[0][1])
                e2.insert(0,vae[0][2])
                e3.insert(0,vae[0][3])
                e4.insert(0,vae[0][4])
                e5.insert(0,vae[0][5])
                e6.insert(0,vae[0][6])
                e7.insert(0,vae[0][7])
                e8.insert(0,vae[0][8])
                e9.insert(0,vae[0][9])
                e10.insert(0,phones_list[0][2])
                e11.insert(0,email_list[0][2])
                def update_contact():
                    e12.delete(0,END)
                
                    lb.delete(0,END)
                    cur.execute("update person_deta set fname=?,mname=?,lname=?,company=?,address=?,city=?,pin=?,website=?,bdate=? where P_id=? ",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),p_id_fe))
                    cur.execute("update person_phones set ph_no=? where P_id=? ",(e10.get(),p_id_fe))
                    cur.execute("update person_emails set email_id=? where P_id=? ",(e11.get(),p_id_fe))
                    con.commit()
                    tkMessageBox.showinfo("Updated","Contact Updated Sucessfully")
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    e4.delete(0,END)
                    e5.delete(0,END)
                    e6.delete(0,END)
                    e7.delete(0,END)
                    e8.delete(0,END)
                    e9.delete(0,END)
                    e10.delete(0,END)
                    e11.delete(0,END)
                    root5.destroy()

                
                Button(root5,text="Save",command=update_contact).grid(row=17,column=4)
                cur.execute("Select * from person_deta")
                vf=cur.fetchall()
            

            Button(root3,text="Edit",command=edit_contact_details).grid(row=12,column=3)
            Button(root3,text="Close",command=close_it).grid(row=12,column=4)
##            Label(root3,text="Name: " + k2 ).grid(row=1,column=2)
##            Label(root3,text="Name: " + k2 ).grid(row=1,column=2)
            root3.mainloop()


        lb.bind('<<ListboxSelect>>',CurSelet)
    e12.bind_all("<Key>",search_by)
    
        
def edit_contact():
    root6=Tk()
    root6.geometry("360x370")
    Label(root6,text="Search contact",font="times 20 bold",fg='Blue').grid(row=0,column=4)
    Label(root6,text="Enter Name",font=('verdana 11')).grid(row=1,column=3)
    lb=Listbox(root6,width=20,height=14,font=('verdana 11'))
    lb.grid(row=2,column=4)
    e12=Entry(root6,width=20,font=('verdana 11'))
    e12.grid(row=1,column=4)
    def search_by2(event):
       
        li=[0]*2
        b=[0]*5
        li[0]=['%'+str(e12.get())+'%']
        b[0]=li[0]*3
        lb.delete(0,END)
        cur.execute("select * from person_deta where fname like ? or mname like ? or lname like ?",b[0])
        temp=cur.fetchall()
        for i in temp:
            lb.insert(END,str(i[1]+' '+i[2]+ ' '+i[3]))
        def edit_contact_details2(e):
            
            root7=Tk()
            root7.geometry("400x350")
            var=lb.curselection()
            geti=var[0]
            v1=IntVar()
            v2=IntVar()
            p_id_fe=temp[geti][0]
            

            Label(root7,text="Edit Contact Details",font='times 20 bold',fg='blue').grid(row=5,column=4)
            Label(root7,text="First Name",font=('verdana 11')).grid(row=6,column=2)
            e1=Entry(root7,font=('verdana 8'))
            e1.grid(row=6,column=4)


            Label(root7,text="Middle Name",font=('verdana 11')).grid(row=7,column=2)
            e2=Entry(root7,font=('verdana 8'))
            e2.grid(row=7,column=4)

            Label(root7,text="Last Name",font=('verdana 11')).grid(row=8,column=2)
            e3=Entry(root7,font=('verdana 8'))
            e3.grid(row=8,column=4)

            Label(root7,text="Company Name",font=('verdana 11')).grid(row=9,column=2)
            e4=Entry(root7,font=('verdana 8'))
            e4.grid(row=9,column=4)

            Label(root7,text="Address",font=('verdana 11')).grid(row=10,column=2)
            e5=Entry(root7,font=('verdana 8'))
            e5.grid(row=10,column=4)

            Label(root7,text="City",font=('verdana 11')).grid(row=11,column=2)
            e6=Entry(root7,font=('verdana 8'))
            e6.grid(row=11,column=4)

            Label(root7,text="Pin Code",font=('verdana 11')).grid(row=12,column=2)
            e7=Entry(root7,font=('verdana 8'))
            e7.grid(row=12,column=4)

            Label(root7,text="Website Url",font=('verdana 11')).grid(row=13,column=2)
            e8=Entry(root7,font=('verdana 8'))
            e8.grid(row=13,column=4)

            Label(root7,text="Date of Birth",font=('verdana 11')).grid(row=14,column=2)
            e9=Entry(root7,font=('verdana 8'))
            e9.grid(row=14,column=4)
            
            Label(root7,text="Phone Number",font=('verdana 11')).grid(row=15,column=2)
            e10=Entry(root7,font=('verdana 8'))
            e10.grid(row=15,column=4)

            Label(root7,text="Email id",font=('verdana 11')).grid(row=16,column=2)
            e11=Entry(root7,font=('verdana 8'))
            e11.grid(row=16,column=4)
            
            cur.execute("select * from person_phones where P_id={0}".format(p_id_fe))
            phones_list=cur.fetchall()
            
            cur.execute("select * from person_emails where P_id={0}".format(p_id_fe))
            email_list=cur.fetchall()
            cur.execute("select * from person_deta where P_id={0}".format(p_id_fe))
            vae=cur.fetchall()
           
            e1.insert(0,vae[0][1])
            e2.insert(0,vae[0][2])
            e3.insert(0,vae[0][3])
            e4.insert(0,vae[0][4])
            e5.insert(0,vae[0][5])
            e6.insert(0,vae[0][6])
            e7.insert(0,vae[0][7])
            e8.insert(0,vae[0][8])
            e9.insert(0,vae[0][9])
            e10.insert(0,phones_list[0][2])
            e11.insert(0,email_list[0][2])
            def update_contact2():
                
                
                e12.delete(0,END)
                
                lb.delete(0,END)
                cur.execute("update person_deta set fname=?,mname=?,lname=?,company=?,address=?,city=?,pin=?,website=?,bdate=? where P_id=? ",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),p_id_fe))
                cur.execute("update person_phones set ph_no=? where P_id=? ",(e10.get(),p_id_fe))
                cur.execute("update person_emails set email_id=? where P_id=? ",(e11.get(),p_id_fe))
                con.commit()
                tkMessageBox.showinfo("Updated","Contact Updated Sucessfully")
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                e7.delete(0,END)
                e8.delete(0,END)
                e9.delete(0,END)
                e10.delete(0,END)
                e11.delete(0,END)
                root7.destroy()

        
            Button(root7,text="Save",command=update_contact2).grid(row=17,column=4)
            cur.execute("Select * from person_deta")
            root7.mainloop()


        
        
##            Label(root3,text="Name: " + k2 ).grid(row=1,column=2)
##            Label(root3,text="Name: " + k2 ).grid(row=1,column=2)
        lb.bind('<<ListboxSelect>>',edit_contact_details2)
        
    
    root6.bind_all("<Key>",search_by2)
    root6.mainloop()

def close_all():
    root.destroy()
    
    
    

    
    
    
Button(root,text="Save",command=save).grid(row=23,column=3)
Button(root,text="Search",command=search).grid(row=23,column=4)
Button(root,text="Close",command=close_all).grid(row=23,column=5)
Label(root,text="          ").grid(row=23,column=6)
Button(root,text="Edit",command=edit_contact).grid(row=23,column=7)

con.commit()
root.mainloop()
