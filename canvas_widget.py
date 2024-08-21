from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")


c = Canvas(root,height=500,width=500,bg="red")
arc = c.create_arc((20,50,350,600),start=0,fill="purple")
line = c.create_line((0,0,500,500),fill="green",width=20)
ractangle = c.create_rectangle((40,350,120,200),fill="pink")

# create object of image
image = PhotoImage(file="img.png",height=200,width=200)

canvasImage = c.create_image((250,250),image=image,anchor = CENTER)

c.pack()

root.mainloop()