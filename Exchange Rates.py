from tkinter import *
from tkinter import messagebox
import requests
master = Tk()
master.title("Exchange Rates App")
responses = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
data = responses.json()
a= data["rates"]
def showcurrlist():
    global a
    currencylist = []
    currdict = {}
    for i in a:
        b = (a[i])
        for j in b:
            if j == 'name':
                curr = (b[j])
                currencylist.append(curr)
                for k in range (len(currencylist)):
                    currdict[k] = currencylist[k]


    messagebox.showinfo(0,currdict)

def getdet():
    for i in a:
        b = (a[i])
        if b['name'] == pw.get():
            messagebox.showinfo(0,b)

pw = Entry(master)
label1 = Label(master,text= 'Enter the Currency ')
button1 = Button(master,text = "Show All Currencies", command= showcurrlist)
button2 = Button(master,text = "Get Details", command= getdet)
button3 = Button(master,text = "Exit", command= master.quit).grid(row = 4,column =0,columnspan=2)

pw.grid(row = 0,column =1)
label1.grid(row = 0,column =0)
button1.grid(row = 1,column =0,columnspan=2)
button2.grid(row = 3,column =0,columnspan=2)

master.mainloop()
