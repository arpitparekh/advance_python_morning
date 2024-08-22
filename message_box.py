from tkinter import *
from tkinter.messagebox import *
from my_custom import *

root = giveMeWindow("Message Boxes")

def clickOnButton(what):
    if what=="info" :
        showinfo(title="Info Box",message="you Click on info box")
    elif what=="warning":
        showwarning(title="Warning Box",message="you Click on warning box")
    elif what=="error":
        showerror(title="Error Box",message="you Click on error box")
        
    elif what=="question":
        
        res=askquestion(title="Question Box",message="Asman he nila kyu")
        
        if res == 'yes': print("User clicked Yes")
        else : print("User clicked No")
        
    elif what=="yesorno":
        
        res = askyesnocancel(title="Yes Or No Box",message="Kehna kya chahte ho ji?")
        
        if res==True:
            print("Yes Click")
        elif res==FALSE:
            print("No Click")
        else:
            print("Cancel")
        
    elif what=="cancel":
        
        res = askokcancel(title="Cancel Box",message="you Click on Cancel box")
        if res==True:
            print("Yes Click")
        else:
            print("No Click")
           
                                

button = Button(root,text="Info Box",command=lambda:clickOnButton("info"))
button.pack()
button1 = Button(root,text="Warning Box",command=lambda:clickOnButton("warning"))
button1.pack()
button2 = Button(root,text="Error Box",command=lambda:clickOnButton("error"))
button2.pack()
button3 = Button(root,text="Ask Question Box",command=lambda:clickOnButton("question"))
button3.pack()
button4 = Button(root,text="Ask Yes Or No Box",command=lambda:clickOnButton("yesorno"))
button4.pack()
button5 = Button(root,text="Ask Ok Cancel Box",command=lambda:clickOnButton("cancel"))
button5.pack()

ronak = lambda a : a+10
print(ronak(10))

root.mainloop()

