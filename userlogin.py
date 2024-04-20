import tkinter as tk
from tkinter import messagebox
from userview import UserView  
import pymongo

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    try:
        client = pymongo.MongoClient("")
        db = client['users']  
        collection = db['userdata']  
        
        user = collection.find_one({'username': username, 'password': password})
        
        if user:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            root.destroy()
            UserView(username)
            
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    except pymongo.errors.ConnectionFailure:
        messagebox.showerror("Connection Error", "Failed to connect to the database.")

def register():
    
    pass

def show_registration_form():
    messagebox.showinfo('Message', 'You clicked the Register button!')
    

root = tk.Tk()
root.title("Login Page")
root.geometry("%dx%d+%d+%d" % (400, 600, 450, 50))

title1 = tk.Label(root, text="CityLink", font=("times new roman", 25, "bold"), bg="white", fg="blue")
title1.place(x=150, y=10)
title2 = tk.Label(root, text="for PMPML", font=("times new roman", 15, "bold"), bg="white", fg="orange")
title2.place(x=160, y=50)

label_username = tk.Label(root, text="Username", font=("Helvetica", 16))
label_username.place(x=30, y=250)
username_entry = tk.Entry(root, font=("Helvetica", 14))
username_entry.place(x=150, y=250)

label_password = tk.Label(root, text="Password:", font=("Helvetica", 18))
label_password.place(x=30, y=300)
password_entry = tk.Entry(root, font=("Helvetica", 14), show="*")
password_entry.place(x=150, y=300)

login_button = tk.Button(root, text="Login", command=login, font=("times new roman", 14))
login_button.place(x=150, y=350)

reg_button = tk.Button(root, text="Register", command=show_registration_form, font=("times new roman", 14))
reg_button.place(x=250, y=350)

root.mainloop()
