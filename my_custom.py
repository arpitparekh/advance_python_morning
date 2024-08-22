from tkinter import *

def giveMeWindow(title):
    root = Tk()
    root.geometry("500x500")
    root.title(title)
    root.resizable(False,False)
    return root