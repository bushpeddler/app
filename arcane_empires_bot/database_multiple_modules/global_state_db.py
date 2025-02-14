def init_global_state_table(conn):
    """
    Initializes the global economy state table.
    """
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS global_state (
            ai_status TEXT DEFAULT 'Active'
        )
    """)