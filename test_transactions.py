import unittest
import os
from transactions import TransactionManager

class TestTransactionManager(unittest.TestCase):

    def setUp(self):
        """Set up sample data before each test"""
        self.tm = TransactionManager()
        self.initial_data = [
            {"id": 1, "date": "2025-01-01", "amount": 100.0, "category": "Food", "description": "Groceries", "type": "expense"},
            {"id": 2, "date": "2025-01-02", "amount": 200.0, "category": "Salary", "description": "Job income", "type": "income"},
            {"id": 3, "date": "2025-01-03", "amount": 50.0, "category": "Transport", "description": "Bus fare", "type": "expense"}
        ]

        self.tm.save_transactions(self.initial_data)

    def tearDown(self):
        """Clean up after each test"""

        if os.path.exists("transactions.csv"):

            os.remove("transactions.csv")

    def test_load_transactions(self):
        """Test that transactions are correctly loaded from the CSV file."""

        transactions = self.tm.load_transactions()
        self.assertEqual(len(transactions), 3)
        self.assertEqual(transactions[0]["category"], "Food")

    def test_add_transaction(self):
        """Test adding a new transaction and verify it's written correctly."""

        self.tm.add_transaction("2025-01-04", 75.0, "Utilities", "Electric bill", "expense")
        transactions = self.tm.load_transactions()
        self.assertEqual(len(transactions), 4)
        self.assertEqual(transactions[-1]["description"], "Electric bill")

    def test_delete_transaction(self):
        """Test deleting a transaction by ID and verify it's removed."""

        self.tm.delete_transaction(2)
        transactions = self.tm.load_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertNotIn(2, [t["id"] for t in transactions])

    def test_update_transaction(self):
        """Test updating an existing transaction's amount and description."""

        self.tm.update_transaction(1, "2025-01-10", 150.0, "Food", "Updated groceries", "expense")
        updated = [t for t in self.tm.load_transactions() if t["id"] == 1][0]
        self.assertEqual(updated["amount"], 150.0)
        self.assertEqual(updated["description"], "Updated groceries")

    def test_get_transactions_date_filter(self):
        """Test filtering transactions by a date range."""

        results = self.tm.get_transactions(start_date="2025-01-02", end_date="2025-01-03")
        self.assertEqual(len(results), 2)
        self.assertTrue(all(r["date"] >= "2025-01-02" and r["date"] <= "2025-01-03" for r in results))

    def test_get_transactions_category_filter(self):
        """Test filtering transactions by a category (case-insensitive)."""

        results = self.tm.get_transactions(category="Transport")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["description"], "Bus fare")

    def test_get_transactions_combined_filters(self):
        """Test filtering by both date range and category."""

        results = self.tm.get_transactions(start_date="2025-01-01", end_date="2025-01-03", category="Food")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["category"], "Food")

if __name__ == '__main__':
    unittest.main()
