from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

label = Label(root, text="this is my design")
c = Canvas(root, height=500, width=500, bg="black")
line = c.create_line((500, 0, 0, 0), fill="red", width=20)
ractangle = c.create_rectangle((20, 150, 120, 50), fill="pink")
ractangle2 = c.create_rectangle((150, 150, 250, 50), fill="blue")
line2 = c.create_line((500, 200, 0, 200), fill="yellow", width=20)

btn = Button(root, text='Welcome to Tkinter!', width=20, height=2, bd='10', command=root.destroy)

btn.place(x=100, y=350)

label.pack()
c.pack()

root.mainloop()
