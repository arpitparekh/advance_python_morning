from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Other Widgets")
label = Label(window, text="Spin Box", font=("Arial", 15))
label.pack()


spinBox = Spinbox(window, from_=0, to=100, font=("Arial", 15))
spinBox.pack()

def checkValue(event=None):
  print(spinBox.get())      # is used to get value from spin box
  label2.configure(text=scaleValue.get())

button = Button(window, text="Check Value SpinBox", command=checkValue)
button.pack()

label1 = Label(window, text="Scale", font=("Arial", 15))
label1.pack()

scaleValue = DoubleVar()
scale = Scale(window, from_=0, to=100, font=("Arial", 15),variable=scaleValue,command=checkValue,orient=HORIZONTAL)
scale.pack()

label2 = Label(window, text="Scale", font=("Arial", 15))
label2.pack()


window.mainloop()
