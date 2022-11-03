from msilib.schema import ListBox
import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("200x300")
listSample = Listbox (root,width=70,height=30,fg="red",font=("Arial 28"))
listSample.insert(1,"pizza")
listSample.insert(2,"pizza 1")
listSample.insert(3,"pizza 2")

listSample.pack()
root.mainloop()