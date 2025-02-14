"""
app.py - Arcane Empires Web Dashboard

This Flask web server provides real-time stock prices, player portfolios, and AI analytics.
"""

from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# 📈 Fetch live stock prices from the database
def get_market_data():
    with sqlite3.connect("../telegram_mini_game/observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT stock, price FROM market")
        market_data = cursor.fetchall()
    return [{"stock": stock, "price": price} for stock, price in market_data]

# 💰 Fetch player portfolio data
def get_player_data():
    with sqlite3.connect("../telegram_mini_game/observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username, wealth FROM players ORDER BY wealth DESC")
        player_data = cursor.fetchall()
    return [{"username": user, "wealth": wealth} for user, wealth in player_data]

# 🎭 Fetch faction influence
def get_faction_influence():
    with sqlite3.connect("../telegram_mini_game/observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT faction, COUNT(*) FROM players GROUP BY faction")
        faction_data = cursor.fetchall()
    return [{"faction": faction, "count": count} for faction, count in faction_data]

# API Endpoint: Stock Prices
@app.route("/api/market")
def market():
    return jsonify(get_market_data())

# API Endpoint: Player Portfolio
@app.route("/api/players")
def players():
    return jsonify(get_player_data())

# API Endpoint: Faction Influence
@app.route("/api/factions")
def factions():
    return jsonify(get_faction_influence())

# 🌍 Render the main dashboard
@app.route("/")
def dashboard():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)