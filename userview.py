import tkinter as tk
from tkinter import messagebox
from tracking import *

import pymongo

        


   

    


class userview:
    def __init__(self,username):
        
        root = tk.Tk()
        root.title("Login Page")
        root.geometry("%dx%d+%d+%d" % (400, 600, 450, 50))

        title1 = tk.Label(root, text="CityLink", font=("times new roman",25,"bold"),bg="white", fg="blue")
        title1.place(x=150, y=10)
        label1=tk.Label(root, text="hello "+"username", font=("times new roman",15,"bold"), fg="black")
        label1.place(x=0, y=100)

        label2=tk.Label(root, text="Enter Bus number", font=("times new roman",15,"bold"), fg="orange")
        label2.place(x=10, y=300)
        busnotext = tk.Entry(root, font=("Helvetica", 10))
        busnotext.place(x=10, y=340)

        label3=tk.Label(root, text="Enter Bus Stop", font=("times new roman",15,"bold"), fg="orange")
        label3.place(x=200, y=300)
        bustop = tk.Entry(root, font=("Helvetica", 10))
        bustop.place(x=200, y=340)
        busno1=busnotext.get()

        button1 = tk.Button(root, text="Find Bus", command=lambda: [tracking1(), root.destroy()], font=("times new roman", 14))
        button1.place(x=10, y=380)
        


def tracking1():
        busno=20
        
        tracking(busno)
        
        
        

