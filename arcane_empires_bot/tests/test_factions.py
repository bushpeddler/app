import unittest
import sqlite3
from game_logic import join_faction

class TestFactionSystem(unittest.TestCase):

    def setUp(self):
        """Set up a test database before each test."""
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE players (id INTEGER PRIMARY KEY, faction TEXT)")
        self.conn.commit()

        # Insert test player
        self.cursor.execute("INSERT INTO players (id, faction) VALUES (1, 'Neutral')")
        self.conn.commit()

    def tearDown(self):
        """Close database connection after each test."""
        self.conn.close()

    def test_faction_assignment(self):
        """Test that a player can successfully join a faction."""
        result = join_faction(1, "Syndicate")
        self.assertIn("✅ You have successfully joined **Syndicate**", result)

        # Verify database change
        self.cursor.execute("SELECT faction FROM players WHERE id = 1")
        faction = self.cursor.fetchone()[0]
        self.assertEqual(faction, "Syndicate")

if __name__ == "__main__":
    unittest.main()