import sqlite3
from database_modules.players_db import init_players_table
from database_modules.market_db import init_market_table
from database_modules.trade_history_db import init_trade_history_table
from database_modules.global_state_db import init_global_state_table
from database_modules.faction_war_db import init_faction_war_table

def init_db():
    """
    Initializes all database tables.
    """
    conn = sqlite3.connect("observer_protocol.db")
    init_players_table(conn)
    init_market_table(conn)
    init_trade_history_table(conn)
    init_global_state_table(conn)
    init_faction_war_table(conn)
    conn.commit()
    conn.close()