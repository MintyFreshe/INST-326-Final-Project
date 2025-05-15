import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import pandas as pd
import transactions
import reports


class MainGui:
    """
    Initializes the main GUI window for the budget application.
    Creates input fields and a submit button to collect user data.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Budget App")
        self.root.geometry("1400x800")

        # Initialize managers
        self.tm = transactions.TransactionManager()
        self.reports = reports.Reports()

        #frames for feilds 
        self.input_frame = tk.LabelFrame(self.root, text="Budget Inputs")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        # Define fields with their types
        self.fields = [
            ('Transaction Name', 'entry'),
            ('Transaction Category', 'dropdown', ['Food', 'Transportation', 'Entertainment', 'Income', 'Other']),
            ('Date (YYYY-MM-DD)', 'entry'),
            ('Amount', 'entry'),
            ('Type', 'dropdown', ['expense', 'income']),
            ('Essential', 'dropdown', ['no', 'yes'])
        ]

        # Create form
        self.entries = self.makeform(self.fields)

        # Submit button
        submit_button = Button(self.input_frame, text="Submit", command=self.on_submit) # Calls the on_submit function when clicked
        submit_button.grid(row=len(self.fields), column=0, columnspan=2, padx=15, pady=15)

        self.charts_frame = tk.Frame(self.root) #new frame for charts
        self.charts_frame.grid(row=0, column=1, padx=2, pady=2) #organizing...
        self.root.columnconfigure(1, weight=1) 
        self.root.rowconfigure(0, weight=1)

        #to hold each chart
        self.chart1_canvas = None 
        self.chart2_canvas = None
        self.chart3_canvas = None

        #Ensure proper closure of the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Load initial data
        self.load_and_display_data()
        
        self.create_charts()
        

    def makeform(self, fields):
        """
        Creates a form with appropriate input widgets for each field type.
        """
        entries = []
        for i, field in enumerate(fields):
            lbl = tk.Label(self.input_frame, text=field[0] + ":")
            lbl.grid(row=i, column=0, sticky="e", pady=1)

            if field[1] == 'entry':
                ent = tk.Entry(self.input_frame, width=20)
                ent.grid(row=i, column=1, pady=2, sticky="w")
                entries.append((field[0], ent))
            
            elif field[1] == 'dropdown': #some chat help 
                var = tk.StringVar(self.input_frame)
                var.set(field[2][0])  # default value
                ent = tk.OptionMenu(self.input_frame, var, *field[2])
                ent.config(width=15)
                ent.grid(row=i, column=1, pady=2, sticky="w")
                entries.append((field[0], var))

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

    def on_submit(self): 
        """
        Handles the submit button click event.
        """
        data = self.process_entry()
        print(data) #the data entered in the form fields to the console for testing purposes
        
        # Convert amount to float
        try:
            amount = float(data['Amount'])
        except ValueError:
            print("Invalid amount value")
            return
            
        # Add transaction to CSV
        self.tm.add_transaction(
            name = data['Transaction Name'],
            transaction_category = data['Transaction Category'],
            date = data['Date (YYYY-MM-DD)'],
            income_expense = data['Type'],
            amount = amount,
            essential = data['Essential']
        )
        
        # Clear form fields -- help from chat 
        for _, widget in self.entries:
            if isinstance(widget, tk.Entry): # if its an entry, 
                widget.delete(0, tk.END) #simple delete
            elif isinstance(widget, tk.StringVar):# if its a string var (dropdown)
                widget.set(self.fields[self.entries.index((_, widget))][2][0]) #set to first value
        
        # reload and display updated data
        self.load_and_display_data()
            
        return data

    def create_charts(self):
        """
        Creates the initial charts with empty data.
        """
        # Create empty charts first
        self.chart1_canvas = self.create_pie_chart([], [])
        self.chart2_canvas = self.create_bar_chart([], [])
        self.chart3_canvas = self.create_line_chart([], [])
        
        # Bind the window resize event
        self.root.bind('<Configure>', self.handle_resize)
        
        # Load and display initial data
        self.load_and_display_data() #using methods from reports and transactions to help!

    def create_pie_chart(self, labels, sizes):
        """Creates a pie chart using seaborn styling"""
        chart_frame = tk.Frame(self.charts_frame)
        chart_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
      
        # Update the chart frame's grid weight to allow expansion -- CHAT assist
        self.charts_frame.grid_columnconfigure(0, weight=1)
        self.charts_frame.grid_rowconfigure(0, weight=1)
      
        # Create figure with dynamic sizing 
        fig = plt.Figure(tight_layout=True) #CHAT assist 

        ax = fig.add_subplot()
        
        if sum(sizes) > 0:

            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.set_title("Transaction Distribution", pad=20)
            fig.tight_layout()
        else:
            ax.text(0.5, 0.5, "No data", ha='center', va='center')
        
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
      
        # Make sure the figure reacts to canvas resize
        fig.canvas.draw()
        return canvas


    def create_bar_chart(self, labels, sizes):
        """
        Creates a bar chart that will resize with its container.
        """
        # Create chart frame
        chart_frame = tk.Frame(self.charts_frame)
        chart_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Update the chart frame's grid weight to allow expansion -- CHAT
        self.charts_frame.grid_columnconfigure(1, weight=1)
        self.charts_frame.grid_rowconfigure(0, weight=1)
        
        # Create figure with dynamic sizing
        fig = plt.Figure(tight_layout=True) # -- CHAT

        ax = fig.add_subplot()
        
        if sum(sizes) > 0:
            # Create bar chart with seaborn
            df = pd.DataFrame({'Category': labels, 'Amount': sizes})
            sns.barplot(data=df, x='Category', y='Amount', ax=ax, hue='Category', legend=False)
            plt.setp(ax.get_xticklabels(), rotation=90, ha='right')
            ax.set_title("Transaction Amounts by Category", pad=20)
            fig.tight_layout()
        else:
            ax.text(0.5, 0.5, "No data", ha='center', va='center')
        
        # Create canvas with expansion enabled -- CHAT 
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        fig.canvas.draw()
        return canvas


    def create_line_chart(self, labels, sizes):
        """
        Creates a line chart that will resize with its container.
        """
        # Create chart frame
        chart_frame = tk.Frame(self.charts_frame)
        chart_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # Update the chart frame's grid weight to allow expansion
        self.charts_frame.grid_rowconfigure(1, weight=1)
        
        # Create figure with dynamic sizing
        fig = plt.Figure(tight_layout=True) #--CHAT 
        ax = fig.add_subplot()
        
        if sum(sizes) > 0:
            # Create line chart with seaborn - some chat help /w3 schools
            sns.lineplot(x=range(len(labels)), y=sizes, ax=ax, marker='o')
            ax.set_xticks(range(len(labels)))
            plt.setp(ax.get_xticklabels(), rotation=90, ha='right')
            ax.set_title("Transaction Trend", pad=20)
            fig.tight_layout()
        else:
            ax.text(0.5, 0.5, "No data", ha='center', va='center')
        
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Make sure the figure reacts to canvas resize
        fig.canvas.draw()
        return canvas
    
    def handle_resize(self, event): #--CHAT
       """
       Handle window resize event and update charts if needed.
       """
       # Check if this is a window resize (not a widget internal event)
       if event.widget == self.root:
           # Cancel previous scheduled resize if it exists
           if hasattr(self, '_resize_job') and self._resize_job: 
               self.root.after_cancel(self._resize_job)
          
           # Schedule new resize with 200ms delay
           self._resize_job = self.root.after(200, self.redraw_charts)
    
    def redraw_charts(self): #--chat assist
        """
        Redraw charts using current data and window size.
        """
        self._resize_job = None  # Clear the job 
        
        if hasattr(self, 'chart_data'):
            self.update_charts(self.chart_data['labels'], self.chart_data['sizes'])


    def update_charts(self, labels, sizes):
        """
        Updates the charts with new data.
        """
        # Store the latest data
        self.chart_data = {
            'labels': labels,
            'sizes': sizes
        }
        
        # destroy the old canvases to make space for new charts -- now a loop cuz its cleeeannerr
        for canvas in [self.chart1_canvas, self.chart2_canvas, self.chart3_canvas]:
            if canvas:
                canvas.get_tk_widget().destroy()
        
        # update the charts
        self.chart1_canvas = self.create_pie_chart(labels, sizes)
        self.chart2_canvas = self.create_bar_chart(labels, sizes)
        self.chart3_canvas = self.create_line_chart(labels, sizes)

    def setup_charts_grid(self):
        """
        Setting up the grid layout to fit on screen properly 
        """
        # Configure main window for resizing
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Configure the charts frame for proper expansion
        self.charts_frame.grid(sticky="nsew")
        
        # Configure grid weights for the charts layout
        self.charts_frame.grid_columnconfigure(0, weight=1)
        self.charts_frame.grid_columnconfigure(1, weight=1)
        self.charts_frame.grid_rowconfigure(0, weight=1)
        self.charts_frame.grid_rowconfigure(1, weight=1)
        
    def on_close(self):
        """
        Handles the window close event.
        """
        self.root.destroy()  # Destroys the Tkinter window
        exit()  # Terminates the program
       
    def load_and_display_data(self):
        """Load transaction data and prepare it for display"""
        transactions = self.tm.load_transactions()
        if transactions:
            category_summary = self.reports.get_category_summary(transactions)
            self.update_charts(
                labels=list(category_summary.keys()),
                sizes=list(category_summary.values())
            )

if __name__ == "__main__":
    """
    Entry point of the program. Launches the GUI.
    """
 
    app = MainGui()

    app.root.mainloop()