import tkinter as tk
from tkinter import messagebox
import pymongo


class TrackingApp:
    def __init__(self, busno):
        self.busno = busno
        self.root = tk.Tk()
        self.root.title("Bus Tracking")
        self.root.geometry("400x600")

        title_label = tk.Label(self.root, text="CityLink", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        title_label.place(x=150, y=10)

        status_label = tk.Label(self.root, text="Running Status", font=("times new roman", 18, "bold"), fg="black")
        status_label.place(x=120, y=60)

        bus_label = tk.Label(self.root, text="Bus no. :", font=("times new roman", 15, "bold"), fg="blue")
        bus_label.place(x=10, y=120)

        busno_label = tk.Label(self.root, text=self.busno, font=("times new roman", 15, "bold"), fg="orange")
        busno_label.place(x=80, y=120)

        source_label = tk.Label(self.root, text="Source :", font=("times new roman", 15, "bold"), fg="blue")
        source_label.place(x=10, y=150)

        destination_label = tk.Label(self.root, text="Destination :", font=("times new roman", 15, "bold"), fg="blue")
        destination_label.place(x=180, y=150)

        refresh_button = tk.Button(self.root, text="Refresh", command=self.refresh, font=("times new roman", 14))
        refresh_button.place(x=200, y=100)

        self.status_text = tk.Text(self.root, height=25, width=30)
        self.status_text.place(x=50, y=190)

        self.load_data()

        self.root.mainloop()

    def load_data(self):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017")
            db = client['users']
            collection = db['bus']

            mydoc = collection.find_one({'busno': self.busno})

            if mydoc:
                source = mydoc.get("source", "Source Not Found")
                dest = mydoc.get("dest", "Destination Not Found")
                stops = mydoc.get("route", [])
                location = mydoc.get("location", "")

                for stop in stops:
                    if stop == location:
                        self.status_text.insert(tk.END, stop + "\n\n", "bold")
                    else:
                        self.status_text.insert(tk.END, stop + "\n\n")

                self.status_text.tag_configure("bold", font=("Arial", 12, "bold"))
            else:
                source, dest = "Source Not Found", "Destination Not Found"

            source_label = tk.Label(self.root, text=source, font=("times new roman", 12, "bold"), fg="orange")
            source_label.place(x=90, y=150)

            dest_label = tk.Label(self.root, text=dest, font=("times new roman", 12, "bold"), fg="orange")
            dest_label.place(x=310, y=150)

        except pymongo.errors.ConnectionFailure:
            messagebox.showerror("Connection Error", "Failed to connect to the database.")

    def refresh(self):
        self.status_text.delete(1.0, tk.END)
        self.load_data()


class tracking2:
    def __init__(self, bus_stop):
        self.bus_stop = bus_stop
        self.root = tk.Tk()
        self.root.title("Bus Tracking")
        self.root.geometry("400x600")
        
        # Create a custom font
        custom_font = ("Helvetica", 12)
        
        # Create a Text widget with custom styling
        text_widget = tk.Text(self.root, height=20, width=20, font=custom_font, bg="white", bd=2)
        text_widget.place(x=100, y=100)
        
        # Connect to MongoDB and retrieve bus numbers
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['users']
        collection = db['bus']
        my_docs = collection.find({"route": bus_stop}, {"busno": 1, "_id": 0})
        bus_numbers = [str(doc['busno']) for doc in my_docs]
        
        # Insert bus numbers into the Text widget
        for bus_no in bus_numbers:
            text_widget.insert(tk.END, bus_no + "\n")
        
        self.root.mainloop()
        
