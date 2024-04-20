import tkinter as tk
from driverview2 import DriveView2

class DriverView:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title("Driver Dashboard")
        self.root.geometry("400x600+450+50")

        title1 = tk.Label(self.root, text="CityLink", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        title1.place(x=150, y=10)
        title2 = tk.Label(self.root, text="for PMPML", font=("times new roman", 15, "bold"), bg="white", fg="orange")
        title2.place(x=160, y=50)
        title4 = tk.Label(self.root, text="Welcome: " + username, font=("times new roman", 25, "bold"), fg="black")
        title4.place(x=10, y=90)

        label1 = tk.Label(self.root, text="Enter Bus number", font=("Helvetica", 16))
        label1.place(x=20, y=250)

        self.busno = tk.Entry(self.root, font=("Helvetica", 10))
        self.busno.place(x=30, y=280)

        login_button = tk.Button(self.root, text="Start Journey", command=self.tracking1, font=("times new roman", 14))
        login_button.place(x=30, y=310)

        self.root.mainloop()

    def tracking1(self):
        busno = self.busno.get()
        self.root.destroy()
        DriveView2(busno)


