import tkinter as tk
from tkinter import *
import time

root = tk.Tk()


mylable = Label(root)
mylable.pack()

def time_loop() :
    time_object = time.localtime()
    time_string = time.asctime(time_object)
    mylable.config(text=time_string)
    mylable.after(1000,time_loop)
    print(time_string)
time_loop()
root.mainloop()