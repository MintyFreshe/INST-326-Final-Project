import csv
import os

class TransactionManager():
    
    def __init__(self, csv_file="transactions.csv"):
        self.csv_file = csv_file
        self.fieldnames = ["id", "date", "amount", "category", "description", "type"]

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

                        continue  #skips bad row

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

    def add_transaction(self, date, amount, category, description, txn_type):
        """Add a new transaction to the CSV file

        Args:
            date (str): Transaction date (YYYY-MM-DD)
            amount (float): Amount of the transaction
            category (str): Category label
            description (str): Short description
            txn_type (str): Transaction type ('income' or 'expense')
        """
        transactions = self.load_transactions()
        next_id = max([t["id"] for t in transactions], default=0) + 1

        new_transaction = {
            "id": next_id,
            "date": date,
            "amount": float(amount),
            "category": category,
            "description": description,
            "type": txn_type
        }

        transactions.append(new_transaction)
        self.save_transactions(transactions)

    def get_transactions(self, start_date=None, end_date=None, category=None):
        """Retrieve transactions filtered by date or category

        Args:
            start_date (str, optional): Earliest date to include
            end_date (str, optional): Latest date to include
            category (str, optional): Category to filter

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

            if category and t["category"].lower() != category.lower():

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

    def update_transaction(self, transaction_id, date, amount, category, description, txn_type):
        """Update an existing transaction by ID

        Args:
            transaction_id (int): ID of transaction to update
            date (str): New date
            amount (float): New amount
            category (str): New category
            description (str): New description
            txn_type (str): New type ('income' or 'expense')
        """
        transactions = self.load_transactions()
        for t in transactions:

            if t["id"] == transaction_id:

                t["date"] = date
                t["amount"] = float(amount)
                t["category"] = category
                t["description"] = description
                t["type"] = txn_type
                break

            else:

                raise ValueError(f"Transaction with ID {transaction_id} not found.")

        self.save_transactions(transactions)

