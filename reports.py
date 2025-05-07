import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_total_income(transactions):
    return sum(float(t["amount"]) for t in transactions if t["income/expense"] == "income")

def calculate_total_expenses(transactions):
    return sum(float(t["amount"]) for t in transactions if t["income/expense"] == "expense")

def calculate_balance(transactions):
    return calculate_total_income(transactions) - calculate_total_expenses(transactions)

def get_monthly_summary(transactions):
    summary = defaultdict(lambda: {"income": 0, "expense": 0})
    for t in transactions:
        month = t["date"][:7]
        if t["income/expense"] == "income":
            summary[month]["income"] += float(t["amount"])
        elif t["income/expense"] == "expense":
            summary[month]["expense"] += float(t["amount"])
    return dict(summary)

def get_category_summary(transactions):
    summary = defaultdict(float)
    for t in transactions:
        summary[t["transaction name"]] += float(t["amount"])
    return dict(summary)

def get_top_expenses(transactions, n=5):
    expenses = [t for t in transactions if t["income/expense"] == "expense"]
    return sorted(expenses, key=lambda t: float(t["amount"]), reverse=True)[:n]

def export_summary_to_csv(summary_dict, filename="summary_report.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "Value"])
        for key, value in summary_dict.items():
            writer.writerow([key, value])

def plot_expense_pie(transactions):
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
