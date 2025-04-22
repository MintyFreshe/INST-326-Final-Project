import tkinter as tk
from tkinter import *

def gui():
    """
    Initializes the main GUI window for the budget application.
    Creates input fields and a submit button to collect user data.
    """
    root = tk.Tk()
    root.title("My Budget App")
    root.geometry("500x300")

    # Define fields
    fields = ['Name', 'Budget', 'Field 3']

    # Create form
    entries = makeform(root, fields)

    # Submit button
    def on_submit():
        
        data = processEntry(entries)
        
    
    #some sort of validation to check if the data is valid before processing it into dictionary



    
    submit_button = Button(root, text="Submit", command=on_submit)
    
    submit_button.pack(pady=10)

    root.mainloop()


def makeform(root, fields):
    """
    Creates a form with labeled input fields.

    Args:
        root (Tk): The root window where the form will be added.
        fields (list): A list of field names to create labels and entry widgets.

    Returns:
        list: A list of tuples containing field names and their corresponding entry widgets.
    """
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=20, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    
    print(entries)
    return entries



def processEntry(entries):
    """
    Processes the data entered in the form fields.

    Args:
        entries (list): A list of tuples containing field names and their corresponding entry widgets.

    Returns:
        dict: A dictionary where keys are field names and values are the entered data. ?? or a dictionary of lists where the 
        keys are the usernames and the values are lists of their corresponding data.
    """
    infoDict = {}
    
    for entry in entries:

        name = entry[0] # grabs first element of tuple, which is the user name
        
        text = []

        #text = entry[1].get()
            
        infoDict[name] = text
    
    return infoDict



def displayData(data):
    """
    
    Displays the processed data in a new window or updates the existing GUI.

    Args:
        data (dict): The data to be displayed.
    
    """
    
    #use regex to search dictionary for the name of the user and display their data in a new window
    # or update the existing GUI with the new data
    
    
    pass




if __name__ == "__main__":
    """
    Entry point of the program. Launches the GUI.
    """
    gui()