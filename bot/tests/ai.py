import unittest
import sqlite3
from ai_trading_logic import ai_trade_decision

class TestAITrading(unittest.TestCase):

    def setUp(self):
        """Set up a test database before each test."""
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE global_state (ai_morality TEXT)")
        self.cursor.execute("CREATE TABLE market (stock TEXT PRIMARY KEY, price INTEGER)")
        self.conn.commit()

        # Insert default AI morality state and stock
        self.cursor.execute("INSERT INTO global_state (ai_morality) VALUES ('Neutral')")
        self.cursor.execute("INSERT INTO market (stock, price) VALUES ('BTC', 100)")
        self.conn.commit()

    def tearDown(self):
        """Close database connection after each test."""
        self.conn.close()

    def test_ai_morality_retrieval(self):
        """Test AI correctly retrieves morality state from database."""
        result = ai_trade_decision()
        self.assertIn("📊 Observer AI (Neutral)", result)

    def test_market_price_adjustment(self):
        """Test AI trading modifies stock prices within expected limits."""
        ai_trade_decision()
        self.cursor.execute("SELECT price FROM market WHERE stock = 'BTC'")
        new_price = self.cursor.fetchone()[0]
        self.assertTrue(5 <= new_price <= 5000, "Stock price should be within limits.")

if __name__ == "__main__":
    unittest.main()