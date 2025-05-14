import csv
import os

class TransactionManager:

    def __init__(self, csv_file="transactions.csv"):

        self.csv_file = csv_file
        self.fieldnames = ['id', 'transaction_name', 'transaction_category', 'date', 'income_expense', 'amount', 'essential']

    def load_transactions(self):
        """Load all transactions from the CSV file."""

        transactions = []
        if os.path.exists(self.csv_file):

            with open(self.csv_file, mode='r', newline='') as file:

                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Convert amount to float
                        row['amount'] = float(row['amount'])
                        transactions.append(row)
                    except (ValueError, KeyError) as e:
                        continue  # skip bad rows
        return transactions

    def save_transactions(self, data):
        """Save a list of transaction dictionaries to the CSV file."""
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def add_transaction(self, name, transaction_category, date, income_expense, amount, essential):
        """Add a new transaction to the CSV file."""

        transactions = self.load_transactions()
        
        # Generate new ID
        new_id = 1
        if transactions:
            new_id = max(int(t['id']) for t in transactions) + 1
            
        new_transaction = {
            'id': str(new_id),
            'transaction_name': name,
            'transaction_category': transaction_category,
            'date': date,
            'income_expense': income_expense,
            'amount': str(amount),
            'essential': essential
        }
        transactions.append(new_transaction)
        self.save_transactions(transactions)

    def get_transactions(self):
        """Return all transactions."""

        return self.load_transactions()

    def delete_transaction(self, transaction_id):
        """Delete a transaction by ID."""
        transactions = self.load_transactions()
        updated = [t for t in transactions if t['id'] != str(transaction_id)]
        self.save_transactions(updated)

    def update_transaction(self, transaction_id, updated_data):
        """
        Update a transaction by ID.

        Args:
            transaction_id (str): ID of transaction to update
            updated_data (dict): Dictionary of updated values
        """
        transactions = self.load_transactions()
        for t in transactions:
            if t['id'] == str(transaction_id):
                for field in self.fieldnames:

                    if field in updated_data:
                        t[field] = str(updated_data[field])
                break
            
        self.save_transactions(transactions)
