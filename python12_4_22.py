import openpyxl 
import tkinter as tk
import xlsxwriter
from openpyxl import *
from tkinter import *


root = tk.Tk()
wb = Workbook()
workbook = xlsxwriter.Workbook("openxl_addinfo_12_4_22.xlsx")
worksheet = workbook.add_worksheet()
root.geometry("500x500")
worksheet.write(0,0,"name")
x=1
def click():
    global x
    global worksheet
    i = fname.get()
    j = userid.get()
    k = password.get()
    worksheet.write(x,0,i)
    worksheet.write(x,1,j)
    worksheet.write(x,2,k)
    x+=1
    print(i,j,k)
# name
tk.Label(root,text="Name").grid(column=1,row=1)
fname = tk.Entry(root)
fname.grid(column=2,row=1)
# user id
tk.Label(root,text="UserID").grid(column=1,row=2)
userid = tk.Entry(root)
userid.grid(column=2,row=2)
# password
tk.Label(root,text="PassWord").grid(column=1,row=3)
password = tk.Entry(root)
password.grid(column=2,row=3)
# button
mybutton = tk.Button(root,text="hello",command=click)
mybutton.grid(column=2,row=4)

workbook.close()
root.mainloop()