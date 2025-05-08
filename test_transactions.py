import unittest
import os
from transactions import TransactionManager

class TestTransactionManager(unittest.TestCase):

    def setUp(self):
        """Set up a test file and TransactionManager instance"""
        
        self.test_file = "test_transactions.csv"
        self.tm = TransactionManager(csv_file=self.test_file)
        self.sample_data = [
            {"id": 1, "transaction_name": "Groceries", "date": "2025-05-01", "income_expense": "expense", "amount": 50.0, "essential": "yes"},
            {"id": 2, "transaction_name": "Salary", "date": "2025-05-02", "income_expense": "income", "amount": 1000.0, "essential": "no"},
        ]
        self.tm.save_transactions(self.sample_data)

    def tearDown(self):
        """Remove the test file after each test"""

        if os.path.exists(self.test_file):

            os.remove(self.test_file)

    def test_load_transactions(self):
        """Test loading transactions"""

        transactions = self.tm.load_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["transaction_name"], "Groceries")

    def test_add_transaction(self):
        """Test adding a new transaction"""

        self.tm.add_transaction("Book", "2025-05-03", "expense", 25.0, "no")
        transactions = self.tm.load_transactions()
        self.assertEqual(len(transactions), 3)
        self.assertEqual(transactions[-1]["transaction_name"], "Book")

    def test_get_transactions_by_date(self):
        """Test filtering by start and end date"""

        results = self.tm.get_transactions(start_date="2025-05-02")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["transaction_name"], "Salary")

    def test_get_transactions_by_category(self):
        """Test filtering by income/expense category"""

        results = self.tm.get_transactions(category="income")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["transaction_name"], "Salary")

    def test_delete_transaction(self):
        """Test deleting a transaction"""

        self.tm.delete_transaction(1)
        transactions = self.tm.load_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["id"], 2)

    def test_update_transaction(self):
        """Test updating a transaction"""

        self.tm.update_transaction(2, "Freelance", "2025-05-04", "income", 1200.0, "yes")
        transactions = self.tm.load_transactions()
        updated = [t for t in transactions if t["id"] == 2][0]
        self.assertEqual(updated["transaction_name"], "Freelance")
        self.assertEqual(updated["amount"], 1200.0)
        self.assertEqual(updated["essential"], "yes")

    def test_update_transaction_invalid_id(self):
        """Test updating a non-existent transaction"""

        with self.assertRaises(ValueError):

            self.tm.update_transaction(999, "None", "2025-05-05", "income", 0.0, "no")

if __name__ == "__main__":

    unittest.main()
