from tkinter import *
from tkinter import ttk

def kodu(aken=None):
    if aken:
       aken.destroy()
    aken=Tk()
    aken.geometry("600x600")
    aken.resizable(width=False,height=False)
    aken.title("mäng ♡")
    aken.iconbitmap("cute.ico")

    lbl=Label(aken,text="avaleht",font="Arial 40")
 
lbl.place(x=190,y=50)
aken.mainloop()