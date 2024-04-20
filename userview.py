import tkinter as tk
from tkinter import messagebox
from tracking1 import *
import pymongo

class UserView:
    def __init__(self, username):
        self.root = tk.Tk()
        self.root.title("User View")
        self.root.geometry("%dx%d+%d+%d" % (400, 600, 450, 50))

        title_label = tk.Label(self.root, text="CityLink", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        title_label.pack(pady=10)

        welcome_label = tk.Label(self.root, text="Hello, " + username, font=("times new roman", 15, "bold"), fg="black")
        welcome_label.pack(pady=20)

        busno_label = tk.Label(self.root, text="Enter Bus number:", font=("times new roman", 15, "bold"), fg="orange")
        busno_label.pack()

        self.busno_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.busno_entry.pack()

        bustop_label = tk.Label(self.root, text="Enter Bus Stop:", font=("times new roman", 15, "bold"), fg="orange")
        bustop_label.pack()

        self.bustop_entry = tk.Entry(self.root, font=("Helvetica", 10))
        self.bustop_entry.pack()

        find_button = tk.Button(self.root, text="Find Bus", command=self.find_bus, font=("times new roman", 14))
        find_button.place(x=120,y=250)

        find_button2 = tk.Button(self.root, text="Find Bus(Stop)", command=self.find_bustop, font=("times new roman", 14))
        find_button2.place(x=250,y=250)

        self.root.mainloop()
        
    def find_bus(self):
        bus_no = self.busno_entry.get()
        bus_stop = self.bustop_entry.get()

        try:
            #bus_no = int(bus_no)
            
            if bus_no == "0":
                messagebox.showerror("Error", "Invalid bus number.")
            
            else:
                self.root.destroy()
                TrackingApp(bus_no)
                
        except ValueError:
            messagebox.showerror("Error", "Invalid bus number. Please enter a valid integer.")

    def find_bustop(self):
        bus_stop = self.bustop_entry.get()
        tracking2(bus_stop)




UserView("jack")