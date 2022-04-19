from cgitb import text
from ctypes import resize
import tkinter as tk
from tkinter import font

def click():
    print("hello")

root = tk.Tk()
# root.resizable(100,100) #fix size
# root.geometry('1000x500') 

# click_hello = tk.Button(root,text='hello',command=click).grid()

# for i in range(10):
#     my_lable = tk.Label(root,text='hello',font=('Arial Bold',20)).grid(column=i,row=i)


#Canvas
# cv = tk.Canvas(root,
#               width=100,
#               height=100,
#               background='blue')
# cv.pack()
# cv.create_line(10,10,20,20)

# textinsert
# ins_text = tk.Text(root)
# ins_text.insert("1.0","hello")
# ins_text.pack()

# Entry
# root.geometry('400x250')
# entrt1 = tk.Entry(root).place(x=85,y=50)
# entrt2 = tk.Entry(root).place(x=85,y=90)


root.mainloop()