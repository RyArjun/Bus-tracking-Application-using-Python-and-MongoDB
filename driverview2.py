import tkinter as tk
import pymongo

class DriveView2:
    def __init__(self, bus_no):
        self.bus_no = bus_no

        self.root = tk.Tk()
        self.root.title("DriveView")
        self.root.geometry("400x600+450+50")

        title1 = tk.Label(self.root, text="CityLink", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        title1.place(x=150, y=10)
        title2 = tk.Label(self.root, text="for PMPML", font=("times new roman", 15, "bold"), bg="white", fg="orange")
        title2.place(x=160, y=50)

        label1 = tk.Label(self.root, text="Bus No:", font=("times new roman", 15, "bold"), bg="white", fg="orange")
        label1.place(x=10, y=150)
        label2 = tk.Label(self.root, text=str(self.bus_no), font=("times new roman", 15, "bold"), bg="white", fg="black")
        label2.place(x=80, y=150)

        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client['users']  
        self.collection = self.db['bus']
        my_doc = self.collection.find_one({'busno': bus_no})  
      
        stops = my_doc.get('route')
        self.destination = my_doc.get('dest')

        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=len(stops))
        for stop in stops:
            self.listbox.insert(tk.END, stop)
        self.listbox.place(x=80, y=200)

        button = tk.Button(self.root, text="UPDATE", command=self.on_button_click, font=("times new roman", 16))
        button.place(x=150, y=450)

        end_button = tk.Button(self.root, text="ENG Journey", command=self.end, font=("times new roman", 16))
        end_button.place(x=150, y=550)

        self.root.mainloop()

    def on_button_click(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_value = self.listbox.get(selected_index[0])
            #print("Selected value:", selected_value)

            filter_criteria = {'busno': self.bus_no}  
            update_operation = {'$set': {'location': selected_value}} 
            try:
                result = self.collection.update_one(filter_criteria, update_operation)
            except pymongo.errors.PyMongoError as e:
                print("Error:", e)
                
           
            self.listbox.delete(selected_index)

    def end(self):
        filter_criteria = {'busno': self.bus_no}  
        update_operation = {'$set': {'location': self.destination}} 
        try:
            result = self.collection.update_one(filter_criteria, update_operation)
        except pymongo.errors.PyMongoError as e:
            print("Error:", e)
        finally:
            self.client.close()
            self.root.destroy()

DriveView2(20)
