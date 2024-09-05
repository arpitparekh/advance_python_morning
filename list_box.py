from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.geometry("500x500")
window.title("Combo Box")


def showSuggestion(event):
  data = entry.get()

  listbox.delete(0, END)

  for i in courses:
    if data.lower() in i.lower():
      listbox.insert(END, i)


label = Label(window, text="Enter Something", font=("Arial", 15))
label.pack()
entry = Entry(window, width=20, font=("Arial", 15))
entry.pack()

# show suggestion
entry.bind('<KeyRelease>', showSuggestion)

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

def getItem(event):
  str = ""
  selectedIndex = listbox.curselection()  # 0,1,2
  for i in selectedIndex:
    str += listbox.get(i)

  # clear entry first
  entry.delete(0, END)
  entry.insert(END, str)


label1 = Label(window, text="Suggestions", font=("Arial", 15))
label1.pack()
listbox = Listbox(window, width=20, height=5, font=("Arial", 15), selectmode=SINGLE)

# select list item
listbox.bind('<<ListboxSelect>>', getItem)
listbox.pack()


  # selectedItem.config(text=str)

# button = Button(window, text="Select", font=("Arial", 15), command=getItem)
# button.pack()

# selectedItem = Label(window, text="")
# selectedItem.pack()

def updateList(course):
  listbox.delete(0, END)
  for course in courses:
    listbox.insert(END, course)

updateList(courses)


window.mainloop()
