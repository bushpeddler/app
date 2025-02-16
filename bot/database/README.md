📘 README: Observer Protocol Database System

✅ Version: Updated for the latest database structure
✅ Purpose: This document explains how the Observer Protocol database system is structured, how tables are initialized, and how data is managed within the game.

🔹 Overview

The database is the backbone of the Observer Protocol’s economy, factions, and AI interactions. It stores all key gameplay data, including:
	•	Player information (wealth, faction)
	•	Market fluctuations & trading history
	•	AI-driven global economy states
	•	Faction conflicts and war history

The database is managed using SQLite, with initialization handled in init_db.py.

🔹 Database Files & Their Purpose

📂 bot/database/ (Stores all database-related scripts)
Each script below is responsible for initializing a table in observer_protocol.db.

File	Purpose
init_db.py	🚀 Master initializer for all database tables
users_db.py	🏛 Stores player data (wealth, faction, ID)
market_db.py	📈 Manages stock market data
trade_hx_db.py	📜 Logs trade history (who bought what, when)
global_state_db.py	🌎 Tracks AI-driven global economic shifts
faction_war_db.py	⚔️ Stores outcomes of faction battles

🔹 Table Structures

🧑‍💼 players Table (users_db.py)

Stores player data, including financial status and faction alignment.

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    username TEXT,
    wealth INTEGER DEFAULT 1000,
    faction TEXT DEFAULT 'Neutral'
);

🔹 Columns Explained:
	•	id → Unique player ID
	•	username → Player’s in-game name
	•	wealth → Current wealth in credits
	•	faction → Player’s chosen faction (Neutral by default)

📊 market Table (market_db.py)

Manages stock values within the in-game economy.

CREATE TABLE IF NOT EXISTS market (
    stock TEXT PRIMARY KEY,
    price INTEGER DEFAULT 100
);

🔹 Columns Explained:
	•	stock → Stock name (e.g., “Quantum Energy”)
	•	price → Current price of the stock

📜 trade_history Table (trade_hx_db.py)

Records all trades made by players.

CREATE TABLE IF NOT EXISTS trade_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    stock TEXT,
    amount INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

🔹 Columns Explained:
	•	id → Auto-generated trade ID
	•	player_id → Player who made the trade
	•	stock → Stock traded
	•	amount → Number of shares bought/sold
	•	timestamp → Time trade was executed

🌎 global_state Table (global_state_db.py)

Tracks major AI-driven economic shifts.

CREATE TABLE IF NOT EXISTS global_state (
    ai_status TEXT DEFAULT 'Active'
);

🔹 Columns Explained:
	•	ai_status → Whether AI is Active, Malfunctioning, or Collapsing

⚔️ faction_war Table (faction_war_db.py)

Logs faction battles and war outcomes.

CREATE TABLE IF NOT EXISTS faction_war (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faction_one TEXT,
    faction_two TEXT,
    outcome TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

🔹 Columns Explained:
	•	id → Unique war event ID
	•	faction_one → First faction in the conflict
	•	faction_two → Opposing faction
	•	outcome → Who won or the result of the battle
	•	timestamp → When the battle occurred

🔹 Initializing the Database

Run the following command to set up all database tables at once:

python init_db.py

🔹 Verifying the Database

To check if tables were created successfully, run:

sqlite3 observer_protocol.db
.tables  # Should display all tables

To inspect specific tables:

SELECT * FROM market;
SELECT * FROM players;
SELECT * FROM trade_history;

🔹 Next Steps

1️⃣ Ensure init_db.py is always run before using the database.
2️⃣ Double-check database paths to prevent connection errors.
3️⃣ If new features require more tables, update init_db.py accordingly.

🎯 Final Thought:
This database structure provides a strong foundation for player interactions, AI-driven market behaviors, and faction conflicts. It will continue evolving as new mechanics are introduced.