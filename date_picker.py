# pip install tkcalendar

from tkinter import *
from tkcalendar import Calendar
from datetime import date,time

root = Tk()
root.geometry("500x500")
root.title("Date Picker")

# get current date and time
myDate =  date.today()
print(myDate)

# myTime = time.now()
# print(myTime)

cal = Calendar(root, selectmode="day", year=myDate.year, month=myDate.month, day=myDate.day)
cal.pack()

def get_date():
  list = cal.get_date().split("/")
  properDate = list[1]+'-'+list[0]+'-'+list[2]
  label.config(text=properDate)

button = Button(root, text="Get Date", command=get_date).pack()

label = Label(root, text="")
label.pack()

root.mainloop()
