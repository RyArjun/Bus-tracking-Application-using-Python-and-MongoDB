import tkinter as tk
from tkinter import messagebox

import pymongo


class tracking:
    def __init__(self,busno):
        self.busno=busno
        
        root = tk.Tk()
        root.title("Login Page")
        root.geometry("%dx%d+%d+%d" % (400, 600, 450, 50))

        title1 = tk.Label(root, text="CityLink", font=("times new roman",25,"bold"),bg="white", fg="blue")
        title1.place(x=150, y=10)
        title1 = tk.Label(root, text="Running Status", font=("times new roman",18,"bold"), fg="black")
        title1.place(x=120, y=60)
        label1=tk.Label(root, text="Bus no. :", font=("times new roman",15,"bold"), fg="blue")
        label1.place(x=10, y=120)
        label2=tk.Label(root, text=busno, font=("times new roman",15,"bold"), fg="orange")
        label2.place(x=80, y=120)

    

        label3=tk.Label(root, text="Source :", font=("times new roman",15,"bold"), fg="blue")
        label3.place(x=10, y=150)
        
        label5=tk.Label(root, text="Destination :", font=("times new roman",15,"bold"), fg="blue")
        label5.place(x=180, y=150)
      

        client = pymongo.MongoClient("")
        db = client['users']  
        collection = db['bus']
        mydoc = collection.find({'busno': busno})
        x=mydoc[0]
        source=x["source"]
        dest=x["dest"]
        print(mydoc)
      
        label4=tk.Label(root, text=source, font=("times new roman",12,"bold"), fg="orange")
        label4.place(x=90, y=150)
        label6=tk.Label(root, text=dest, font=("times new roman",12,"bold"), fg="orange")
        label6.place(x=310, y=150)

