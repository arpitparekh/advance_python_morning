from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.geometry("500x500")
window.title("Combo Box")

# entry widget with dropdown

courses = [
  "Python",
  "C",
  "C++",
  "Java",
  "Javascript",
  "PHP",
  "Ruby",
  "Perl",
  "C#",
  "Swift",
  "Kotlin",
  "Go"
]

def readSelected(*arg):  # read item from combo box
    selectedItem.configure(text=stringVar.get())

stringVar = StringVar(window)
# add hint in combo box

combo = ttk.Combobox(window, width=20,textvariable=stringVar,values=courses,font=("Arial",15),justify=CENTER,background="blue")
# combo.current(0)
combo.set("Select Course")
combo.pack()

selectedItem = Label(window, text=stringVar.get())
selectedItem.pack()

stringVar.trace_add("write", readSelected)

window.mainloop()
