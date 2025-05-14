#import requred external modules
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import csv
import os
import datetime

#import required internal modules
from gui import MainGui
from transactions import TransactionManager

import reports



import test_transactions


#import modules to merge code





class BudgetApp(MainGui):
    
    def __init__(self):
        super().__init__()  # Initialize GUI first
        
        self.transaction_manager = TransactionManager()
        
        #self.populate_charts_from_csv()  # Populate charts on startup












#def main():

   
    
    #app.root.mainloop()
    
    #tm.load_transactions() #load csv
    
    #load the last transaction from the csv file and display it in the GUI
    
    
    #entered_data = app.on_submit() #<-------- after button is clicked, this function is called to process the data and returns it as a dictionary

    
    #tm.add_transaction(entered_data) #writes the data to the csv file

    #tm.save_transactions(entered_data) #<-------- this function is called to save the data to the csv file

    














   
   
   
    
    
    
    #make.gui.#pie chart update method to update the pie chart with the data which has been processed by calculations


    #take info from processEntry and pass it to the transactions module



    
    #take data from entry and pass it to pie chart method in gui module




    #retrieve data from csv file and pass it to pie chart method in gui module (get_transactions())








if __name__ == "__main__":

    app = BudgetApp()

    app.root.mainloop()
    