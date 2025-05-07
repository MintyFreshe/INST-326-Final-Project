import csv
import os

class TransactionManager():

    def __init__(self, csv_file="transactions.csv"):

        self.csv_file = csv_file
        self.fieldnames = ["id", "transaction_name", "date", "income_expense", "amount", "essential"]

    def load_transactions(self):
        """Load all transactions from the CSV file

        Returns:
            list[dict]: A list of transactions as dictionaries
        """
        transactions = []
        if os.path.exists(self.csv_file):

            with open(self.csv_file, mode='r', newline='') as file:

                reader = csv.DictReader(file)
                for row in reader:

                    try:

                        row["id"] = int(row["id"])
                        row["amount"] = float(row["amount"])

                    except ValueError:

                        continue  # skips bad row

                    transactions.append(row)

        return transactions

    def save_transactions(self, data):
        """Save a list of transaction dictionaries to the CSV file

        Args:
            data (list[dict]): Transactions to write to file
        """
        with open(self.csv_file, mode='w', newline='') as file:

            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for row in data:

                row_str = {key: str(row[key]) for key in self.fieldnames}
                writer.writerow(row_str)

    def add_transaction(self, transaction_name, date, income_expense, amount, essential):
        """Add a new transaction to the CSV file

        Args:
            transaction_name (str): Name/label for the transaction
            date (str): Transaction date (YYYY-MM-DD)
            income_expense (str): 'income' or 'expense'
            amount (float): Transaction amount
            essential (str): 'yes' or 'no'
        """
        transactions = self.load_transactions()
        next_id = max([t["id"] for t in transactions], default=0) + 1

        new_transaction = {
            "id": next_id,
            "transaction_name": transaction_name,
            "date": date,
            "income_expense": income_expense,
            "amount": float(amount),
            "essential": essential
        }

        transactions.append(new_transaction)
        self.save_transactions(transactions)

    def get_transactions(self, start_date=None, end_date=None, category=None):
        """Retrieve transactions filtered by date or category

        Args:
            start_date (str, optional): Earliest date to include
            end_date (str, optional): Latest date to include
            category (str, optional): Category (income/expense) to filter

        Returns:
            list[dict]: Matching transactions
        """
        transactions = self.load_transactions()
        filtered = []
        for t in transactions:

            if start_date and t["date"] < start_date:
                continue

            if end_date and t["date"] > end_date:
                continue

            if category and t["income_expense"].lower() != category.lower():
                continue

            filtered.append(t)

        return filtered

    def delete_transaction(self, transaction_id):
        """Delete a transaction by ID

        Args:
            transaction_id (int): The transaction ID to delete
        """
        transactions = self.load_transactions()
        updated = [t for t in transactions if t["id"] != transaction_id]
        self.save_transactions(updated)

    def update_transaction(self, transaction_id, transaction_name, date, income_expense, amount, essential):
        """Update an existing transaction by ID

        Args:
            transaction_id (int): ID of transaction to update
            transaction_name (str): New transaction name
            date (str): New date
            income_expense (str): New type ('income' or 'expense')
            amount (float): New amount
            essential (str): 'yes' or 'no'
        """
        transactions = self.load_transactions()
        found = False
        for t in transactions:

            if t["id"] == transaction_id:
                t["transaction_name"] = transaction_name
                t["date"] = date
                t["income_expense"] = income_expense
                t["amount"] = float(amount)
                t["essential"] = essential
                found = True
                break

        if not found:

            raise ValueError(f"Transaction with ID {transaction_id} not found.")
        
        self.save_transactions(transactions)


