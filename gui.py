import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Gui:
    """
    Initializes the main GUI window for the budget application.
    Creates input fields and a submit button to collect user data.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Budget App")
        self.root.geometry("1000x800")

        
        #Ensure proper closure of the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Define fields
        self.fields = ['Name', 'Budget', 'Food', 'Transport', 'Housing', 'Entertainment', 'Savings', 'Miscellaneous']

        # Create form
        self.entries = self.makeform(self.fields)

        # Submit button
        submit_button = Button(self.root, text="Submit", command=self.on_submit) #<-- Calls the on_submit function when clicked
        submit_button.pack(side=LEFT, padx=100, pady=15)

        self.pie_chart()

        self.root.mainloop()

    def makeform(self, fields):
        """
        Creates a form with labeled input fields.

        Args:
            fields (list): A list of field names to create labels and entry widgets.

        Returns:
            list: A list of tuples containing field names and their corresponding entry widgets.
        """
        entries = []
        for field in fields:
            row = Frame(self.root)
            lab = Label(row, width=10, text=field, anchor='w')
            ent = Entry(row, width=20)  # Adjust the width here
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=LEFT, expand=FALSE, fill=X)
            entries.append((field, ent))

        print(entries)
        return entries

    def process_entry(self):
        """
        Processes the data entered in the form fields.

        Returns:
            dict: A dictionary where keys are field names and values are the entered data.
        """
        info_dict = {}
        for entry in self.entries:
            name = entry[0]  # grabs first element of tuple, which is the field name
            text = entry[1].get()  # gets the text from the entry widget
            info_dict[name] = text
        
        return info_dict #<-- Holds the data entered in the form fields

    def display_data(self, data):
        """
        Displays the processed data in a new window or updates the existing GUI.

        Args:
            data (dict): The data to be displayed.
        """
        # Example implementation to display data in a new window
        new_window = tk.Toplevel(self.root)
        new_window.title("Processed Data")
        
        for key, value in data.items():
            label = Label(new_window, text=f"{key}: {value}")
            label.pack()

    def on_submit(self):
        """
        Handles the submit button click event.
        changes the data in the Pie chart based off the data entered in the form fields.
        
        """
        data = self.process_entry()
        self.display_data(data)

    def pie_chart(self):
        """
        
        Placeholder for pie chart functionality.
        """
        
        self.labels = 'Frogs', 'Hogs', 'Dogs', 'Logs' #
        
        self.sizes = [15, 30, 45, 10] #<-- Placeholder data - calculate % each part of total budget and replace

        fig, ax = plt.subplots()
        
        ax.pie(self.sizes, labels=self.labels, textprops={'size': 'smaller'}, radius=1.2, startangle=90, autopct='%1.1f%%', shadow=True, explode=(0.1, 0.1, 0.1, 0.1))
        
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=False)
        
        
    def on_close(self):
        """
        Handles the window close event.
        """
        self.root.destroy()  # Destroys the Tkinter window
        exit()  # Terminates the program
       

if __name__ == "__main__":
    """
    Entry point of the program. Launches the GUI.
    """
    Gui()