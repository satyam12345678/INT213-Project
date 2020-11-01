#import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import os
#sqlite3 connection
connect=sqlite3.connect("storedb.db")
c=connect.cursor()
#storing all ids
result=c.execute("SELECT id from inventory")
id=""
for r in result:
    id=id+str(r[0])+" "  
list_id = id.split(" ")
class Database:
    def __init__(self,root):
        
         self.root=root
         
         self.master = Frame(root,bg='#000000',width=1600,height=1200)
         self.master.place(x=0,y=0)
         
         self.heading=Label(self.master,text="Add in the databse",font=('arial 40 bold'),fg='#ebebeb',bg='#000000')
         self.heading.place(x=500,y=10)

         self.view_list=Button(self.master, text="View list", font=('arial 12 bold'), width=22, height=2, bg='#4f3961',fg='white',command=self.view_all)
         self.view_list.place(x=860, y=480)               

         #lables  for the window
         self.name_l=Label(self.master,text="Enter Product Name",font=('arial 18 bold'),fg='#ebebeb',bg='#000000')
         self.name_l.place(x=50,y=120+50)

         self.stock_l=Label(self.master,text="Enter Stocks",font=('arial 18 bold'),fg='#ebebeb',bg='#000000')
         self.stock_l.place(x=50,y=170+50)

         self.cp_l = Label(self.master, text="Enter Cost Price ", font=('arial 18 bold'),fg='#ebebeb',bg='#000000')
         self.cp_l.place(x=50, y=220+50)

         self.sp_l = Label(self.master, text="Enter Selling Price", font=('arial 18 bold'),fg='#ebebeb',bg='#000000')
         self.sp_l.place(x=50, y=270+50)

         self.id_l = Label(self.master, text="Enter ID", font=('arial 18 bold'),fg='#ebebeb',bg='#000000')
         self.id_l.place(x=50, y=70+50)

        #enteries for window

         self.name_e=Entry(self.master,width=25,font=('arial 18 bold'),bg='#ebebeb')
         self.name_e.place(x=380,y=120+50)

         self.stock_e = Entry(self.master, width=25, font=('arial 18 bold'),bg='#ebebeb')
         self.stock_e.place(x=380, y=170+50)

         self.cp_e = Entry(self.master, width=25, font=('arial 18 bold'),bg='#ebebeb')
         self.cp_e.place(x=380, y=220+50)

         self.sp_e = Entry(self.master, width=25, font=('arial 18 bold'),bg='#ebebeb')
         self.sp_e.place(x=380, y=270+50)

         self.id_e=Entry(self.master,width=25,font=('arial 18 bold'),bg='#ebebeb')
         self.id_e.place(x=380,y=70+50)

         #button to add to the database
         self.btn_add=Button(self.master,text='Add to Database',font=('arial 12 bold'),width=20,height=1,bg='#e6739f',fg='white',command=self.get_items)
         self.btn_add.place(x=550,y=330+50)

         self.btn_clear=Button(self.master,text="Clear All Fields",font=('arial 12 bold'),width=13,height=1,bg='#e6739f',fg='white',command=self.clear_all)
         self.btn_clear.place(x=350,y=330+50)
         
         self.result=c.execute("SELECT id from inventory")
         self.id=""
         for r in self.result:
             self.id=self.id+str(r[0])+" "  
         self.list_id = self.id.split(" ")
         
          #text box for the log
         self.tbBox=Text(self.master,width=60,height=18, font=('arial 12 bold'),bg='#000000',fg='#ebebeb')
         self.tbBox.place(x=850,y=70+50)
         self.tbBox.insert(END,"Existing IDs: "+"\n")
         for r in range(0,len(self.list_id)-1):
             self.tbBox.insert(END,(self.list_id[r])+"\t")
         

         self.root.bind('<Return>', self.get_items)
         self.root.bind('<Up>', self.clear_all)
         
         #exit button
         self.exit_btn=Button(self.master,text="Go Back",width=22,height=2,bg='#4f3961',fg='white',font=('arial 12 bold'),command=self.go_back)
         self.exit_btn.place(x=1155,y=480)
         
    #to close the window
    def go_back(self):
        self.root.destroy()    
        
    def view_all(self):
        os.system('python view_all.py')     

    def get_items(self):
        
       if self.id_e.get() in self.list_id or self.id_e.get() == '':
           tkinter.messagebox.showinfo("Error","ID empty or already in use.")
           self.clear_all()
           return None
    # get from entries
       self.idef = self.id_e.get() 
       self.name = self.name_e.get()
       self.stock = self.stock_e.get()
       self.cp = self.cp_e.get()
       self.sp = self.sp_e.get()

       if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
        tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
       else:
        sql = "INSERT INTO inventory (id, name, stock, cp, sp) VALUES(?,?,?,?,?)"
        c.execute(sql, (
        self.idef, self.name, self.stock, self.cp, self.sp))
        connect.commit()
        self.__init__(self.root)
        # textbox insert
        tkinter.messagebox.showinfo("Success", "Successfully added '"+ self.name + "' with code '"+ self.idef +"' to the database")


    def clear_all(self):
       self.id_e.delete(0,END) 
       self.name_e.delete(0, END)
       self.stock_e.delete(0, END)
       self.cp_e.delete(0, END)
       self.sp_e.delete(0, END)



root=Tk()
b=Database(root)

root.geometry("1366x768+0+0")
root.state('zoomed')
root.title("Add in the database")
root.mainloop()