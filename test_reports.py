import unittest
from collections import defaultdict
from datetime import datetime

transactions_sample = [
    {"id": 1, "date": "2025-01-01", "amount": 100.0, "category": "Food", "description": "Groceries", "type": "expense"},
    {"id": 2, "date": "2025-01-02", "amount": 200.0, "category": "Salary", "description": "January salary", "type": "income"},
    {"id": 3, "date": "2025-01-15", "amount": 50.0, "category": "Transport", "description": "Bus fare", "type": "expense"},
    {"id": 4, "date": "2025-02-01", "amount": 150.0, "category": "Salary", "description": "February salary", "type": "income"},
]


def calculate_total_income(transactions):
    return sum(t["amount"] for t in transactions if t["type"] == "income")

def calculate_total_expenses(transactions):
    return sum(t["amount"] for t in transactions if t["type"] == "expense")

def calculate_balance(transactions):
    return calculate_total_income(transactions) - calculate_total_expenses(transactions)

def get_monthly_summary(transactions):
    summary = defaultdict(lambda: {"income": 0, "expense": 0})
    for t in transactions:
        month = t["date"][:7]
        summary[month][t["type"]] += t["amount"]
    return dict(summary)

def get_category_summary(transactions):
    summary = defaultdict(float)
    for t in transactions:
        summary[t["category"]] += t["amount"]
    return dict(summary)

def get_top_expenses(transactions, n=5):
    expenses = [t for t in transactions if t["type"] == "expense"]
    return sorted(expenses, key=lambda t: t["amount"], reverse=True)[:n]

# Define the test cases
class TestReportsFunctions(unittest.TestCase):

    def test_total_income(self):
        self.assertEqual(calculate_total_income(transactions_sample), 350.0)

    def test_total_expenses(self):
        self.assertEqual(calculate_total_expenses(transactions_sample), 150.0)

    def test_balance(self):
        self.assertEqual(calculate_balance(transactions_sample), 200.0)

    def test_monthly_summary(self):
        summary = get_monthly_summary(transactions_sample)
        self.assertEqual(summary["2025-01"]["income"], 200.0)
        self.assertEqual(summary["2025-01"]["expense"], 150.0)
        self.assertEqual(summary["2025-02"]["income"], 150.0)

    def test_category_summary(self):
        summary = get_category_summary(transactions_sample)
        self.assertEqual(summary["Food"], 100.0)
        self.assertEqual(summary["Salary"], 350.0)

    def test_top_expenses(self):
        top_exp = get_top_expenses(transactions_sample, n=1)
        self.assertEqual(top_exp[0]["amount"], 100.0)
        self.assertEqual(top_exp[0]["category"], "Food")

if __name__ == '__main__':
    unittest.main()
