from tkinter import *


aken=Tk()
aken.geometry("900x900")
aken.title("Sisenemine")

var=IntVar()

aken.iconbitmap("xexe.ico")
f=Frame(aken,bg="#E6E6FA")
lbl=Label(aken,text="fdhth",font="Arial 50",fg="#4B0082",height=10,width=15)
btn=Button(f,text="Vajuta siia",font="Arial 24",relief=GROOVE,width=15)

lbl.pack()
btn.pack()


aken.mainloop()



