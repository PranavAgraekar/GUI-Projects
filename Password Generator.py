import password_generator
from tkinter import *

master = Tk()
master.title("Password Generator")

# password = password_generator.generate(count=1, length= 8)
# password.minlen = 8
# password.maxlen = 15
# password.minuchars = 1
# password.minlchars = 1
# password.minchars = 1

def gen():
    a = password_generator.generate(count=1, length= 8)
    pw.insert(0,a)

def del1():
    pw.delete(0,END)

pw = Entry(master)
label1 = Label(master,text = "Password")
button1 = Button(master,text = "Generate", command= gen)
button2 = Button(master,text = "Clear", command= del1)

pw.grid(row = 0,column =1)
label1.grid(row = 0,column =0)
button1.grid(row = 1,column =0,columnspan=2)
button2.grid(row = 2,column =0,columnspan=2)
master.mainloop()