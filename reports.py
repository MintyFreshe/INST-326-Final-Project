import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime




def load_transactions_from_csv(filename):
    """
    Load transactions from a CSV file and return a list of dictionaries.
    Each row becomes a dictionary with string values.
    """
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def calculate_total_income(transactions):
    """
    Calculate the total income from a list of transactions.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        float: Total income amount.
    """
    return sum(float(t["amount"]) for t in transactions if t["income/expense"] == "income")

def calculate_total_expenses(transactions):
    """
    Calculate the total expenses from a list of transactions.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        float: Total expense amount.
    """
    return sum(float(t["amount"]) for t in transactions if t["income/expense"] == "expense")

def calculate_balance(transactions):
    """
    Calculate the current balance based on income and expenses.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        float: Net balance (income - expenses).
    """
    return calculate_total_income(transactions) - calculate_total_expenses(transactions)

def get_monthly_summary(transactions):
    """
    Summarize income and expenses for each month.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        dict: Dictionary with month keys and income/expense totals.
    """
    summary = defaultdict(lambda: {"income": 0, "expense": 0})
    for t in transactions:
        month = t["date"][:7]
        if t["income/expense"] == "income":
            summary[month]["income"] += float(t["amount"])
        elif t["income/expense"] == "expense":
            summary[month]["expense"] += float(t["amount"])
    return dict(summary)

def get_category_summary(transactions):
    """
    Summarize total transaction amounts by category.

    Args:
        transactions (list): List of transaction dictionaries.

    Returns:
        dict: Dictionary of categories with summed amounts.
    """
    summary = defaultdict(float)
    for t in transactions:
        summary[t["transaction name"]] += float(t["amount"])
    return dict(summary)

def get_top_expenses(transactions, n=5):
    """
    Retrieve the top N largest expense transactions.

    Args:
        transactions (list): List of transaction dictionaries.
        n (int): Number of top expenses to return.

    Returns:
        list: Top N expense transaction dictionaries.
    """
    expenses = [t for t in transactions if t["income/expense"] == "expense"]
    return sorted(expenses, key=lambda t: float(t["amount"]), reverse=True)[:n]

def export_summary_to_csv(summary_dict, filename="summary_report.csv"):
    """
    Export a summary dictionary to a CSV file.

    Args:
        summary_dict (dict): Summary data to write.
        filename (str): Name of the output CSV file.
    """
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "Value"])
        for key, value in summary_dict.items():
            writer.writerow([key, value])

def plot_expense_pie(transactions):
    """
    Generate and display a pie chart of expenses by category.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    category_totals = defaultdict(float)
    for t in transactions:
        if t["income/expense"] == "expense":
            category_totals[t["transaction name"]] += float(t["amount"])

    if not category_totals:
        print("No expenses to plot.")
        return

    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Expenses by Category")
    plt.axis("equal")
    plt.show()

def plot_cumulative_balance(transactions):
    """
    Generate and display a line chart of cumulative balance over time.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    transactions_sorted = sorted(transactions, key=lambda x: x["date"])
    balance = 0
    dates = []
    balances = []

    for t in transactions_sorted:
        if t["income/expense"] == "income":
            balance += float(t["amount"])
        elif t["income/expense"] == "expense":
            balance -= float(t["amount"])
        dates.append(datetime.strptime(t["date"], "%Y-%m-%d"))
        balances.append(balance)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, balances, marker="o")
    plt.title("Cumulative Balance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Balance")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_stacked_expense_categories(transactions):
    """
    Generate and display a stacked bar chart of monthly expenses by category.

    Args:
        transactions (list): List of transaction dictionaries.
    """
    import pandas as pd

    expenses = [t for t in transactions if t["income/expense"] == "expense"]
    data = defaultdict(lambda: defaultdict(float))

    for t in expenses:
        month = t["date"][:7]
        data[month][t["transaction name"]] += float(t["amount"])

    df = pd.DataFrame(data).T.fillna(0).sort_index()

    df.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.title("Monthly Expenses by Category")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title="Category")
    plt.show()
    
    
    
    
if __name__ == "__main__":
    transactions = load_transactions_from_csv("sample_transactions.csv")

    print("Total Income:", calculate_total_income(transactions))
    print("Total Expenses:", calculate_total_expenses(transactions))
    print("Net Balance:", calculate_balance(transactions))

    print("\nMonthly Summary:")
    for month, values in get_monthly_summary(transactions).items():
        print(f"{month}: Income = ${values['income']:.2f}, Expenses = ${values['expense']:.2f}")

    print("\nTop Expenses:")
    for t in get_top_expenses(transactions):
        print(f"{t['date']} - {t['transaction name']} - ${t['amount']}")

    plot_expense_pie(transactions)
    plot_cumulative_balance(transactions)
    plot_stacked_expense_categories(transactions)
