from tkinter import *

root = Tk()

userNameLabel = Label(root,text="Username").grid(row=0,column=0)
userEntry = Entry(root).grid(row=0,column=1)
passwordLabel = Label(root,text="Password").grid(row=1,column=0)
passwordEntry = Entry(root).grid(row=1,column=1)
submitButton = Button(root,text="Submit").grid(row=2,column=0)

root.mainloop()
