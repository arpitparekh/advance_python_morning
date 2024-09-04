from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
import tkinter.messagebox as messagebox


# database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Walden0042$$",
  database="python_morning_ronak",
)
cursor = db.cursor()

def fetchData():
    cursor.execute("select * from userLogin")
    result = cursor.fetchall()
    return result

def createTable():
    cursor.execute("create table if not exists userLogin(id int primary key AUTO_INCREMENT, username varchar(255),email varchar(255),password varchar(255))")

def insertData(username,email,password):
    cursor.execute(f"insert into userLogin(username,email,password) values ('{username}','{email}','{password}')")

def checkData(username,password):
    cursor.execute(f"select * from userLogin where username = '{username}' and password = '{password}'")
    result = cursor.fetchall()
    return result

def login():
    username = username_entry.get()
    password = password_entry.get()
    result = checkData(username,password)

    if result:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

def register():
    username = username_entry_register.get()
    email = email_entry_register.get()
    password = password_entry_register.get()

    insertData(username,email,password)
    refreshTreeView()

def refreshTreeView():
  for row in tree.get_children():
    tree.delete(row)

  rows = fetchData()
  for row in rows:
    tree.insert("",END,values=row)

  db.commit()

# Create the main window
window = Tk()
window.title("HOME > Login & Register")

# Create the login frame
login_frame = Frame(window)
login_frame.pack(side=LEFT, padx=20, pady=20)

# Login Label
login_label = Label(login_frame, text="Login", font=("Arial", 16, "bold"))
login_label.pack(pady=10)

# Username Label
username_label = Label(login_frame, text="Username:")
username_label.pack()

# Username Entry
userEntryFrame = Frame(login_frame)
userEntryFrame.pack()

# image = PhotoImage(file="img.png", width=70, height=70)
# image_label = Label(userEntryFrame, image=image)
# image_label.pack(side="left", padx=5)

username_entry = Entry(userEntryFrame)
username_entry.pack(side="left", padx=5)

# Password Label
password_label = Label(login_frame, text="Password:")
password_label.pack()

# Password Entry
password_entry = Entry(login_frame, show="*")
password_entry.pack()

# Login Button
login_button = Button(login_frame, text="Login", command=login)
login_button.pack(pady=10)

# # Lost Password Link
# lost_password_link = Label(login_frame, text="Lost your password?", fg="blue", cursor="hand2")
# lost_password_link.pack()

# Create the register frame
register_frame = Frame(window)
register_frame.pack(side=RIGHT, padx=20, pady=20)

# Register Label
register_label = Label(register_frame, text="Register", font=("Arial", 16, "bold"))
register_label.pack(pady=15)

# Username Label
username_label_register = Label(register_frame, text="Username:")
username_label_register.pack()

# Username Entry
username_entry_register = Entry(register_frame)
username_entry_register.pack()

# Email Label
email_label_register = Label(register_frame, text="E-mail Address:")
email_label_register.pack()

# Email Entry
email_entry_register = Entry(register_frame)
email_entry_register.pack()

password_label_register = Label(register_frame, text="Password:")
password_label_register.pack()

password_entry_register = Entry(register_frame)
password_entry_register.pack()

# Register Button
register_button = Button(register_frame, text="Register", command=register)
register_button.pack(pady=10)

style = ttk.Style()
style.configure("Treeview", rowheight=25, borderwidth=1, relief="solid")
style.map("Treeview", background=[('selected', 'blue')])


tree = ttk.Treeview(window,columns=("id","username","email","password"),show="headings")
tree.heading("id",text="ID")
tree.heading("username",text="Username")
tree.heading("email",text="Email")
tree.heading("password",text="Password")

tree.pack(fill=BOTH,expand=True)

createTable()
refreshTreeView()


window.mainloop()
