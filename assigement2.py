from cProfile import label
from cmath import log
from logging import root
import tkinter
from tkinter import*
root = Tk()
logo = tkinter.PhotoImage(file="11.PNG")
w1 = Label(root,image=logo).pack(side="right")
msg = "Welcome Semester 3."
w2 = Label(root,justify=tkinter.LEFT,padx=10,text=msg).pack(side=LEFT)
root.mainloop()
