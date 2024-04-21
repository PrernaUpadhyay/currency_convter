from currency_converter import CurrencyConverter
import tkinter as tk
a=CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")

def clicked():
    amount=int(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    data=a.convert(amount,cur1,cur2)
    l5=tk.Label(window,text=data).place(x=230,y=290)

l1 = tk.Label(window, text=" CurrencyConverter", font="Times 25 bold")
l1.place(x=100,y=30)


l2 = tk.Label(window, text="Enter your amount:", font="Times 18 bold")
l2.place(x=50, y=70)

e1 = tk.Entry(window)
e1.place(x=300, y=90)

l3 = tk.Label(window, text="Enter currency:", font="Times 18 bold")
l3.place(x=100, y=130)

e2 = tk.Entry(window)
e2.place(x=300, y=140)

l4 = tk.Label(window, text="Enter req currency:", font="Times 18 bold")
l4.place(x=50, y=180)

e3 = tk.Entry(window)
e3.place(x=300, y=190)

b1=tk.Button(window,text="click",command=clicked).place(x=230,y=240)
e1.place(x=300, y=90)
e2.place(x=300, y=140)
e3.place(x=300, y=190)

window.mainloop()
