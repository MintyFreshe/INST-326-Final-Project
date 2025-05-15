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
        
        self.transaction_manager.load_transactions()  # Load transactions from CSV
        
        

    
    def on_submit(self):

        self.data = super().on_submit()  # Call the parent class method to handle the GUI submission


        # Return the entered data to be processed further


    #def 











        #load the last transaction from the csv file and display it in the GUI
        

        #self.populate_charts_from_csv()  # Populate charts on startup


    

   
   #should we write methods within the program object to combine methods from the other classes?










def main():

    app = BudgetApp()

    app.root.mainloop()
  
    



    #entered_data = app.on_submit() #<-------- after button is clicked, this function is called to process the data and returns it as a dictionary

    
    #tm.add_transaction(entered_data) #writes the data to the csv file

    #tm.save_transactions(entered_data) #<-------- this function is called to save the data to the csv file

    
















if __name__ == "__main__":

    main()
    