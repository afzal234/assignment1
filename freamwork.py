# 1
from struct import pack
from tkinter import*
import tkinter as  tk
from tkinter import messagebox
top=Tk() 
top.geometry("300x200")

def fun():
    messagebox.showinfo("Hello", "Red Button clicked")

b1 = Button(top,text="Red",command=fun,activeforeground="red",activebackground ="pink",pady=10 )
b2 = Button(top,text="Blue",activeforeground="blue",activebackground="pink",pady=10)
b3 = Button(top,text="Green",activeforeground="green",activebackground="pink",pady=10)
b4 = Button(top,text="Yellow",activeforeground="yellow",activebackground="pink",pady=10)

b1.pack(side= LEFT)
b2.pack(side= RIGHT)
b3.pack(side= TOP)
b4.pack(side= BOTTOM)




# top.mainloop()

# 2
# from tkinter import *
# # creating Tk window
# pane = Tk()

# b1 = Button(pane,text= "Click me !")
# b1.pack(fill=Y, expand = True)

# b2 = Button(pane,text="Click me too")
# b2.pack(fill= X, expand = True)

# # Execute Tkinter
# pane.mainloop()

# 3
# creating Tk window
# from doctest import master
# from re import X
# from tkinter import CENTER, NE, SW, Button, Tk, mainloop
# import tkinter


# master = Tk()

# setting geometry of tk window
# master.geometry("200x200")

# button widget

# b1 = Button(master, text= "Click me !")
# b1.place(relx = 1,x = -2, y=2,anchor =NE)

# # button width

# b2 = Button(master, text="GFG")
# b2.place(relx=0.5,rely=0.5,anchor=CENTER)

# master.mainloop()

# 4
# from doctest import master
# from tkinter import *
# # creating main tkinter window/topLevel
# master = Tk()

# # this will create Label widget
# l1 = Label(master,text="First:")
# l2 = Label(master,text="Second:")

# # grid method to arrange Labels in respective
# # rows and columns as specified 
# l1.grid(row=0,column=0,sticky=W,pady=2)
# l2.grid(row=1,column=0,sticky=W,pady=2)
# master.mainloop()

# 5

# from tkinter import * 
# window = Tk() 

# l1 - Label (window, text='Gujrat University!' ,font="Arial Bold",20)
# window.geometry('350x200')
# l1. grid (column=0, row=0) 

# window.mainloop()



# 6
# from tkinter import * 
# root = Tk()

# logo = root.PhotoImage(file='test.png') 
# w1 = Label(root, image=logo).pack(side="right")
# msg = Welcome semester 3.”””
# W2 = Label(root,justify=tk. LEFT, padx = 10,text=msg).pack(side="left") 
# root.mainloop()


# 7
# import tkinter as tk 
# root=tk.Tk() 
# root.geometry("600x400") 
# name_var=tk.StringVar() 
# passw_var=tk.StringVar() 
# def submit():
#     name=name_var.get() 
#     password=passw_var.get() 
#     print("The name is : " + name) 
#     print("The password is : " + password) 
#     name_var.set("") 
#     passw_var.set("")

# name_label = tk.Label(root, text = 'Username', font=('Arial',10, 'bold')) 
# name_entry = tk.Entry(root,textvariable = name_var, font=('Arial',10,'normal')) 
# passw_label = tk.Label(root, text = 'Password', font = ('Arial',10,'bold')) 
# passw_entry=tk.Entry(root, textvariable = passw_var, font = ('Arial',10,'normal'), show = '*') 
# sub_btn=tk.Button(root,text = 'Submit', command = submit)


# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)

# root.tk.mainloop()

# 8
from logging import root
from tkinter import *
import tkinter 
root=Tk()
root.geometry("300x200")

W=Label(root,text='Gujrat University',font="50").pack()

Checkbutton1 = tkinter.IntVar()
Checkbutton2 = tkinter.IntVar() 
Checkbutton3 = tkinter.IntVar()

Button1 = Checkbutton(root,text="Tutorial",variable=Checkbutton1,onvalue=1,offvalue=0,height=2,width=10)
Button2 = Checkbutton(root,text="Student",variable=Checkbutton2,onvalue=1,offvalue=0,height=2,width=10)
Button3 = Checkbutton(root,text="Courses",variable=Checkbutton3,onvalue=1,offvalue=0,height=2,width=10)

Button1.pack()
Button2.pack()
Button3.pack()

root.mainloop()