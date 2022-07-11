from tkinter import *
from tkinter import messagebox

master = Tk()
master.title('Calculator')

def add():
    try:
        x = int(num1.get())
        y = int(num2.get())
        result = x+y
        messagebox.showinfo('Solution',f'The Answer is {result}')
    except:
        messagebox.showerror('Error','Please Enter Valid Input')

def sub():
    try:
        x = int(num1.get())
        y = int(num2.get())
        result = x-y
        messagebox.showinfo('Solution',f'The Answer is {result}')
    except:
        messagebox.showerror('Error','Please Enter Valid Input')

def mul():
    try:
        x = int(num1.get())
        y = int(num2.get())
        result = x*y
        messagebox.showinfo('Solution',f'The Answer is {result}')
    except:
        messagebox.showerror('Error','Please Enter Valid Input')

def div():
    try:
        x = int(num1.get())
        y = int(num2.get())
        result = x/y
        messagebox.showinfo('Solution',f'The Answer is {result}')
    except:
        messagebox.showerror('Error','Please Enter Valid Input')

num1 = Entry(master)
num2 = Entry(master)

label1 = Label(master,text= 'Enter First Number')
label2 = Label(master,text= 'Enter Second Number')
Button1 = Button(master,text= 'Add',padx=40,pady=20,command= add)
Button2 = Button(master,text= 'Subtract',padx=40,pady=20,command= sub)
Button3 = Button(master,text= 'Multiply',padx=40,pady=20,command= mul)
Button4 = Button(master,text= 'Divide',padx=40,pady=20,command= div)
Button5 = Button(master,text= 'Exit',padx=40,pady=20,command = master.quit)

label1.grid(row = 0,column =0)
label2.grid(row = 1,column =0)
num1.grid(row = 0,column =1,ipadx=20,ipady=15)
num2.grid(row = 1,column =1,ipadx=20,ipady=15)
Button1.grid(row = 2,column =0,columnspan=2)
Button2.grid(row = 3,column =0,columnspan=2)
Button3.grid(row = 4,column =0,columnspan=2)
Button4.grid(row = 5,column =0,columnspan=2)
Button5.grid(row = 6,column =0,columnspan=2)

master.mainloop()