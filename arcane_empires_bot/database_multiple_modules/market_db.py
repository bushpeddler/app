def init_market_table(conn):
    """
    Initializes the market stocks table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market (
            stock TEXT PRIMARY KEY,
            price INTEGER DEFAULT 100
        )
    """)