from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x200")

class GridButton:
    def __init__(self,root):
        self.root = root
        self.row = 1
        self.column = 0 # 1

    def addButton(self):
        print("Button Clicked")
        b = Button(self.root,text="Button")
        b.grid(row=self.row,column=self.column)
    
        self.column+=1
    
        if self.column == 5:
            self.column=0
            self.row+=1            

gridButton = GridButton(root)
button = Button(root,text="Add Button",command=gridButton.addButton)
button.grid(row=0,column=0)

root.mainloop()