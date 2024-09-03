import mysql.connector
from tkinter import *
import tkinter.ttk as ttk

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Walden0042$$",
  database="python_morning_ronak",
)

cursor = db.cursor()

# database functions

def fetchData():
    cursor.execute("select * from newProduct")
    result = cursor.fetchall()
    return result

def createTable():
    cursor.execute("create table if not exists newProduct(id int, name varchar(255))")

def insertData(id,name):
    cursor.execute(f"insert into newProduct(id,name) values ({id},'{name}')")

def updateData(id,name):
    cursor.execute(f"update newProduct set name = '{name}' where id = {id}")

def deleteData(id):
    cursor.execute(f"delete from newProduct where id = {id} ")

def refreshTreeView():
  for row in tree.get_children():
    tree.delete(row)

  rows = fetchData()
  for row in rows:
    tree.insert("",END,values=row)

  db.commit()

# tkinter functions

def addProduct():
  insertData(entryID.get(),entryName.get())
  db.commit()
  refreshTreeView()


def updateProduct():
  updateData(entryID.get(),entryName.get())
  db.commit()
  refreshTreeView()

def deleteProduct():
  deleteData(entryID.get())
  db.commit()
  refreshTreeView()

root = Tk()
root.title("CRUD Operation")
root.geometry("500x400")

Label(root,text="ID : ").pack()
entryID = Entry(root)
entryID.pack()
Label(root,text="Name : ").pack()
entryName = Entry(root)
entryName.pack()

Button(root,text="Add Product",command=addProduct).pack()
Button(root,text="Update Product",command=updateProduct).pack()
Button(root,text="Delete Product",command=deleteProduct).pack()

tree = ttk.Treeview(root,columns=("id","name"),show="headings")
tree.heading("id",text="ID")
tree.heading("name",text="Name")
tree.pack(fill=BOTH,expand=True)

createTable()
refreshTreeView()

root.mainloop()
