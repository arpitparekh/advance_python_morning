from tkinter import *

root = Tk()

userNameLabel = Label(root,text="Username").place(x=10,y=10)
userEntry = Entry(root).place(x=10,y=40)
passwordLabel = Label(root,text="Password").place(x=10,y = 80)
passwordEntry = Entry(root).place(x=10,y = 110)
submitButton = Button(root,text="Submit").place(x = 10,y = 150)

root.mainloop()
