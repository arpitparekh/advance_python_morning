import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Walden0042$$",
    database="python_morning_ronak"
)

cursor = db.cursor()

def login():
  username = username_entry.get()
  password = password_entry.get()

  # Replace with your actual login logic
  if username == "user" and password == "password":
    messagebox.showinfo("Success", "Login successful!")
  else:
    messagebox.showerror("Error", "Invalid username or password!")

def register():
  username2 = username_entry_reg.get()
  email2 = email_entry_reg.get()



# Create the main window
root = tk.Tk()
root.title("Login/Register")

# Create frames for login and register sections
login_frame = tk.Frame(root)
register_frame = tk.Frame(root)

# Login section
username_label = tk.Label(login_frame, text="Username")
username_entry = tk.Entry(login_frame)

password_label = tk.Label(login_frame, text="Password")
password_entry = tk.Entry(login_frame, show="*")

remember_me_var = tk.BooleanVar()
remember_me_checkbox = tk.Checkbutton(login_frame, text="Remember Me", variable=remember_me_var)


lost_password_label = tk.Label(login_frame, text="Lost your password?", cursor="hand2") # Make label clickable

# Register section
username_label_reg = tk.Label(register_frame, text="Username")
username_entry_reg = tk.Entry(register_frame)

email_label_reg = tk.Label(register_frame, text="E-mail Address")
email_entry_reg = tk.Entry(register_frame)



# Layout elements
login_frame.pack(side="left", padx=20, pady=20)
register_frame.pack(side="right", padx=20, pady=20)

# Login frame layout
username_label.pack()
username_entry.pack()

password_label.pack()
password_entry.pack()

remember_me_checkbox.pack()


lost_password_label.pack()

# Register frame layout
username_label_reg.pack()
username_entry_reg.pack()

email_label_reg.pack()
email_entry_reg.pack()



def fatchData():
    cursor.execute("select * from registertable")
    result = cursor.fetchall()
    return result
def createTable():
    cursor.execute("create table if not exists registertable(id int, name varchar(255))")
def insertData(id,name):
    cursor.execute(f"insert into registertable(id,name) values ({id},'{name}')")
def updateData(id,name):
    cursor.execute(f"update registertable set name = '{name}' where id = {id}")

def login_button():
    id = login_button.get()
    name = login_button.get()

    insertData(id,name)
    db.commit()


def password():
    id = password.get()
    name = password.get()
    password(id,name)
    db.commit()




#Buttons

login_button = tk.Button(login_frame, text="Login", command=login).pack()
register_button = tk.Button(register_frame, text="Register", command=register).pack()


tree = ttk.Treeview(root,columns=("ID","Name","password"),show="headings")
tree.heading("ID",text="ID")
tree.heading("Name",text="Name")
tree.heading("password",text="password")

createTable()


root.mainloop()
