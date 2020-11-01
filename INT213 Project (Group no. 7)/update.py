#import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import os

connect=sqlite3.connect("storedb.db")
c=connect.cursor()  
class Database:
    def __init__(self,root):
         self.root=root
         
         self.master = Frame(root,bg='#000000',width=1600,height=1200)
         self.master.place(x=0,y=0)
         
         self.heading=Label(self.master,text="Update to the databse",font=('arial 40 bold'),bg='#000000',fg='#ebebeb')
         self.heading.place(x=450,y=10)
         
         self.view_list=Button(self.master, text="View list", font=('arial 12 bold'), width=22, height=2, bg='#4f3961',fg='white',command=self.view_all)
         self.view_list.place(x=860, y=480)

         #label and entry for id
         self.id_le=Label(self.master,text="Enter ID",font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
         self.id_le.place(x=50,y=70+50)

         self.id_leb=Entry(self.master,font=('arial 18 bold'),width=10,bg='#ebebeb')
         self.id_leb.place(x=380,y=70+50)

         self.btn_search=Button(self.master,text="Search",font=('arial 15'),width=12,height=1,bg='#e6739f',fg='white',command=self.search)
         self.btn_search.place(x=550,y=70+45)

         #lables  for the window
         self.name_l=Label(self.master,text="Enter Product Name",font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
         self.name_l.place(x=50,y=120+55)

         self.stock_l=Label(self.master,text="Enter Stocks",font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
         self.stock_l.place(x=50,y=170+55)

         self.cp_l = Label(self.master, text="Enter Cost Price ", font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
         self.cp_l.place(x=50, y=220+55)

         self.sp_l = Label(self.master, text="Enter Selling Price", font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
         self.sp_l.place(x=50, y=270+55)

        #enteries for window

         self.name_e=Entry(self.master,width=25,font=('arial 18 bold'),bg='#ebebeb')
         self.name_e.place(x=380,y=120+55)

         self.stock_e = Entry(self.master, width=25, font=('arial 18 bold'),bg='#ebebeb')
         self.stock_e.place(x=380, y=170+55)

         self.cp_e = Entry(self.master, width=25, font=('arial 18 bold'),bg='#ebebeb')
         self.cp_e.place(x=380, y=220+55)

         self.sp_e = Entry(self.master, width=25, font=('arial 18 bold'),bg='#ebebeb')
         self.sp_e.place(x=380, y=270+55)

         #button to add to the database
         self.btn_add=Button(self.master,text='Update Database',font=('arial 12'),width=20,height=2,bg='#003f5c',fg='white',command=self.update)
         self.btn_add.place(x=520,y=320+55)

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
         
         #exit button
         self.exit_btn=Button(self.master,text="Go Back",width=22,height=2,bg='#4f3961',fg='white',font=('arial 12 bold'),command=self.go_back)
         self.exit_btn.place(x=1155,y=480)
    #to close the window     
    def go_back(self):
        self.root.destroy()
        
    def view_all(self):
        os.system('python view_all.py')    
        
    def search(self):
         if self.id_leb.get() not in self.list_id or self.id_leb.get() == '':
             tkinter.messagebox.showinfo("Error","ID is incorrect.")
             self.clear_all()
             return None
         sql = "SELECT * FROM inventory WHERE id=?"
         result = c.execute(sql, (self.id_leb.get(),))
         for r in result:
              self.n0 = r[0]  # id
              self.n1 = r[1]  # name
              self.n2 = r[2]  # stock
              self.n3 = r[3]  # cp
              self.n4 = r[4]  # sp
         connect.commit()

          #inster into the enteries to update
         self.name_e.delete(0,END)
         self.name_e.insert(0, str(self.n1))

         self.stock_e.delete(0, END)
         self.stock_e.insert(0, str(self.n2))

         self.cp_e.delete(0, END)
         self.cp_e.insert(0, str(self.n3))

         self.sp_e.delete(0, END)
         self.sp_e.insert(0, str(self.n4))
         
    def clear_all(self):
         self.id_leb.delete(0,END)
         self.name_e.delete(0, END)
         self.stock_e.delete(0, END)
         self.cp_e.delete(0, END)
         self.sp_e.delete(0, END)          

    def update(self):
          self.u1 = self.name_e.get()
          self.u2 = self.stock_e.get()
          self.u3 = self.cp_e.get()
          self.u4 = self.sp_e.get()


          query="UPDATE  inventory SET name=?,stock=?,cp=?,sp=?  WHERE id=?"
          c.execute(query,(self.u1,self.u2,self.u3,self.u4,self.id_leb.get()))
          self.clear_all()
          connect.commit()
          self.__init__(self.root)
          tkinter.messagebox.showinfo("Success","Updated '" + str(self.n1) + "' database with code '" + str(self.n0) + "' successfully")

        

root=Tk()
b=Database(root)
root.geometry("1366x768+0+0")
root.state('zoomed')
root.title("Update to the database")
root.mainloop()