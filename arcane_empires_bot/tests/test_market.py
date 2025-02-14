import unittest
import sqlite3
from game_logic import trade

class TestMarketTrading(unittest.TestCase):

    def setUp(self):
        """Set up a test database before each test."""
        self.conn = sqlite3.connect(":memory:")  # Use an in-memory database for testing
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE players (id INTEGER PRIMARY KEY, wealth INTEGER)")
        self.cursor.execute("CREATE TABLE market (stock TEXT PRIMARY KEY, price INTEGER)")
        self.cursor.execute("CREATE TABLE trade_history (id INTEGER PRIMARY KEY, player_id INTEGER, stock TEXT, amount INTEGER)")
        self.conn.commit()

        # Insert test player and stock
        self.cursor.execute("INSERT INTO players (id, wealth) VALUES (1, 1000)")
        self.cursor.execute("INSERT INTO market (stock, price) VALUES ('BTC', 50)")
        self.conn.commit()

    def tearDown(self):
        """Close database connection after each test."""
        self.conn.close()

    def test_successful_trade(self):
        """Test a successful stock trade."""
        result = trade(1, 'BTC', 10)  # Buy 10 BTC at 50 credits each
        self.assertIn("✅ Trade successful!", result)

    def test_insufficient_funds(self):
        """Test trade rejection due to insufficient funds."""
        result = trade(1, 'BTC', 100)  # Trying to buy more than player can afford
        self.assertIn("❌ Insufficient funds", result)

    def test_invalid_stock(self):
        """Test trade rejection for an invalid stock."""
        result = trade(1, 'ETH', 5)  # ETH doesn't exist in market
        self.assertIn("❌ Stock 'ETH' not found!", result)

if __name__ == "__main__":
    unittest.main()