"""
postgame.py - Post-Endgame Economy & Player Market Control

✅ Transitions the market after AI control ends.
✅ Enables player-driven financial structures (banks, cartels, governance).
✅ Introduces postgame economic warfare between factions & financial elites.
"""

import sqlite3
import logging
import random

# ✅ Database Path
DB_PATH = "observer_protocol.db"

# ✅ Logging Setup
logging.basicConfig(
    filename="logs/postgame.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ✅ Post-Endgame Factions
POSTGAME_FACTIONS = {
    "Decentralists": "Unregulated free markets—high volatility.",
    "Market Lords": "Elite-controlled financial monopolies.",
    "Crypto-Nomads": "Black-market traders & alternative economies.",
}

def determine_postgame_state():
    """
    Determines the postgame economic state based on final AI outcome.
    Returns:
        str: Economic state description.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ai_status FROM global_state")
            ai_status = cursor.fetchone()

            if ai_status and ai_status[0] == "Active":
                return "AI still controls financial markets—players have limited influence."
            elif ai_status and ai_status[0] == "Faction-Controlled":
                return "Factions dictate financial policies—economic stability depends on ruling faction."
            elif ai_status and ai_status[0] == "Destroyed":
                return "AI is gone—players now shape the market, leading to unpredictable financial shifts."
            else:
                return "Unknown economic state—data corruption or unexpected event detected."

    except Exception as e:
        logging.error(f"❌ Error determining postgame state: {e}")
        return "⚠️ Market status unclear—unexpected error."

def transition_to_player_control():
    """
    Enables player-driven economic structures by allowing banks, cartels, and financial governance.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            
            # ✅ Convert AI-controlled economy into player-driven structures
            cursor.execute("UPDATE market SET price = price * ? WHERE stock IS NOT NULL", (random.uniform(0.8, 1.2),))
            cursor.execute("UPDATE banks SET governance = 'Player-Controlled' WHERE governance = 'AI-Controlled'")
            cursor.execute("UPDATE factions SET economic_power = economic_power + 50 WHERE name IN ('Syndicate', 'Technocrats')")

            conn.commit()
            logging.info("✅ Market transitioned to player control. AI influence removed.")

        return "🌍 The financial world is now ruled by players—markets will evolve dynamically."

    except Exception as e:
        logging.error(f"❌ Transition to player control failed: {e}")
        return "⚠️ Error: Market transition disrupted."

def enable_postgame_factions():
    """
    Introduces new financial factions based on player economic behavior.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()

            # ✅ Insert new postgame factions
            for faction, description in POSTGAME_FACTIONS.items():
                cursor.execute("INSERT OR IGNORE INTO factions (name, description, economic_power) VALUES (?, ?, ?)", 
                               (faction, description, random.randint(50, 200)))
            
            conn.commit()
            logging.info("✅ Postgame factions activated—players can align with new financial entities.")

        return "🏛️ New financial factions have emerged, shaping the future economy."

    except Exception as e:
        logging.error(f"❌ Postgame faction creation failed: {e}")
        return "⚠️ Error: Failed to establish new economic factions."

def trigger_market_war():
    """
    Simulates financial warfare between postgame factions.
    """
    try:
        faction_1, faction_2 = random.sample(list(POSTGAME_FACTIONS.keys()), 2)
        impact = random.choice(["Currency War", "Stock Market Manipulation", "Economic Collapse", "Trade Embargo"])
        
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE factions SET economic_power = economic_power - 20 WHERE name = ?", (faction_1,))
            cursor.execute("UPDATE factions SET economic_power = economic_power + 20 WHERE name = ?", (faction_2,))
            conn.commit()
        
        logging.info(f"⚔️ {faction_1} & {faction_2} are engaged in a {impact}!")
        return f"🔥 **Market War Alert:** {faction_1} & {faction_2} are battling through {impact}!"

    except Exception as e:
        logging.error(f"❌ Market war failed: {e}")
        return "⚠️ Error: Market war scenario disrupted."

if __name__ == "__main__":
    print(determine_postgame_state())
    print(transition_to_player_control())
    print(enable_postgame_factions())
    print(trigger_market_war())