
import tkinter as tk
from tkinter import *

    

root = tk.Tk()
root.title("My interface :)")
root.geometry("500x500+400+300")
def click():
    message1=(txt1.get())
    message2=(txt2.get())
    message3=(txt3.get())
    message4=(txt4.get())
    print("Hello %s!!! \nFullname : %s %s \nAge : %s"%(message4,message1,message2,message3))

txt1 = StringVar()
txt2 = StringVar()
txt3 = StringVar()
txt4 = StringVar()

Label(root,text='name',font=20).pack()
Entry = tk.Entry(root,textvariable=txt1).pack()
Label(root,text='last name',font=20).pack()
Entry = tk.Entry(root,textvariable=txt2).pack()
Label(root,text='age',font=20).pack()
Entry = tk.Entry(root,textvariable=txt3).pack()
Label(root,text='nickname',font=20).pack()
Entry = tk.Entry(root,textvariable=txt4).pack()
button1 = tk.Button(root,text='click',command=click).pack()


root.mainloop()