import csv
import os

def load_transactions():
    """Load all transactions from the CSV file.

    Returns:
        list[dict]: A list of transactions as dictionaries.
    """
    pass

def save_transactions(data):
    """Save a list of transaction dictionaries to the CSV file.

    Args:
        data (list[dict]): Transactions to write to file.
    """
    pass

def add_transaction(date, amount, category, description, type_):
    """Add a new transaction to the CSV file.

    Args:
        date (str): Transaction date (YYYY-MM-DD).
        amount (float): Amount of the transaction.
        category (str): Category label.
        description (str): Short description.
        type_ (str): Transaction type ('income' or 'expense').
    """
    pass

def get_transactions(start_date=None, end_date=None, category=None):
    """Retrieve transactions filtered by date or category.

    Args:
        start_date (str, optional): Earliest date to include.
        end_date (str, optional): Latest date to include.
        category (str, optional): Category to filter.

    Returns:
        list[dict]: Matching transactions.
    """
    pass

def delete_transaction(transaction_id):
    """Delete a transaction by ID.

    Args:
        transaction_id (int): The transaction ID to delete.
    """
    pass

def update_transaction(transaction_id, date, amount, category, description, type_):
    """Update an existing transaction by ID.

    Args:
        transaction_id (int): ID of transaction to update.
        date (str): New date.
        amount (float): New amount.
        category (str): New category.
        description (str): New description.
        type_ (str): New type ('income' or 'expense').
    """
    pass