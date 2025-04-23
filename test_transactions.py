import unittest
import os
from transactions import (
    add_transaction,
    get_transactions,
    delete_transaction,
    update_transaction,
    load_transactions,
    save_transactions
)

class TestTransactionCSV(unittest.TestCase):

    def setUp(self):
        """Set up test data before each test runs

        This ensures that each test starts with a known state — two transactions in the CSV file
        """
    
        self.test_data = [
            {"id": 1, "date": "2025-01-01", "amount": 100.0, "category": "Food", "description": "Groceries", "type": "expense"},
            {"id": 2, "date": "2025-01-02", "amount": 300.0, "category": "Salary", "description": "Monthly pay", "type": "income"},
        ]
        save_transactions(self.test_data)

    def tearDown(self):
        """Clean up after each test by deleting the CSV file to avoid interference between tests

        """
        if os.path.exists("transactions.csv"):
            os.remove("transactions.csv")

    def test_add_transaction(self):
        """Test that a new transaction is added correctly to the CSV file

        - Adds a transport expense
        - Checks that the total number of transactions is now 3
        - Verifies that the last added transaction is categorized correctly
        """
        add_transaction("2025-01-03", 50, "Transport", "Bus", "expense")
        transactions = load_transactions()
        self.assertEqual(len(transactions), 3)
        self.assertEqual(transactions[-1]["category"], "Transport")

    def test_delete_transaction(self):
        """Test that a transaction can be deleted by its ID

        - Deletes the transaction with ID 1
        - Verifies that only one transaction remains.
        - Checks that the remaining transaction has ID 2
        """
        delete_transaction(1)
        transactions = load_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["id"], 2)

    def test_update_transaction(self):
        """Test that a transaction can be updated correctly

        - Updates the transaction with ID 2
        - Verifies that the amount and description fields have been modified
        """
        update_transaction(2, "2025-01-02", 350, "Salary", "Updated pay", "income")
        updated = [t for t in load_transactions() if t["id"] == 2][0]
        self.assertEqual(updated["amount"], 350)
        self.assertEqual(updated["description"], "Updated pay")

if __name__ == '__main__':
    unittest.main()
