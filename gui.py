import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

class MainGui:
    """
    Initializes the main GUI window for the budget application.
    Creates input fields and a submit button to collect user data.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Budget App")
        self.root.geometry("1200x600")

        #frames for feilds 
        self.input_frame = tk.LabelFrame(self.root, text="Budget Inputs")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nw")

        # Define fields
        self.fields = ['Name', 'Budget', 'Food', 'Transport', 'Housing', 'Entertainment', 'Savings', 'Miscellaneous']

        # Create form
        self.entries = self.makeform(self.fields)

        # Submit button
        submit_button = Button(self.input_frame, text="Submit", command=self.on_submit) # Calls the on_submit function when clicked
        submit_button.grid(row=len(self.fields), column=0, columnspan=2, padx=15, pady=15)

        self.charts_frame = tk.Frame(self.root) #new frame for charts
        self.charts_frame.grid(row=0, column=1, padx=2, pady=2) #orginizing...
        self.root.columnconfigure(1, weight=1) 
        self.root.rowconfigure(0, weight=1)

        #to hold each chart
        self.chart1_canvas = None 
        self.chart2_canvas = None
        self.chart3_canvas = None

        #Ensure proper closure of the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)


        self.create_charts()
        

    def makeform(self, fields):
        """
        Creates a form with labeled input fields.

        Args:
            fields (list): A list of field names to create labels and entry widgets.

        Returns:
            list: A list of tuples containing field names and their corresponding entry widgets.
        """
        entries = []
        for i, field in  enumerate(fields):
            lbl = tk.Label(self.input_frame, text=field + ":")
            lbl.grid(row=i, column=0, sticky="e", pady=1)

            ent = tk.Entry(self.input_frame ,width=20)
            ent.grid(row=i, column=1, pady=2, sticky="w")

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


    def on_submit(self): 
        """
        Handles the submit button click event.
        changes the data in the Pie chart based off the data entered in the form fields.
        
        """
        data = self.process_entry()
        print(data) #the data entered in the form fields to the console for testing purposes
        
        labels = [field for field in self.fields if field not in ["Name", "Budget"]] # we dont want these to show in the data

        try:
            sizes = [float(data[label]) for label in labels] #tries converting string input to floats
        except ValueError:
            sizes = [0.0] * len(labels)

        return data #returns the data entered in form fields to be accessed in main.py   
        #self.display_data(data) 

    def create_charts(self):
        """
        Creates the initial charts with empty data.
        """
        labels = []
        sizes = []
        
        # Store data for resizing  --CHAT
        self.chart_data = {
            'labels': labels,
            'sizes': sizes
        }
        
        # Create empty charts if no data input (like on startup)
        self.chart1_canvas = self.create_pie_chart(labels, sizes)
        self.chart2_canvas = self.create_bar_chart(labels, sizes)
        self.chart3_canvas = self.create_line_chart(labels, sizes)
        
        # Bind the window resize event -- chat assist
        self.root.bind('<Configure>', self.handle_resize) #bind() connects configure to the handle resize,
                                                          #<configure> is the event for resizing the window,
                                                          #so when the window is resized, it calls the handle_resize method
                                                          #and resizes the charts.
        
    def create_pie_chart(self, labels, sizes):
        """
        Creates a pie chart
        """
        total = sum(sizes)
      
        # Create chart frame
        chart_frame = tk.Frame(self.charts_frame)
        chart_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
      
        # Update the chart frame's grid weight to allow expansion -- CHAT assist
        self.charts_frame.grid_columnconfigure(0, weight=1)
        self.charts_frame.grid_rowconfigure(0, weight=1)
      
        # Create figure with dynamic sizing 
        fig = plt.Figure(tight_layout=True) #CHAT assist 

        ax = fig.add_subplot()
      
        if total > 0: #is there any data to plot
           ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        else:
           #in the center write no data
           ax.text(0.5, 0.5, "No data", ha='center', va='center')
      
        #title for the charts 
        ax.set_title("Budget Distribution")
      
        # Create canvas with expansion enabled -- chat assist 
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
        
        if sum(sizes) > 0: #non Zero data
            ax.bar(range(len(labels)), sizes)
            if labels:
                ax.set_xticks(range(len(labels))) # organize the bars with the ticks - Chat assist
                ax.set_xticklabels(labels, rotation=45, ha='right') #each tick gets the appropriate label
        else:
            ax.text(0.5, 0.5, "No data", ha='center', va='center') #no data tag
        
        ax.set_title("Budget Comparison")
        
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
        
        if sum(sizes) > 0: #if data 
            ax.plot(range(len(labels)), sizes)

            if labels:
                ax.set_xticks(range(len(labels)))
                ax.set_xticklabels(labels, rotation=45, ha='right')
        else:
            ax.text(0.5, 0.5, "No data", ha='center', va='center')
        
        ax.set_title("Budget Trend")
        
        # Create canvas with expansion enabled
        canvas = FigureCanvasTkAgg(fig, master=chart_frame) #-- chat assist
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
        
        # destroy the old canvases to make space for new charts
        if self.chart1_canvas:
            self.chart1_canvas.get_tk_widget().destroy()
        if self.chart2_canvas:
            self.chart2_canvas.get_tk_widget().destroy()
        if self.chart3_canvas:
            self.chart3_canvas.get_tk_widget().destroy()
        
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
       

if __name__ == "__main__":
    """
    Entry point of the program. Launches the GUI.
    """
 
    app = MainGui()

    app.root.mainloop()