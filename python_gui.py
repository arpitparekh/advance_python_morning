from tkinter import*
from tkinter.simpledialog import askinteger

# tkinter is used for gui development in python
m = Tk()

m.geometry("400x400")
label = Label(m,text="This is my python Gui")
# label2 = Label(m,text="This is my python Gui 2")

# The pack() Method 
# This geometry manager organizes widgets in blocks before placing them in the parent widget.
# The grid() Method
# This geometry manager organizes widgets in a table-like structure in the parent widget.
# The place() Method
# This geometry manager organizes widgets by placing them in a specific position in the parent widget.

label.pack()
# label2.pack()

def show():
    print("Button clicked")
    num = askinteger('Please Enter Number',"Enter something")
    print(num)
    
button = Button(m,text="Please Click me",command=show)    
button.pack()

m.mainloop()  # render a screen on desktop

# widgets

