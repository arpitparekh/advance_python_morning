from tkinter import *

root = Tk()
root.title("User Form")
root.geometry("490x650")
# root.configure(background="lightblue")

languageList = []
hobbiesList = []

# username and address

label = Label(root, text="Username").grid(row=0, column=0,padx=10,pady=10)
entry = Entry(root,width=20)
entry.grid(row=0, column=1)

label2 = Label(root, text="Address").grid(row=1, column=0,padx=10,pady=10)
entry2 = Entry(root,width=20)
entry2.grid(row=1, column=1)

# checkbox hobbies

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

label3 = Label(root, text="Add Hobies : ",padx=10,pady=10,)
label3.grid(row=2, column=0)

checkbox1= Checkbutton(root,text="Cricet",onvalue=1,offvalue=0,variable=var1)
checkbox1.grid(row=3,column=0)
checkbox2= Checkbutton(root,text="Cycling",onvalue=1,offvalue=0,variable=var2)
checkbox2.grid(row=3,column=1)
checkbox3= Checkbutton(root,text="FootBall",onvalue=1,offvalue=0,variable=var3)
checkbox3.grid(row=3,column=2)
checkbox4= Checkbutton(root,text="Gaming",onvalue=1,offvalue=0,variable=var4)
checkbox4.grid(row=4,column=0)
checkbox5= Checkbutton(root,text="Music",onvalue=1,offvalue=0,variable=var5)
checkbox5.grid(row=4,column=1)


# menu button

menuButton = Menubutton(root,text="Select Language",padx=10,pady=20)

menuButton.menu = Menu(menuButton)
menuButton["menu"]= menuButton.menu

var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

menuButton.menu.add_checkbutton(label="Hindi",variable=var6)
menuButton.menu.add_checkbutton(label="English",variable=var7)
menuButton.menu.add_checkbutton(label="Sanskrit",variable=var8)

menuButton.grid(row=5,column=1)

# radio button

maleVar = StringVar()
femaleVar = StringVar()
otherVar = StringVar()

v = StringVar(root, "1")

label4 = Label(root, text="Gender : ",padx=10,pady=10).grid(row=6, column=1)

radio = Radiobutton(root,text="Male",variable=v,value="Male").grid(row=7,column=0)
radio = Radiobutton(root,text="Female",variable=v,value="Female").grid(row=7,column=1)
radio = Radiobutton(root,text="Other",variable=v,value="Other").grid(row=7,column=2)

scaleVar = DoubleVar()

label4 = Label(root, text="Confidence Level :  ",padx=10,pady=5).grid(row=8, column=1)
s1 = Scale(root, variable = scaleVar,
           from_ = 0, to = 100,
           orient = HORIZONTAL).grid(row=9,column=1)

def submitButtonClick():

    languageList.clear()
    hobbiesList.clear()

    if var1.get() : hobbiesList.append("Cricet")
    if var2.get() : hobbiesList.append("Cycling")
    if var3.get() : hobbiesList.append("FootBall")
    if var4.get() : hobbiesList.append("Gaming")
    if var5.get() : hobbiesList.append("Music")

    if var6.get() : languageList.append("Hindi")
    if var7.get() : languageList.append("English")
    if var8.get() : languageList.append("Sanskrit")

    userData={
        "username":str(entry.get()),
        "address":str(entry2.get()),
        "hobbies":hobbiesList,
        "language":languageList,
        "gender":v.get(),
        "confidence":scaleVar.get()
    }
    
    userDataString = f"Username : {userData['username']} \nAddress : {userData['address']} \nHobbies : {userData['hobbies']} \nLanguage : {userData['language']} \nGender : {userData['gender']} \nConfidence Level : {userData['confidence']}"

    resultLabel.configure(text=userDataString)

submitButton = Button(root, text="Submit",command=submitButtonClick).grid(row=10, column=1)

resultLabel = Label(root, text="Result : ")
resultLabel.grid(row=11, column=1)

root.mainloop()


