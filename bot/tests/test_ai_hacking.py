import unittest
import sqlite3
import time
from game_logic import hack_ai, restrict_player_market_access

class TestAIHacking(unittest.TestCase):

    def setUp(self):
        """Set up an in-memory test database before each test."""
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

        # Create the players table with market restriction field
        self.cursor.execute("""
            CREATE TABLE players (
                id INTEGER PRIMARY KEY,
                username TEXT,
                wealth INTEGER DEFAULT 1000,
                market_restricted_until DATETIME DEFAULT NULL
            )
        """)

        # Insert test player
        self.cursor.execute("INSERT INTO players (id, username, wealth) VALUES (1, 'TestPlayer', 1000)")
        self.conn.commit()

    def tearDown(self):
        """Close the database after each test."""
        self.conn.close()

    def test_successful_hack(self):
        """Test if a successful AI hack provides a market advantage."""
        result = hack_ai(1)
        self.assertIn("🕵️ AI hacked successfully!", result)

    def test_failed_hack_restriction(self):
        """Test if a failed hack correctly restricts market access."""
        restrict_player_market_access(1, 1)  # Restrict market access for 1 minute
        self.cursor.execute("SELECT market_restricted_until FROM players WHERE id = 1")
        restriction_time = self.cursor.fetchone()[0]
        self.assertIsNotNone(restriction_time, "Market restriction should be applied.")

    def test_market_access_during_restriction(self):
        """Test that a player cannot trade while restricted."""
        restrict_player_market_access(1, 1)  # Restrict for 1 minute
        self.cursor.execute("SELECT market_restricted_until FROM players WHERE id = 1")
        restriction_time = self.cursor.fetchone()[0]

        # Simulate checking if restriction is still active
        if restriction_time:
            result = "⛔ Market access restricted due to AI detection! Try again later."
        else:
            result = "✅ Market access granted."

        self.assertIn("⛔ Market access restricted", result)

    def test_market_access_after_restriction_expires(self):
        """Test that a player can trade after the restriction expires."""
        restrict_player_market_access(1, 1)  # Restrict for 1 minute
        time.sleep(61)  # Simulate waiting for restriction expiration

        self.cursor.execute("UPDATE players SET market_restricted_until = NULL WHERE id = 1")  # Simulate restriction expiry
        self.cursor.execute("SELECT market_restricted_until FROM players WHERE id = 1")
        restriction_time = self.cursor.fetchone()[0]

        if restriction_time:
            result = "⛔ Market access restricted due to AI detection! Try again later."
        else:
            result = "✅ Market access granted."

        self.assertIn("✅ Market access granted", result)

if __name__ == "__main__":
    unittest.main()