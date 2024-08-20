from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("300x200")


def myclick(h):
    label.config(text=f"Pressed Something {h}")
    
label = Label(root,text="Nothing Pressed")
label.pack(side=TOP)

button1 = Button(root,command=lambda:myclick("Button 1"),text="Button1",activeforeground="red",activebackground="lightgreen",padx=20,pady=20).pack(side=LEFT)
button2 = Button(root,command=lambda:myclick("Button 2"),text="Button2",activeforeground="red",activebackground="lightgreen",padx=20,pady=20).pack(side=RIGHT)
button3 = Button(root,command=lambda:myclick("Button 3"),text="Button3",activeforeground="red",activebackground="lightgreen",padx=20,pady=20).pack(side=TOP)
button4 = Button(root,command=lambda:myclick("Button 4"),text="Button4",activeforeground="red",activebackground="lightgreen",padx=20,pady=20).pack(side=BOTTOM)

root.mainloop()