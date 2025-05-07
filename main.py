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
import gui
import transactions
import reports



import test_transactions


#import modules to merge code







def main():

    makegui = gui.MainGui()

    entered_data = makegui.on_submit() #<-------- after button is clicked, this function is called to process the data and returns it as a dictionary

    
    #make.gui.#pie chart update method to update the pie chart with the data which has been processed by calculations


    #take info from processEntry and pass it to the transactions module



    
    #take data from entry and pass it to pie chart method in gui module




    #retrieve data from csv file and pass it to pie chart method in gui module (get_transactions())








if __name__ == "__main__":

    main()

    pass