from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("this is my application")
label1 = Label(root,text="this is my label 1",fg="red").grid(row=0,column=0)
label2 = Label(root,text="this is my label 2",bg="red")
label3 = Label(root,text="this is my label 3",bg="green")
label4 = Label(root,text="this is my label 4",fg="green")

# label1.pack(side=LEFT)
# label2.pack(side=RIGHT)
# label3.pack(side=TOP)
# label4.pack(side=BOTTOM)

# label1.grid(row=0,column=0)
label2.grid(row=1,column=1)
label3.grid(row=2,column=2)
label4.grid(row=5,column=5)

# event loop
root.mainloop()
