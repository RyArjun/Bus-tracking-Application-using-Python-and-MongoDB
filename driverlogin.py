import tkinter as tk
from tkinter import messagebox
import pymongo
from driverview import *

class DriverLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login Page")
        self.root.geometry("%dx%d+%d+%d" % (400, 600, 450, 50))

        title1 = tk.Label(self.root, text="CityLink", font=("times new roman",25,"bold"),bg="white", fg="blue")
        title1.place(x=150, y=10)
        title2 = tk.Label(self.root, text="for PMPML", font=("times new roman",15,"bold"),bg="white", fg="orange")
        title2.place(x=160, y=50)

        title3 = tk.Label(self.root, text="Driver's Portal", font=("times new roman",25,"bold"),bg="black", fg="white")
        title3.place(x=100, y=150)

        label_username = tk.Label(self.root, text="Username", font=("Helvetica", 16))
        label_username.place(x=30, y=250)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.username_entry.place(x=150, y=250)

        label_password = tk.Label(self.root, text="Password:", font=("Helvetica", 18))
        label_password.place(x=30, y=300)
        self.password_entry = tk.Entry(self.root, font=("Helvetica", 14), show="*")
        self.password_entry.place(x=150, y=300)

        login_button = tk.Button(self.root, text="Login", command=self.login, font=("times new roman", 14))
        login_button.place(x=150, y=350)

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            client = pymongo.MongoClient("")
            db = client['users']
            collection = db['driverdata']

            user = collection.find_one({'username': username, 'password': password})

            if user:
                messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
                self.root.destroy()  
                DriverView(username)  
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        
        except pymongo.errors.ConnectionFailure:
            messagebox.showerror("Connection Error", "Failed to connect to the database.")

DriverLogin()
