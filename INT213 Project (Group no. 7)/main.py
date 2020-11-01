#import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
#sqlite3 connection
connect=sqlite3.connect("storedb.db")
c=connect.cursor()

date=datetime.datetime.now().date()
#temporary list like sessions
products_list=[]
product_price=[]
product_quantity=[]
product_id=[]

class Application:
    def __init__(self,master):
        self.master=master
        
        self.left=Frame(master,width=768,height=1200,bg='#000000')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=767, height=1200, bg='#4f3961')
        self.right.pack(side=RIGHT)

        #components
        self.heading=Label(self.left,text="SnS Store",font=('arial 40 bold'),bg='#000000',fg='#ebebeb')
        self.heading.place(x=10,y=10)
        
        self.view_list=Button(self.left, text="View list", font=('arial 18 bold'), width=15, height=1, bg='#4f3961',fg='white',command=self.view_all)
        self.view_list.place(x=520, y=15)

        self.date_l=Label(self.right,text="Today's Date: "+str(date),font=('arial 16 bold'),bg='#4f3961',fg='#ffffff')
        self.date_l.place(x=10,y=10)

        #invoice printing
        self.tproduct=Label(self.right,text="Products",font=('arial 20 bold'),bg='#4f3961',fg='#ffffff')
        self.tproduct.place(x=50,y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 20 bold'), bg='#4f3961', fg='#ffffff')
        self.tquantity.place(x=320, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 20 bold'), bg='#4f3961', fg='#ffffff')
        self.tamount.place(x=590, y=60)

        #enter stuff
        self.enterid=Label(self.left,text="Enter Product's ID",font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
        self.enterid.place(x=10,y=100)


        self.enteride=Entry(self.left,width=25,font=('arial 18 bold'),bg='#ebebeb')
        self.enteride.place(x=230,y=100)
        self.enteride.focus()

        #button
        self.search_btn=Button(self.left,text="Search",font=('arial 12 bold'),width=16,height=1,bg='#e6739f',fg='#ffffff',command=self.right_panel)
        self.search_btn.place(x=580,y=100)
        #fill it later by the fuction right_panel

        self.productname=Label(self.left,text="",font=('arial 27 bold'),bg='#000000',fg='#ebebeb')
        self.productname.place(x=10,y=250)

        self.pprice = Label(self.left, text="", font=('arial 27 bold'), bg='#000000', fg='#ebebeb')
        self.pprice.place(x=10, y=290)

        #total label
        self.total_l=Label(self.right,text="",font=('arial 40 bold'),bg='#4f3961',fg='#ffffff')
        self.total_l.place(x=10,y=740)
        
        #update / add / delete button
        self.update_btn=Button(self.left,text="Update",font=('arial 12 bold'),width=18,height=1,bg="#e6739f",fg='#ffffff',command=self.update_db)
        self.update_btn.place(x=40,y=750)
        
        self.add_btn=Button(self.left,text="Add",font=('arial 12 bold'),width=18,height=1,bg="#e6739f",fg='#ffffff',command=self.add_db)
        self.add_btn.place(x=290,y=750)
        
        self.del_btn=Button(self.left,text="Delete",font=('arial 12 bold'),width=18,height=1,bg="#e6739f",fg='#ffffff',command=self.del_db)
        self.del_btn.place(x=530,y=750)
        
        #self.refresh = Button()
        
        self.result=c.execute("SELECT id from inventory")
        self.id=""
        for r in self.result:
            self.id=self.id+str(r[0])+" "  
        self.list_id = self.id.split(" ") 
    
    #to open "update to db" window
    def update_db(self):
        os.system('python update.py')
    
    #to open "add to db" window    
    def add_db(self):
        os.system('python add_to_db.py')
    
    #to open "delete from db" window
    def del_db(self):
        os.system('python delete.py')
    
    #to open "list view" window    
    def view_all(self):
        os.system('python view_all.py')
        
    def right_panel(self):
        self.get_id=self.enteride.get()
        if self.get_id not in self.list_id or self.get_id == '':
             tkinter.messagebox.showinfo("Error","ID is incorrect.")
             self.clear_all()
             return None
        #get the product info with that id and fill i the labels above
        query="SELECT * FROM inventory WHERE id=?"
        result=c.execute(query,(self.get_id,))
        for self.r in result:
            self.get_id=self.r[0]
            self.get_name=self.r[1]
            self.get_price=self.r[4]
            self.get_stock=self.r[2]
        self.productname.configure(text="Product's Name: " +str(self.get_name))
        self.pprice.configure(text="Price: Rs. "+str(self.get_price))


        #craete the quantity and the discount label
        self.quantity_l=Label(self.left,text="Enter Quantity",font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
        self.quantity_l.place(x=10,y=370)

        self.quantity_e=Entry(self.left,width=25,font=('arial 18 bold'),bg='#ebebeb')
        self.quantity_e.place(x=200,y=370)
        self.quantity_e.focus()

        #discount
        self.discount_l = Label(self.left, text="Enter Discount", font=('arial 18 bold'), bg='#000000',fg='#ebebeb')
        self.discount_l.place(x=10, y=410)


        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='#ebebeb')
        self.discount_e.place(x=200, y=410)
        self.discount_e.insert(END,0)


        #add to cart button
        self.add_to_cart_btn = Button(self.left, text="Add to Cart", width=22, height=2, bg='#e6739f',command=self.add_to_cart)
        self.add_to_cart_btn.place(x=550, y=405)

        #generate bill and change
        self.change_l=Label(self.left,text="Given Amount",font=('arial 18 bold'),bg='#000000',fg='#ebebeb')
        self.change_l.place(x=10,y=550)

        self.change_e=Entry(self.left,width=25,font=('arial 18 bold'),bg='#ebebeb')
        self.change_e.place(x=200,y=550)

        self.change_btn= Button(self.left, text="Calculate Change", width=22, height=2, bg='#e6739f',command=self.change_func)
        self.change_btn.place(x=550, y=545)

        #generate bill button
        self.bill_btn = Button(self.left, text="Generate Bill",font=("arial 18 bold"), width=45, height=1, bg='#4f3961',fg='white',command=self.generate_bill)
        self.bill_btn.place(x=40, y=640)

    def add_to_cart(self):
        self.quantity_value=int(self.quantity_e.get())
        if  self .quantity_value >int(self.get_stock):
            tkinter.messagebox.showinfo("Error","Don't have much stocks.")
        else:
            #calculate the price first
            self.final_price=(float(self.quantity_value) * float(self.get_price))-(float(self.discount_e.get()))
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index=0
            self.y_index=120
            self.counter=0
            #right list
            for self.p in products_list:
                self.tempname=Label(self.right,text="# "+str(products_list[self.counter]),font=('arial 15 bold'),bg='#4f3961',fg='#ffffff')
                self.tempname.place(x=60,y=self.y_index)
                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 15 bold'), bg='#4f3961', fg='#ffffff')
                self.tempqt.place(x=370, y=self.y_index)
                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 15 bold'), bg='#4f3961', fg='#ffffff')
                self.tempprice.place(x=610, y=self.y_index)

                self.y_index+=40
                self.counter+=1


                #total confugure
                self.total_l.configure(text="Total : Rs. "+str(sum(product_price)))
                #delete
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()
                #autofocus to the enter id
                self.enteride.focus()
                self.enteride.delete(0,END)
    
    #calculates change        
    def change_func(self):
        self.amount_given=float(self.change_e.get())
        self.our_total=float(sum(product_price))

        self.to_give=self.amount_given-self.our_total

        #label change
        self.c_amount=Label(self.left,text="Change: Rs. "+str(self.to_give),font=('arial 18 bold'),fg='#e6739f',bg='#000000')
        self.c_amount.place(x=10 ,y=600)

    def generate_bill(self):
        self.x=0
        initial="SELECT * FROM inventory WHERE id=?"
        result=c.execute(initial,(product_id[self.x],))
        for r in result:
            self.old_stock=r[2]
        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock=int(self.old_stock) - int(product_quantity[self.x])
            #updating the stock
            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql,(self.new_stock,product_id[self.x]))
            connect.commit()

            #inster into transcation
            sql2="INSERT INTO transactions (product_name,quantity,amount,date) VALUES(?,?,?,?)"
            c.execute(sql2,(products_list[self.x],product_quantity[self.x],product_price[self.x],date))
            connect.commit()
            self.x+=1
        if self.amount_given < self.our_total:
            tkinter.messagebox.showinfo("Error","Less money given")
        else:    
            tkinter.messagebox.showinfo("success","Bill generated successfully")
        self.master.destroy()
        os.system('python main.py')
        #os.system('python bill.py')
        
    #clears all the entries
    def clear_all(self):
        self.enteride.delete(0,END)
        
        
root=Tk()
b=Application(root)
root.geometry("1366x768+0+0")
root.state('zoomed')
root.title("Inventory Mgmt.")
root.mainloop()