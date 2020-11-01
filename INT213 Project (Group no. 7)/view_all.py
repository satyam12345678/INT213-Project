#import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
#sqlite3 connection
connect=sqlite3.connect("storedb.db")
c=connect.cursor()
#storing all ids
result=c.execute("SELECT id from inventory")
id=""
for r in result:
    id=id+str(r[0])+" "  
list_id = id.split(" ")
#global variables
get_id=[]
get_name=[]
get_stock=[]
get_cp=[]
get_sp=[]

class Database:
    def __init__(self,root):
        self.root = root
        
        self.master = Canvas(root,bg='#000000',width=1600,height=1200)
        self.master.place(x=0,y=0)
        
        #components 
        self.heading=Label(self.master,text="List View",font=('arial 40 bold'),fg='#ebebeb',bg='#000000')
        self.heading.place(x=650,y=10)
        
        self.id_e = Label(self.master, text="ID", font=('arial 25 bold'),fg='#ebebeb',bg='#000000')
        self.id_e.place(x=100,y=150)
        
        self.id_e = Label(self.master, text="Name", font=('arial 25 bold'),fg='#ebebeb',bg='#000000')
        self.id_e.place(x=300,y=150)
        
        self.id_e = Label(self.master, text="Stock", font=('arial 25 bold'),fg='#ebebeb',bg='#000000')
        self.id_e.place(x=600,y=150)
        
        self.id_e = Label(self.master, text="Cost Price", font=('arial 25 bold'),fg='#ebebeb',bg='#000000')
        self.id_e.place(x=900,y=150)
        
        self.id_e = Label(self.master, text="Sale Price", font=('arial 25 bold'),fg='#ebebeb',bg='#000000')
        self.id_e.place(x=1250,y=150)
        
        self.y_index=200
        
        #storing all the details of every prodct
        query="SELECT * FROM inventory WHERE id=?"
        for i in range(0,len(list_id)-1):
            result=c.execute(query,(list_id[i],))
            for self.r in result:
                get_id.append(self.r[0])
                get_name.append(self.r[1])
                get_stock.append(self.r[2])
                get_cp.append(self.r[3])
                get_sp.append(self.r[4])   
                
        #printing all the details        
        for i in range(0,len(list_id)-1):
                self.tempid=Label(self.master,text=str(get_id[i]),font=('arial 18 bold'), bg='#ffffff', fg='#000000')
                self.tempid.place(x=100,y=self.y_index)
                
                self.tempname = Label(self.master, text=str(get_name[i]), font=('arial 18 bold'), fg='#ebebeb',bg='#000000')
                self.tempname.place(x=320, y=self.y_index)
                
                self.tempstock = Label(self.master, text=str(get_stock[i]), font=('arial 18 bold'), fg='#ebebeb',bg='#000000')
                self.tempstock.place(x=630, y=self.y_index)
                
                self.tempcp = Label(self.master, text=str(get_cp[i]), font=('arial 18 bold'), fg='#ebebeb',bg='#000000')
                self.tempcp.place(x=950, y=self.y_index)
                
                self.tempsp = Label(self.master, text=str(get_sp[i]), font=('arial 18 bold'), fg='#ebebeb',bg='#000000')
                self.tempsp.place(x=1320, y=self.y_index)
                
                self.y_index+=40
        #exit button
        self.exit_btn=Button(self.master,text="Go Back",width=22,height=2,bg='#4f3961',fg='white',font=('arial 12 bold'),command=self.go_back)
        self.exit_btn.place(x=1155,y=self.y_index + 30)
        #clearing the global variables
        get_id.clear()
        get_name.clear()
        get_stock.clear()
        get_cp.clear()
        get_sp.clear()
    #to close the window    
    def go_back(self):
        self.root.destroy()


root=Tk()
b=Database(root)
root.geometry("1366x768+0+0")
root.state('zoomed')
root.title("View List")
root.mainloop()        