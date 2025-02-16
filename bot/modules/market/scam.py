# market_scam.py - AI-led pump-and-dump schemes, deception trading

import sqlite3
import random
from market.blacklist_scam import is_blacklisted, add_to_blacklist
from market.multi_stock_scam import trigger_multi_stock_scam
from market.scam_countermeasures import has_scam_protection
from market.fake_orders import create_fake_orders  # ✅ Imported fake order manipulation

DB_PATH = "observer_protocol.db"

def trigger_pump_and_dump(player_id):
    """AI manipulates stock prices by creating artificial demand."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    stock = "Cyber Credits"
    pump_chance = random.randint(1, 100)

    if is_blacklisted(player_id):  # Prevents scamming the same player twice
        return f"⚠️ {stock} scam failed—Player already aware of manipulation."

    if has_scam_protection(player_id):  # Checks if player invested in scam detection
        return f"🛡️ Scam detection active—{stock} manipulation neutralized!"

    if pump_chance > 70:  # 30% chance of a true pump-and-dump event
        cursor.execute("UPDATE market SET price = price * 2 WHERE stock = ?", (stock,))
        event = f"🚀 AI creates a **Pump and Dump!** {stock} skyrockets!"
        add_to_blacklist(player_id)  # Mark player as scammed
    else:
        event = f"📉 Fake hype detected—{stock} price remains unchanged."

    conn.commit()
    conn.close()

    return event

if __name__ == "__main__":
    print(trigger_pump_and_dump(1))
    print(trigger_multi_stock_scam(1))
    print(create_fake_orders())  # ✅ Now executes fake order creation