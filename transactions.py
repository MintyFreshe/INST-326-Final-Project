import csv
import os

class TransactionManager:

    def __init__(self, csv_file="transactions.csv"):

        self.csv_file = csv_file
        self.fieldnames = ['Name', 'Budget', 'Food', 'Transport', 'Housing', 'Entertainment', 'Savings', 'Miscellaneous']

    def load_transactions(self):
        """Load all transactions from the CSV file."""

        transactions = []
        if os.path.exists(self.csv_file):

            with open(self.csv_file, mode='r', newline='') as file:

                reader = csv.DictReader(file)
                for row in reader:

                    try:

                        for field in ['Budget', 'Food', 'Transport', 'Housing', 'Entertainment', 'Savings', 'Miscellaneous']:
                            row[field] = float(row[field])

                    except ValueError:

                        continue  # skip bad rows

                    transactions.append(row)

        return transactions

    def save_transactions(self, data):
        """Save a list of transaction dictionaries to the CSV file."""

        with open(self.csv_file, mode='w', newline='') as file:

            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for row in data:

                row_str = {key: str(row[key]) for key in self.fieldnames}
                writer.writerow(row_str)

    def add_transaction(self, name, budget, food, transport, housing, entertainment, savings, miscellaneous):
        """Add a new transaction to the CSV file."""

        transactions = self.load_transactions()
        new_transaction = {
            'Name': name,
            'Budget': float(budget),
            'Food': float(food),
            'Transport': float(transport),
            'Housing': float(housing),
            'Entertainment': float(entertainment),
            'Savings': float(savings),
            'Miscellaneous': float(miscellaneous)
        }
        transactions.append(new_transaction)
        self.save_transactions(transactions)

    def get_transactions(self):
        """Return all transactions."""

        return self.load_transactions()

    def delete_transaction(self, name):
        """Delete a transaction by name."""

        transactions = self.load_transactions()
        updated = [t for t in transactions if t["Name"] != name]
        self.save_transactions(updated)

    def update_transaction(self, name, updated_data):
        """
        Update a transaction by name.

        Args:
            name (str): Name of transaction to update
            updated_data (dict): Dictionary of updated values
        """
        transactions = self.load_transactions()
        for t in transactions:

            if t["Name"] == name:

                for field in self.fieldnames:

                    if field in updated_data:

                        t[field] = updated_data[field]

                break
            
        self.save_transactions(transactions)
