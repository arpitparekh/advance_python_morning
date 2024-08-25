from tkinter import *
from tkinter.messagebox import *

root = Tk()  # base widgets
root.geometry("440x400")
root.title("Screen 1")
root.resizable(False,False)

formFrame = Frame(root,padx=5,pady=5)
formFrame.place(x=10,y=10)

label = Label(formFrame,text="Firstname")
label.pack()
firstEntry = Entry(formFrame)
firstEntry.pack()

label1 = Label(formFrame,text="Lastname")
label1.pack()
lastEntry = Entry(formFrame)
lastEntry.pack()

formFrame1 = Frame(root,padx=10,pady=10)
formFrame1.place(x=205,y=5)

label = Label(formFrame1,text="Email")
label.pack()
emailEntry = Entry(formFrame1)
emailEntry.pack()

label1 = Label(formFrame1,text="Password")
label1.pack()
passwordEntry = Entry(formFrame1)
passwordEntry.pack()

def submitdata():
  showinfo("Data",f"Firstname: {firstEntry.get()}\nLastname: {lastEntry.get()}\nEmail: {emailEntry.get()}\nPassword: {passwordEntry.get()}")

button = Button(root,text="Submit Data",command=submitdata)
button.place(x=150,y=150)



root.mainloop()
