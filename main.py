"""
Main entry point for the Personal Finance Tracker application.

This module provides two main functionalities:
1. Launching the GUI for interactive use.
2. Running reports from the command line for summary and visualization.

Usage:
    python main.py           # Launches the GUI
    python main.py reports   # Runs reports in the console
"""

import sys
from gui import MainGui
from reports import Reports

def run_gui():
    """
    Launches the main graphical user interface (GUI) of the application.
    """
    app = MainGui()
    app.root.mainloop()

def run_reports():
    """
    Runs financial reports in the console, including:
    - Total income, expenses, and net balance
    - Monthly summary
    - Top expenses
    - Expense and balance visualizations

    Loads transactions from 'transactions.csv'.
    """
    reports = Reports()
    transactions = reports.load_transactions_from_csv("transactions.csv")

    print("Total Income:", reports.calculate_total_income(transactions))
    print("Total Expenses:", reports.calculate_total_expenses(transactions))
    print("Net Balance:", reports.calculate_balance(transactions))

    print("\nMonthly Summary:")
    for month, values in reports.get_monthly_summary(transactions).items():
        print(f"{month}: Income = ${values['income']:.2f}, Expenses = ${values['expense']:.2f}")

    print("\nTop Expenses:")
    for t in reports.get_top_expenses(transactions):
        print(f"{t['date']} - {t['transaction_name']} - ${t['amount']}")

    reports.plot_expense_pie(transactions)
    reports.plot_cumulative_balance(transactions)
    reports.plot_stacked_expense_categories(transactions)

def main():
    """
    Main function to determine the mode of operation.

    If the first command-line argument is 'reports', runs reports in the console.
    Otherwise, launches the GUI.
    """
    if len(sys.argv) > 1 and sys.argv[1] == "reports":
        run_reports()
    else:
        run_gui()

if __name__ == "__main__":
    main()








