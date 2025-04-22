import tkinter as tk
from tkinter import *

def gui():
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
        
        

    
    submit_button = Button(root, text="Submit", command=on_submit)
    
    submit_button.pack(pady=10)

    root.mainloop()

def makeform(root, fields):
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
    
    infoDict = {}
    
    for entry in entries:

        name = entry[0] # grabs first element of tuple, which is the user name
        
        text = []

        #text = entry[1].get()
            
        infoDict[name] = text
    
    
    return infoDict





if __name__ == "__main__":
    
    gui()