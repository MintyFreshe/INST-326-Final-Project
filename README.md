# Budget Tracker App

A personal finance and budget management tool with a graphical user interface (GUI) built using Python and Tkinter. This application allows users to input, visualize, and manage their income and expenses in an intuitive and interactive way.

View the repository on GitHub: [https://github.com/MintyFreshe/INST-326-Final-Project](https://github.com/MintyFreshe/INST-326-Final-Project)

---

## Project Structure

```
├── gui.py             # GUI interface with charts and transaction form
├── main.py            # Main entry point to launch the application
├── reports.py         # Functions for analyzing and plotting financial summaries
├── transactions.py    # Transaction manager to load, save, and manipulate CSV data
├── transactions.csv   # Data file to store transactions
```

---

## Features

- Add income and expense transactions with category and date
- Automatically saves and updates data in a CSV file
- Pie chart showing transaction distribution by category
- Bar chart of category spending
- Line chart for transaction trends over time
- Summary functions for:
  - Total income and expenses
  - Monthly summaries
  - Top expense entries
- Responsive GUI built with Tkinter and embedded Matplotlib charts

---

## Technologies Used

- Python 3
- Tkinter – for the graphical interface
- Matplotlib & Seaborn – for visualizing financial data
- Pandas – for data manipulation
- CSV – for data storage and persistence

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MintyFreshe/INST-326-Final-Project.git
cd INST-326-Final-Project
```

### 2. Install Required Libraries

```bash
pip install matplotlib seaborn pandas
```

### 3. Run the Application

```bash
python main.py
```

### 4. Run the Reports

```bash
python main.py reports
```

---

## Example Transaction Fields

When adding a transaction, you will provide:

- Transaction Name: Description or label
- Transaction Category: e.g. Food, Transportation, Entertainment
- Date (YYYY-MM-DD): When the transaction occurred
- Amount: Positive number (float)
- Type: Either "income" or "expense"
- Essential: Whether the transaction is essential (yes/no)

---

## Visualizations

- Pie Chart: Proportional breakdown of categories
- Bar Chart: Expense amounts per category
- Line Chart: Financial trend over time

---

## Testing & Extending

Although tests are not currently included, the structure supports:

- Unit testing for "TransactionManager" methods
- Unit testing for "Reports" methods
- Pytest for "MainGui" methods

---

## Notes

- The application saves data to "transactions.csv" automatically.
- Invalid input (like non-numeric amounts) is rejected gracefully.
- Closing the GUI exits the program cleanly.
