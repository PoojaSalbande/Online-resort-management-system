

from cProfile import label
from datetime import datetime

from distutils.cmd import Command
from email.errors import MessageError
from random import Random, random
from re import L

from tkinter import*
from tkinter.font import BOLD
from turtle import st, title, width
from xml.dom.minicompat import StringTypes

from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
from cv2 import IMWRITE_JPEG2000_COMPRESSION_X1000
from matplotlib import image
import mysql.connector
from requests import delete
from time import strftime
from datetime import datetime
#from customer import cust_win

win=Tk()
win.title("Resort management system")
#to set icon
#win.iconbitmap("icon.ico")
win.geometry("900x400")
#win.attributes('-fullscreen',True)


def ulogin():
    
    if ((var1.get()=="") or (var2.get()=="")):
        messagebox.showwarning("warning","please enter text")
   
        
    else:
        f=Toplevel(win)
        f.geometry("1550x600+0+265")
        lbl1=Label(f,text="USER_MENU",font=("times new roman",20,BOLD),bg="Gold",fg="brown",bd=4)
        lbl1.place(x=0,y=2,width=1550,height=30)
            
        def useradd():
                #f4=Frame(win,bd=4,relief=RIDGE)
                #f4.place(x=0,y=245,width=1550,height=600)
                f4=Toplevel(win)
                f4.geometry("1550x600+0+265")
                #variable for generating random number as reference number
                var_ref=StringVar()
                X=random.randint(1,9999)
                var_ref.set(str(X))
                var_name=StringVar()
                var_mobile=StringVar()
                var_nationality=StringVar()
                var_email=StringVar()
                var_gender=StringVar()
                var_add=StringVar()
                var_id=StringVar()

                lbl=Label(f4,text=" ADD CUSTOMER DETAILS",font=("times new roman",20,BOLD),fg="brown",bg="gold",bd=10)
                lbl.place(x=0,y=0,width=1550,height=40)
                frame1=Frame(f4,bd=4,relief=RIDGE)
                frame1.place(x=520,y=60,width=450,height=400)
                lbl1=Label(frame1,text="Cust_ref",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=0,column=0,pady=1)
                entry_ref=ttk.Entry(frame1,textvariable=var_ref,width=20,font=("times new roman",15))
                entry_ref.grid(row=0,column=1)
                #name
                lbl1=Label(frame1,text="Name",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=1,column=0,pady=1)
                entry_n=ttk.Entry(frame1,textvariable=var_name,width=20,font=("times new roman",15))
                entry_n.grid(row=1,column=1)
                #number
                lbl1=Label(frame1,text="mobile",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=2,column=0,pady=1)
                entry_mob=ttk.Entry(frame1,textvariable=var_mobile, width=20,font=("times new roman",15))
                entry_mob.grid(row=2,column=1)
                #natinality
                lbl1=Label(frame1,text="Nationality", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=3,column=0,pady=1)
                entry_na=ttk.Entry(frame1,textvariable=var_nationality,width=20,font=("times new roman",15))
                entry_na.grid(row=3,column=1)
            #email
                lbl1=Label(frame1,text="Email", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=4,column=0,pady=1)
                entry_email=ttk.Entry(frame1,textvariable=var_email,width=20,font=("times new roman",15))
                entry_email.grid(row=4,column=1)
                #gender combobox
                lbl1=Label(frame1,text="Gender", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=5,column=0,pady=1)
                entry_add=ttk.Entry(frame1,textvariable=var_gender,width=20,font=("times new roman",15,))
                entry_add.grid(row=5,column=1)
                
                #address
                lbl1=Label(frame1,text="address", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=6,column=0,pady=1)
                entry_add=ttk.Entry(frame1,textvariable=var_add,width=20,font=("times new roman",15,))
                entry_add.grid(row=6,column=1)
                #id proof combobox
                lbl1=Label(frame1,text="Customer id",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=7,column=0,pady=1)
                combo2=ttk.Combobox(frame1,width=20,font=("times new roman",14),state="read only")
                combo2["value"]=("adhar","pan","other")
                combo2.current(0)
                combo2.grid(row=7,column=1)
                def add_info():
                    if ((var_name.get()=="")or (var_mobile.get()=="")):
                        messagebox.showwarning("error","enter required fields",parent=f4)
                    else:
                        try:

                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    var_ref.get(),
                                                                                    var_name.get(),
                                                                                    var_mobile.get(),
                                                                                    var_nationality.get(),
                                                                                    var_email.get(),
                                                                                    var_gender.get(),
                                                                                    var_add.get(),
                                                                                    var_id.get()
                                                                                    
                                                                                                ))
                            conn.commit()
                            #fetch_data()

                            
                            
                            conn.close()
                            messagebox.showinfo("SUCCESS","CUSTOMER ADDED",parent=f4)
                        except Exception as es:
                            messagebox.showwarning("warning",f"wrong:{str(es)}",parent=f4)
                
                
                frame2=Frame(frame1,bd=4,relief=RIDGE)
                frame2.place(x=9,y=300,width=130,height=35)
                btn =Button(frame2,text="ADD",font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",command=add_info)
                btn .grid(row=0,column=0,)
        f11=Frame(f,bd=4,relief=RIDGE)
        f11.place(x=510,y=40,width=550,height=50)
        b1=Button(f11,text="ADD DETAILS",command=useradd, fg="black",bg="blue",font=("times new roman",15,BOLD),width=50)
        b1.grid(row=0,column=0)
            
        
        
    
   


def menu():
    
    if ((var1.get()=="") or (var2.get()=="")):
        messagebox.showwarning("warning","please enter text")
    else:
    
        if var1.get()=="sai" and var2.get()=="1122":


            f3=Frame(win,bd=4,relief=RIDGE)
            f3.place(x=0,y=245,width=1550,height=600)
            
            #frame
            
            lbl1=Label(f3,text="MENU",font=("times new roman",35,BOLD),bg="Gold",fg="brown",bd=4)
            lbl1.place(x=0,y=2,width=1550,height=50)
            btn_frame=Frame(f3,bd=2,relief=RIDGE)
            btn_frame.place(x=450,y=80,width=620,height=254)
            #add buttons in menu
            def customer():
                #f4=Frame(win,bd=4,relief=RIDGE)
                #f4.place(x=0,y=245,width=1550,height=600)
                f4=Toplevel(win)
                f4.geometry("1550x600+0+265")
                #variable for generating random number as reference number
                var_ref=StringVar()
                X=random.randint(1,9999)
                var_ref.set(str(X))
                var_name=StringVar()
                var_mobile=StringVar()
                var_nationality=StringVar()
                var_email=StringVar()
                var_gender=StringVar()
                var_add=StringVar()
                var_id=StringVar()

                lbl=Label(f4,text=" ADD CUSTOMER DETAILS",font=("times new roman",20,BOLD),fg="brown",bg="gold",bd=10)
                lbl.place(x=0,y=0,width=1550,height=40)
                frame1=Frame(f4,bd=4,relief=RIDGE)
                frame1.place(x=0,y=60,width=450,height=520)
                lbl1=Label(frame1,text="Cust_ref",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=0,column=0,pady=1)
                entry_ref=ttk.Entry(frame1,textvariable=var_ref,width=20,font=("times new roman",15))
                entry_ref.grid(row=0,column=1)
                #name
                lbl1=Label(frame1,text="Name",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=1,column=0,pady=1)
                entry_n=ttk.Entry(frame1,textvariable=var_name,width=20,font=("times new roman",15))
                entry_n.grid(row=1,column=1)
                #number
                lbl1=Label(frame1,text="mobile",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=2,column=0,pady=1)
                entry_mob=ttk.Entry(frame1,textvariable=var_mobile, width=20,font=("times new roman",15))
                entry_mob.grid(row=2,column=1)
                #natinality
                lbl1=Label(frame1,text="Nationality", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=3,column=0,pady=1)
                entry_na=ttk.Entry(frame1,textvariable=var_nationality,width=20,font=("times new roman",15))
                entry_na.grid(row=3,column=1)
            #email
                lbl1=Label(frame1,text="Email", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=4,column=0,pady=1)
                entry_email=ttk.Entry(frame1,textvariable=var_email,width=20,font=("times new roman",15))
                entry_email.grid(row=4,column=1)
                #gender combobox
                lbl1=Label(frame1,text="Gender", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=5,column=0,pady=1)
                entry_add=ttk.Entry(frame1,textvariable=var_gender,width=20,font=("times new roman",15,))
                entry_add.grid(row=5,column=1)
                
                #address
                lbl1=Label(frame1,text="address", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=6,column=0,pady=1)
                entry_add=ttk.Entry(frame1,textvariable=var_add,width=20,font=("times new roman",15,))
                entry_add.grid(row=6,column=1)
                #id proof combobox
                lbl1=Label(frame1,text="Customer id",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=7,column=0,pady=1)
                entry_add=ttk.Entry(frame1,textvariable=var_id,width=20,font=("times new roman",15,))
                entry_add.grid(row=7,column=1)
                
            
                def add_info():
                    if ((var_name.get()=="")or (var_mobile.get()=="")):
                        messagebox.showwarning("error","enter required fields",parent=f4)
                    else:
                        try:

                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    var_ref.get(),
                                                                                    var_name.get(),
                                                                                    var_mobile.get(),
                                                                                    var_nationality.get(),
                                                                                    var_email.get(),
                                                                                    var_gender.get(),
                                                                                    var_add.get(),
                                                                                    var_id.get()
                                                                                    
                                                                                                ))
                            conn.commit()
                            fetch_data()

                            
                            
                            conn.close()
                            messagebox.showinfo("SUCCESS","CUSTOMER ADDED",parent=f4)
                        except Exception as es:
                            messagebox.showwarning("warning",f"wrong:{str(es)}",parent=f4)
                def fetch_data():
                    conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select *from customer")
                    rows=my_cursor.fetchall()
                    for i in rows:
                        tree.insert("",END,values=i)
                    conn.commit()
                    conn.close()
                def get_cursor(event=""):
                    cursor_row=tree.focus()
                    content=tree.item(cursor_row)
                    row=content["values"]
                
                    var_ref.set(row[0])
                    var_name.set(row[1])
                    var_mobile.set(row[2])
                    var_nationality.set(row[3])
                    var_email.set(row[4])
                    var_gender.set(row[5])
                    var_add.set(row[6])
                    var_id.set(row[7])
                def update():
                    if ((var_name.get()=="")or (var_mobile.get()=="")):
                        messagebox.showwarning("error","enter required fields",parent=f4)
                    else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update customer set name=%s,mobile=%s,nationality=%s,email=%s,gender=%s,address=%s,customer_id=%s where ref=%s",(
                                                                                                    
                                                                                                    var_name.get(),
                                                                                                    var_mobile.get(),
                                                                                                    var_nationality.get(),
                                                                                                    var_email.get(),
                                                                                                    var_gender.get(),
                                                                                                    var_add.get(),
                                                                                                    var_id.get(),
                                                                                                    var_ref.get()
                        ))

                        conn.commit()
                        fetch_data()
                        conn.close()
                        messagebox.showinfo("SUCCESS","UPDATED",parent=f4)
                def Delete():
                    Delete=messagebox.askyesno("rms","DO YOU WANT TO DELETE?",parent=f4)
                    
                    if Delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                        my_cursor=conn.cursor()
                        query="delete from customer where ref=%s"
                        value=(var_ref.get(),)
                        my_cursor.execute(query,value)
                
                    else:
                        if not Delete:
                            return
                    conn.commit()
                    fetch_data()
                    conn.close()
                def search():
                    conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from customer where " +str(search_var.get())+" LIKE '%"+str(text_search.get())+"%'")
                    rows=my_cursor.fetchall()
                    for i in rows:
                        tree.insert("",END,values=i)
                        conn.commit()
                        
                    conn.close()
                frame2=Frame(frame1,bd=4,relief=RIDGE)
                frame2.place(x=9,y=350,width=367,height=35)
                btn =Button(frame2,text="ADD",font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",command=add_info)
                btn .grid(row=0,column=0,)
                btn =Button(frame2,text="UPDATE", font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",command=update)
                btn .grid(row=0,column=1,padx=2)
                btn =Button(frame2,text="DELETE",font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",command=Delete)
                btn .grid(row=0,column=2,padx=2)
                #btn =Button(frame2,text="RESET",font=("times new roman",10,),width=20,bg="blue",fg="black",bd=4,cursor="hand1")
                #btn .grid(row=1,column=1,pady=1)
                frame6=Frame(f4,bd=4,relief=RIDGE)
                frame6.place(x=450,y=60,width=1400,height=600)
                lbl1=Label(frame6,text="SEARCH BY:",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=0,column=0,pady=1)
                search_var=StringVar()

                combo1=ttk.Combobox(frame6,textvariable=search_var, width=20,font=("times new roman",15),state="read only")
                combo1["value"]=("mobile","name","ref")
                combo1.current(0)
                combo1.grid(row=0,column=1)
                text_search=StringVar()

                entry_add=ttk.Entry(frame6,textvariable=text_search,width=15,font=("times new roman",15,))
                entry_add.grid(row=0,column=2,padx=2)
                btn =Button(frame6,text="SEARCH",command=search, font=("times new roman",10),width=8,bg="blue",fg="black",bd=4,cursor="hand1")
                btn .grid(row=0,column=3,padx=2)
                btn =Button(frame6,text="SHOW ALL",command=fetch_data, font=("times new roman",10),width=8,bg="blue",fg="black",bd=4,cursor="hand1")
                btn .grid(row=0,column=4,padx=2)
                frame7=Frame(frame6,bd=4,relief=RIDGE)
                frame7.place(x=0,y=80,width=800,height=300)
                    
                sbb_y=Scrollbar(frame7,orient='vertical')
                sbb_y.pack(side=RIGHT,fill="y")
                sbb_x=Scrollbar(frame7,orient='horizontal')
                sbb_x.pack(side=BOTTOM,fill="x")
                tree = ttk.Treeview(frame7,height=30,column=("c1", "c2","c3","c4","c5","c6","c7","c8"), show='headings',xscrollcommand=sbb_x.set,yscrollcommand=sbb_y.set)
            
                tree.column("# 1", anchor=CENTER)
                tree.heading("# 1", text="REF_NO")
                tree.column("# 2", anchor=CENTER)
                tree.heading("# 2", text="NAME")
                tree.column("# 3", anchor=CENTER)
                tree.heading("# 3", text="MOBILE")
                tree.column("# 4", anchor=CENTER)
                tree.heading("# 4", text="NATIONALITY")
                tree.column("# 5", anchor=CENTER)
                tree.heading("# 5", text="EMAIL")
                tree.column("# 6", anchor=CENTER)
                tree.heading("# 6", text="GENDER")
                tree.column("# 7", anchor=CENTER)
                tree.heading("# 7", text="ADDRESS")
                tree.column("# 8", anchor=CENTER)
                tree.heading("# 8", text="CUSTOMER")
                tree.pack()
                tree.bind("<ButtonRelease-1>",get_cursor)
                fetch_data()
                
            
                sbb_x.config(command=tree.xview)
                sbb_y.config(command=tree.yview)

                
                #scroll_x.config(command=tree.xview)
                #croll_y.config(command=details.yvie
                #function for adding values in customer table
            ##-------------END OF CUSTOMER FUNCTION--------------
            def reservation():
                f7=Toplevel(win)
                f7.geometry("1550x600+0+265")
                #------------variable creation------------------------------------------------------
                var_contact=StringVar()
                var_in=StringVar()
                var_out=StringVar()
                var_type=StringVar()
                var_avail=StringVar()
                var_days=StringVar()
                var_food=StringVar()
                var_paidtax=StringVar()
                var_sub=StringVar()
                var_total=StringVar()
                def fetch_contact():
                    if var_contact.get()=="":
                        messagebox.showwarning("Error","enter contact",parent=f7)
                    else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                        my_cursor=conn.cursor()
                        query="select name from customer where mobile=%s"
                        value=(var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Not Found",parent=f7)
                        else:
                            conn.commit()
                            conn.close()
                            frame4=Frame(f7,bd=4,relief=RIDGE)
                            frame4.place(x=450,y=40,width=247,height=230)
                            lbl1=Label(frame4,text="Name", font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl1.grid(row=0,column=0,pady=1)
                            lbl2=Label(frame4,text=row, font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl2.grid(row=0,column=1,pady=1)
                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            query="select email from customer where mobile=%s"
                            value=(var_contact.get(),)
                            my_cursor.execute(query,value)
                            row=my_cursor.fetchone()
                            lbl1=Label(frame4,text="Email", font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl1.grid(row=1,column=0,pady=1)
                            lbl2=Label(frame4,text=row, font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl2.grid(row=1,column=1,pady=1)
                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            query="select gender from customer where mobile=%s"
                            value=(var_contact.get(),)
                            my_cursor.execute(query,value)
                            row=my_cursor.fetchone()
                            lbl1=Label(frame4,text="Gender", font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl1.grid(row=2,column=0,pady=1)
                            lbl2=Label(frame4,text=row, font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl2.grid(row=2,column=1,pady=1)
                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            query="select address from customer where mobile=%s"
                            value=(var_contact.get(),)
                            my_cursor.execute(query,value)
                            row=my_cursor.fetchone()
                            lbl1=Label(frame4,text="Address", font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl1.grid(row=3,column=0,pady=1)
                            lbl2=Label(frame4,text=row, font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl2.grid(row=3,column=1,pady=1)
                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            query="select nationality from customer where mobile=%s"
                            value=(var_contact.get(),)
                            my_cursor.execute(query,value)
                            row=my_cursor.fetchone()
                            lbl1=Label(frame4,text="nationality", font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl1.grid(row=4,column=0,pady=1)
                            lbl2=Label(frame4,text=row, font=("times new roman",14,"bold"),fg="brown",bd=4)
                            lbl2.grid(row=4,column=1,pady=1)
                    #--------------END OF FETCH DATA FUNCTION----------------
                def add_info():
                    if ((var_contact.get()=="")or (var_in.get()=="")):
                        messagebox.showwarning("error","enter required fields",parent=f7)
                    else:
                        try:

                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    var_contact.get(),
                                                                                    var_in.get(),
                                                                                    var_out.get(),
                                                                                    var_type.get(),
                                                                                    var_avail.get(),
                                                                                    var_food.get(),
                                                                                    var_days.get()
                                                                                    
                                                                                    
                                                                                                ))
                            conn.commit()
                            fetch_data()

                            
                            
                            conn.close()
                            messagebox.showinfo("SUCCESS","DETAILS ADDED",parent=f7)
                        except Exception as es:
                            messagebox.showwarning("warning",f"wrong:{str(es)}",parent=f7)
                def fetch_data():
                    conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select *from room")
                    rows=my_cursor.fetchall()
                    for i in rows:
                        tree1.insert("",END,values=i)
                    conn.commit()
                    conn.close()
                def get_cursor(event=""):
                    cursor_row=tree1.focus()
                    content=tree1.item(cursor_row)
                    row=content["values"]
                
                    var_contact.set(row[1])
                    var_in.set(row[2])
                    var_out.set(row[3])
                    var_type.set(row[4])
                    var_avail.set(row[5])
                    var_food.set(row[6])
                    var_days.set(row[7])
                def update():
                    if ((var_contact.get()=="")or (var_avail.get()=="")):
                        messagebox.showwarning("error","enter required fields",parent=f7)
                    else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update room set check_in=%s,check_out=%s,type=%s,available=%s,food=%s,days=%s where contact=%s",(
                                                                                                    
                                                                                                    
                                                                                                    var_in.get(),
                                                                                                    var_out.get(),
                                                                                                    var_type.get(),
                                                                                                    var_avail.get(),
                                                                                                    var_food.get(),
                                                                                                    var_days.get(),
                                                                                                    var_contact.get()
                                                                                                    
                        ))

                        conn.commit()
                        fetch_data()
                        conn.close()
                        messagebox.showinfo("SUCCESS","UPDATED",parent=f7)
                def Delete():
                    Delete=messagebox.askyesno("rms","DO YOU WANT TO DELETE?",parent=f7)
                    
                    if Delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                        my_cursor=conn.cursor()
                        query="delete from room where contact=%s"
                        value=(var_contact.get(),)
                        my_cursor.execute(query,value)
                
                    else:
                        if not Delete:
                            return
                    conn.commit()
                    fetch_data()
                    conn.close()
                def total():
                    in_date=var_in.get()
                    out_date=var_out.get()
                    in_date=datetime.strptime(in_date,"%d/%m/%Y")
                    out_date=datetime.strptime(out_date,"%d/%m/%Y")
                    var_days.set(abs(out_date-in_date).days)
                    if (var_food.get()=="lunch" and var_type.get()=="single"):
                        q1=float(300)
                        q2=float(400)
                        q3=float(var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs."+str("%.2f"%((q5)*0.1))
                        sub="Rs."+str("%.2f"%((q5)))
                        T="Rs."+str("%.2f"%(q5+((q5)*0.1)))
                        var_paidtax.set(tax)
                        var_sub.set(sub)
                        var_total.set(T)
                    elif (var_food.get()=="lunch" and var_type.get()=="double"):
                        q1=float(300)
                        q2=float(400)
                        q3=float(var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs."+str("%.2f"%((q5)*0.8))
                        sub="Rs."+str("%.2f"%((q5)))
                        T="Rs."+str("%.2f"%(q5+((q5)*0.8)))
                        var_paidtax.set(tax)
                        var_sub.set(sub)
                        var_total.set(T)
                    elif (var_food.get()=="lunch" and var_type.get()=="luxury"):
                        q1=float(300)
                        q2=float(400)
                        q3=float(var_days.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs."+str("%.2f"%((q5)*0.12))
                        sub="Rs."+str("%.2f"%((q5)))
                        T="Rs."+str("%.2f"%(q5+((q5)*0.12)))
                        var_paidtax.set(tax)
                        var_sub.set(sub)
                        var_total.set(T)
                def search():
                    conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from room where " +str(search_var.get())+" LIKE '%"+str(text_search.get())+"%'")
                    rows=my_cursor.fetchall()
                    for i in rows:
                        tree1.insert("",END,values=i)
                        conn.commit()
                


                    
                                



                lbl=Label(f7,text="ROOM RESERVATION",font=("times new roman",20,BOLD),fg="brown",bg="gold",bd=10)
                lbl.place(x=0,y=0,width=1550,height=40)
                frame2=Frame(f7,bd=4,relief=RIDGE)
                frame2.place(x=0,y=60,width=450,height=520)
                lbl1=Label(frame2,text="Contact", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=0,column=0,pady=1)
                entry_contact=ttk.Entry(frame2,textvariable=var_contact,width=15,font=("times new roman",15))
                entry_contact.grid(row=0,column=1,sticky=W)
                lbl1=Label(frame2,text="check_in_date",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=1,column=0,pady=1)
                entry1=ttk.Entry(frame2,width=20,textvariable=var_in,font=("times new roman",15))
                entry1.grid(row=1,column=1)
                lbl1=Label(frame2,text="check_out_date",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=2,column=0,pady=1)
                entry2=ttk.Entry(frame2,width=20,textvariable=var_out,font=("times new roman",15))
                entry2.grid(row=2,column=1)
                lbl1=Label(frame2,text="room type",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=3,column=0,pady=1)
                conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select room_type from booking")
                ide=my_cursor.fetchall()
                combo=ttk.Combobox(frame2,textvariable=var_type,width=20,font=("times new roman",15))
                combo["value"]=ide
                combo.current(0)
                combo.grid(row=3,column=1)
                lbl1=Label(frame2,text="available room",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=4,column=0,pady=1)
                #entry3=ttk.Entry(frame2,textvariable=var_avail,width=20,font=("times new roman",15))
                #entry3.grid(row=4,column=1)
                conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("select room_no from booking")
                rows=my_cursor.fetchall()
                combo=ttk.Combobox(frame2,textvariable=var_avail,width=20,font=("times new roman",15))
                combo["value"]=rows
                combo.current(0)
                combo.grid(row=4,column=1)

                lbl1=Label(frame2,text="no of days",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=5,column=0,pady=1)
                entry4=ttk.Entry(frame2,textvariable=var_days,width=20,font=("times new roman",15))
                entry4.grid(row=5,column=1)
                lbl1=Label(frame2,text="Food Type",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=6,column=0,pady=1)
                entry5=ttk.Entry(frame2,textvariable=var_food,width=20,font=("times new roman",15))
                entry5.grid(row=6,column=1)
                lbl1=Label(frame2,text="paid tax",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=7,column=0,pady=1)
                entry5=ttk.Entry(frame2,textvariable=var_paidtax,width=20,font=("times new roman",15))
                entry5.grid(row=7,column=1)
                lbl1=Label(frame2,text="sub total",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=8,column=0,pady=1)
                entry6=ttk.Entry(frame2,textvariable=var_sub,width=20,font=("times new roman",15))
                entry6.grid(row=8,column=1)
                lbl1=Label(frame2,text="total cost",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=9,column=0,pady=1)
                entry7=ttk.Entry(frame2,textvariable=var_total,width=20,font=("times new roman",15))
                entry7.grid(row=9,column=1)
                fetch=Button(frame2,text="FETCH DATA",command=fetch_contact, font=("times new roman",8,BOLD),width=12,bg="blue",fg="black",bd=4,cursor="hand1")
                fetch.grid(row=0,column=2,)
                fetch=Button(frame2,text="BILL",command=total, font=("times new roman",8,BOLD),width=12,bg="blue",fg="black",bd=4,cursor="hand1")
                fetch.grid(row=10,column=1,)
                frame3=Frame(frame2,bd=4,relief=RIDGE)
                frame3.place(x=9,y=400,width=367,height=60)
                btn =Button(frame3,text="ADD",command=add_info, font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",)
                btn.grid(row=0,column=0,)
                btn =Button(frame3,text="UPDATE",command=update, font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1")
                btn.grid(row=0,column=1,padx=2)
                btn =Button(frame3,text="DELETE",command=Delete,font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",)
                btn.grid(row=0,column=2,padx=2)
                frame6=Frame(f7,bd=4,relief=RIDGE)
                frame6.place(x=450,y=270,width=1000,height=400)
                lbl1=Label(frame6,text="SEARCH BY:",font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=0,column=0,pady=1)
                search_var=StringVar()

                combo1=ttk.Combobox(frame6,textvariable=search_var, width=20,font=("times new roman",15),state="read only")
                combo1["value"]=("contact")
                combo1.current(0)
                combo1.grid(row=0,column=1)
                text_search=StringVar()

                entry_add=ttk.Entry(frame6,textvariable=text_search,width=15,font=("times new roman",15,))
                entry_add.grid(row=0,column=2,padx=2)
                btn =Button(frame6,text="SEARCH",command=search, font=("times new roman",10),width=8,bg="blue",fg="black",bd=4,cursor="hand1")
                btn .grid(row=0,column=3,padx=2)
                btn =Button(frame6,text="SHOW ALL",command=fetch_data, font=("times new roman",10),width=8,bg="blue",fg="black",bd=4,cursor="hand1")
                btn .grid(row=0,column=4,padx=2)
                frame7=Frame(frame6,bd=4,relief=RIDGE)
                frame7.place(x=0,y=80,width=800,height=500)
                    
                sbb_y=Scrollbar(frame7,orient='vertical')
                sbb_y.pack(side=RIGHT,fill="y")
                sbb_x=Scrollbar(frame7,orient='horizontal')
                sbb_x.pack(side=BOTTOM,fill="x")
                tree1 = ttk.Treeview(frame7,height=30,column=("c1", "c2","c3","c4","c5","c6","c7"), show='headings',xscrollcommand=sbb_x.set,yscrollcommand=sbb_y.set)
            
                tree1.column("# 1", anchor=CENTER)
                tree1.heading("# 1", text="Contact")
                tree1.column("# 2", anchor=CENTER)
                tree1.heading("# 2", text="Check_in_date")
                tree1.column("# 3", anchor=CENTER)
                tree1.heading("# 3", text="Check_out_date")
                tree1.column("# 4", anchor=CENTER)
                tree1.heading("# 4", text="Room Type")
                tree1.column("# 5", anchor=CENTER)
                tree1.heading("# 5", text="Available room")
                tree1.column("# 6", anchor=CENTER)
                tree1.heading("# 6", text="Food Type")
                tree1.column("# 7", anchor=CENTER)
                tree1.heading("# 7", text="Days")
                
                tree1.pack()
                tree1.bind("<ButtonRelease-1>",get_cursor)
                fetch_data()
                
                
            
                sbb_x.config(command=tree1.xview)
                sbb_y.config(command=tree1.yview)
            def details():
                f8=Toplevel(win)
                f8.geometry("1550x600+0+265")
                lbl=Label(f8,text="DETAILS",font=("times new roman",20,BOLD),fg="brown",bg="gold",bd=10)
                lbl.place(x=0,y=0,width=1550,height=40)
                var_floor=StringVar()
                var_roomno=StringVar()
                var_type=StringVar()
                def add_info():
                    if ((var_floor.get()=="") or (var_type.get()=="")):
                        messagebox.showwarning("error","enter required fields",parent=f8)
                    else:
                    
                        try:

                            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into booking values(%s,%s,%s)",(
                                                                                    var_floor.get(),
                                                                                    var_roomno.get(),
                                                                                    var_type.get()
                                                                                    
                                                                                    
                                                                                    
                                                                                                ))
                            conn.commit()
                            fetch_data()
                            conn.close()
                            messagebox.showinfo("SUCCESS","ADDED",parent=f8)
                        except Exception as es:
                            messagebox.showwarning("warning",f"wrong:{str(es)}",parent=f8)
                def fetch_data():
                    conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select *from booking")
                    rows=my_cursor.fetchall()
                    for i in rows:
                        tree1.insert("",END,values=i)
                    conn.commit()
                    conn.close()
                def get_cursor(event=""):
                    cursor_row=tree1.focus()
                    content=tree1.item(cursor_row)
                    row=content["values"]
                
                    
                    var_floor.set(row[0])
                    var_roomno.set(row[1])
                    var_type.set(row[2])
                def update():
                    if ((var_floor.get()=="")):
                        messagebox.showwarning("error","enter required fields",parent=f8)
                    else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update booking set floor=%s,room_type=%s where room_no=%s",(
                                                                                                    
                                                                                                    
                                                                                                    var_floor.get(),
                                                                                                    var_type.get(),
                                                                                                    var_roomno.get()
                                                                                                    
                        ))

                        conn.commit()
                        fetch_data()
                        conn.close()
                        messagebox.showinfo("SUCCESS","UPDATED",parent=f8)
                def Delete():
                    Delete=messagebox.askyesno("rms","DO YOU WANT TO DELETE?",parent=f8)
                    
                    if Delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
                        my_cursor=conn.cursor()
                        query="delete from booking where room_no=%s"
                        value=(var_roomno.get(),)
                        my_cursor.execute(query,value)
                
                    else:
                        if not Delete:
                            return
                    conn.commit()
                    fetch_data()
                    conn.close()
                    
                frame2=Frame(f8,bd=4,relief=RIDGE)
                frame2.place(x=0,y=60,width=450,height=520)
                lbl1=Label(frame2,text="Floor", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=0,column=0,pady=1)
                entry_add=ttk.Entry(frame2,textvariable=var_floor,width=15,font=("times new roman",15,))
                entry_add.grid(row=0,column=1)
                lbl1=Label(frame2,text="Room No", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=1,column=0,pady=1)
                entry_1=ttk.Entry(frame2,textvariable=var_roomno,width=15,font=("times new roman",15))
                entry_1.grid(row=1,column=1,sticky=W)
                lbl1=Label(frame2,text="Room Type", font=("times new roman",14,"bold"),fg="brown",bd=4)
                lbl1.grid(row=2,column=0,pady=1)
                entry_2=ttk.Entry(frame2,textvariable=var_type, width=15,font=("times new roman",15))
                entry_2.grid(row=2,column=1,sticky=W)
                frame3=Frame(frame2,bd=4,relief=RIDGE)
                frame3.place(x=9,y=400,width=367,height=60)
                btn =Button(frame3,text="ADD",command=add_info,font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",)
                btn.grid(row=0,column=0,)
                btn =Button(frame3,text="UPDATE",command=update, font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1")
                btn.grid(row=0,column=1,padx=2)
                btn =Button(frame3,text="DELETE",command=Delete, font=("times new roman",10,),width=15,bg="blue",fg="black",bd=4,cursor="hand1",)
                btn.grid(row=0,column=2,padx=2)
                #-------table frame--------------------------
                frame4=Frame(f8,bd=4,relief=RIDGE)
                frame4.place(x=460,y=70,width=500,height=300)
                sbb_y=Scrollbar(frame4,orient='vertical')
                sbb_y.pack(side=RIGHT,fill="y")
                sbb_x=Scrollbar(frame4,orient='horizontal')
                sbb_x.pack(side=BOTTOM,fill="x")
                tree1 = ttk.Treeview(frame4,height=30,column=("c1", "c2","c3"), show='headings',xscrollcommand=sbb_x.set,yscrollcommand=sbb_y.set)
            
                tree1.column("# 1", anchor=CENTER)
                tree1.heading("# 1", text="Floor")
                tree1.column("# 2", anchor=CENTER)
                tree1.heading("# 2", text="Room No")
                tree1.column("# 3", anchor=CENTER)
                tree1.heading("# 3", text="Room Type")
                
                tree1.pack()
                tree1.bind("<ButtonRelease-1>",get_cursor)
                fetch_data()
                sbb_x.config(command=tree1.xview)
                sbb_y.config(command=tree1.yview)
            def logout():
                win.destroy()
                

                            
                            
                            

                
                
                
                
                
            
            cust_btn=Button(btn_frame,text="CUSTOMER",font=("times new roman",15,BOLD),width=50,bg="blue",fg="black",bd=4,cursor="hand1",command=customer)
            cust_btn.grid(row=0,column=0,pady=3,padx=2)
            #1
            room_btn=Button(btn_frame,text="ROOM RESERVATION",font=("times new roman",15,BOLD),width=50,bg="blue",fg="black",bd=4,cursor="hand1",command=reservation)
            room_btn.grid(row=1,column=0,pady=3,padx=2)
            #2
            details_btn=Button(btn_frame,text="DETAILS",command=details, font=("times new roman",15,BOLD),width=50,bg="blue",fg="black",bd=4,cursor="hand1")
            details_btn.grid(row=2,column=0,pady=3,padx=2,)
            #3
            
            
            logout_btn=Button(btn_frame,text="LOGOUT",command=logout, font=("times new roman",15,BOLD),width=50,bg="blue",fg="black",bd=4,cursor="hand1")
            logout_btn.grid(row=4,column=0,pady=3,padx=2)
                
            #add images at background
    
var1=StringVar()
var2=StringVar()
var_name=StringVar()
var_mobile=StringVar()
var_address=StringVar()
var1=StringVar()
var2=StringVar()
var_repass=StringVar()
var_check=IntVar()
def register():
    fr1=Toplevel(win)
    fr1.geometry("1550x600+0+265")
    
    lbl=Label(fr1,text="REGISTER HERE",font=("times new roman",30,BOLD),bg="gold",fg="brown",bd=10)
    lbl.place(x=0,y=0,width=1550,height=50)
    f5=Frame(fr1,bd=4,relief=RIDGE,bg="gold")
    f5.place(x=520,y=80,width=400,height=400)
    lbl1=Label(f5,text="Name",font=("times new roman",14,"bold"),fg="brown",bg="gold",bd=4)
    lbl1.grid(row=0,column=0,pady=5)
    entry_n=ttk.Entry(f5,textvariable=var_name ,width=20,font=("times new roman",15))
    entry_n.grid(row=0,column=1)
    lbl1=Label(f5,text="mobile",font=("times new roman",14,"bold"),fg="brown",bg="gold",bd=4)
    lbl1.grid(row=1,column=0,pady=5)
    entry_n=ttk.Entry(f5,textvariable=var_mobile,width=20,font=("times new roman",15))
    entry_n.grid(row=1,column=1)
    lbl1=Label(f5,text="address",font=("times new roman",14,"bold"),fg="brown",bg="gold",bd=4)
    lbl1.grid(row=2,column=0,pady=5)
    entry_n=ttk.Entry(f5,textvariable=var_address,width=20,font=("times new roman",15))
    entry_n.grid(row=2,column=1)
    lbl1=Label(f5,text="username",font=("times new roman",14,"bold"),fg="brown",bg="gold",bd=4)
    lbl1.grid(row=3,column=0,pady=5)
    entry_n=ttk.Entry(f5,textvariable=var1,width=20,font=("times new roman",15))
    entry_n.grid(row=3,column=1)
    lbl1=Label(f5,text="password",font=("times new roman",14,"bold"),fg="brown",bg="gold",bd=4)
    lbl1.grid(row=4,column=0,pady=5)
    entry_n=ttk.Entry(f5,textvariable=var2,width=20,font=("times new roman",15))
    entry_n.grid(row=4,column=1)
    lbl1=Label(f5,text=" Re-enter password",font=("times new roman",14,"bold"),fg="brown",bg="gold",bd=4)
    lbl1.grid(row=5,column=0,pady=5)
    entry_n=ttk.Entry(f5,textvariable=var_repass,width=20,font=("times new roman",15))
    entry_n.grid(row=5,column=1)
    check=Checkbutton(f5,variable=var_check, text="I agree the term and conditions",font=("times new roman",14,"bold"),fg="brown",bg="gold",bd=4,onvalue=1,offvalue=0)
    check.place(x=25,y=250)
    
    
    def register_data():
        if var_name.get()=="" or var_mobile.get()=="":
            messagebox.showwarning("error","enter required fields",parent=f5)
        elif var2.get()!=var_repass.get():
            messagebox.showwarning("error","both password must be same",parent=f5)
        elif var_check.get()==0:
            messagebox.showwarning("error","please agree with terms and conditions:",parent=f5)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pooja3010",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where mobile=%s")
            value=(var_mobile.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                 messagebox.showwarning("Error","user already exist",parent=f5)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
                                                                            var_name.get(),
                                                                            var_mobile.get(),
                                                                            var_address.get(),
                                                                            var1.get(),
                                                                            var2.get()

                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("SUCCESS","ADDED",parent=f5)


                                                                                                                                                                
                                                                                
                                                                                
                                                                                            
               
                        

    reg_btn=Button(f5,text="REGISTER NOW",font=("times new roman",12,BOLD),width=13,bg="blue",fg="black",command=register_data, bd=4,cursor="hand1")
    reg_btn.place(x=40,y=300)
    login_btn=Button(f5,text="LOGIN NOW",font=("times new roman",12,BOLD),width=13,bg="blue",fg="black",bd=4,cursor="hand1")
    login_btn.place(x=220,y=300)

        




    

f5=Frame(win,bd=4,relief=RIDGE,bg="gold")
f5.place(x=400,y=340,width=800,height=400)
lbl=Label(win,text="RESORT MANAGEMENT SYSTEM",font=("times new roman",30,BOLD),bg="gold",fg="brown")
lbl.place(x=0,y=0,width=1550,height=60)
lbl=Label(win,text="WELCOME",font=("times new roman",37,BOLD),bg="gold",fg="brown",bd=10)
lbl.place(x=0,y=243,width=1550,height=50)

load=Image.open("Resort.png")
img1=load.resize((1380,180))
render=ImageTk.PhotoImage(img1)
img=Label(win,image=render)
img.place(x=220,y=60)
load1=Image.open("resortlogo1.png")
img=load1.resize((220,180))
render1=ImageTk.PhotoImage(img)
img2=Label(win,image=render1)
img2.place(x=0,y=0)
#-----------------------------------ADDING LABLES--------------------------------------------------------
lbl=Label(f5,text="USERNAME",font=("times new roman",15,BOLD),fg="brown",bg="gold",bd=10)
lbl.place(x=90,y=50)
ent=Entry(f5,bg="lavender",fg="brown",font=("times new roman",15,),textvariable=var1)
ent.place(x=280,y=50,width=300,height=30)
lbl=Label(f5,text="PASSWORD",font=("times new roman",15,BOLD),fg="brown",bg="gold",bd=10)
lbl.place(x=90,y=100)
ent=Entry(f5,show="****",bg="lavender",fg="brown",font=("times new roman",15,),textvariable=var2)
ent.place(x=280,y=100,width=300,height=30)
b1=Button(f5,text="USER LOGIN",command=ulogin, fg="black",bg="blue",font=("times new roman",15,BOLD))
b1.place(x=140,y=250,width=200,height=40)
b2=Button(f5,text="ADMIN LOGIN",fg="black",bg="blue",font=("times new roman",15,BOLD),command=menu)
b2.place(x=440,y=250,width=200,height=40)
b2=Button(f5,text="New User register",fg="black",bg="blue",font=("times new roman",9,BOLD),command=register)
b2.place(x=100,y=320,width=100,height=20)
b2=Button(f5,text="Forgot Password",fg="black",bg="blue",font=("times new roman",9,BOLD))
b2.place(x=100,y=350,width=100,height=20)
win.mainloop()
