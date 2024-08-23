from tkinter import *

root = Tk()
root.title("User Form")
root.geometry("490x500")
# root.configure(background="lightblue")

label = Label(root, text="Username").grid(row=0, column=0,padx=10,pady=10)
entry = Entry(root,width=20).grid(row=0, column=1)

label2 = Label(root, text="Address").grid(row=1, column=0,padx=10,pady=10)
entry2 = Entry(root,width=20).grid(row=1, column=1)

label3 = Label(root, text="Add Hobies : ",padx=10,pady=10).grid(row=2, column=0)
checkbox1= Checkbutton(root,text="Cricet",onvalue=1,offvalue=0).grid(row=3,column=0)
checkbox2= Checkbutton(root,text="Cycling",onvalue=1,offvalue=0).grid(row=3,column=1)
checkbox3= Checkbutton(root,text="FootBall",onvalue=1,offvalue=0).grid(row=3,column=2)
checkbox4= Checkbutton(root,text="Gaming",onvalue=1,offvalue=0).grid(row=4,column=0)
checkbox5= Checkbutton(root,text="Music",onvalue=1,offvalue=0).grid(row=4,column=1)

menuButton = Menubutton(root,text="Select Language",padx=10,pady=20)

menuButton.menu = Menu(menuButton)
menuButton["menu"]= menuButton.menu

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

menuButton.menu.add_checkbutton(label="Hindi",variable=var1)
menuButton.menu.add_checkbutton(label="English",variable=var2)
menuButton.menu.add_checkbutton(label="Sanskrit",variable=var3)

menuButton.grid(row=5,column=1)

print(checkbox1)

maleVar = StringVar()
femaleVar = StringVar()
otherVar = StringVar()

v = StringVar(root, "1")

label4 = Label(root, text="Gender : ",padx=10,pady=10).grid(row=6, column=1)

radio = Radiobutton(root,text="Male",variable=v,value=maleVar).grid(row=7,column=0)
radio = Radiobutton(root,text="Female",variable=v,value=femaleVar).grid(row=7,column=1)
radio = Radiobutton(root,text="Other",variable=v,value=otherVar).grid(row=7,column=2)

scaleVar = DoubleVar()

label4 = Label(root, text="Confidence Level : ",padx=10,pady=5).grid(row=8, column=1)
s1 = Scale(root, variable = scaleVar,
           from_ = 0, to = 100,
           orient = HORIZONTAL).grid(row=9,column=1)

submitButton = Button(root, text="Submit").grid(row=10, column=1)

a  = IntVar()
a = 12
print(a)

root.mainloop()


