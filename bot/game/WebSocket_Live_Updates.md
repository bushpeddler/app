📜 WebSocket Live Updates Development Plan

📂 Location: /docs/WebSocket_Live_Updates.md
📌 Purpose: This document outlines all necessary files and modifications for integrating WebSocket-based real-time updates into Arcane Empires.

📂 New Files Required (3-4)

These files will enable live updates for stock prices, AI decisions, and faction influence.

1️⃣ websocket_server.py

📂 Location: /web_dashboard/websocket_server.py
📌 Purpose: Runs a WebSocket server to handle real-time communication between the backend and frontend.

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print("Client connected.")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected.")

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)

2️⃣ static/websocket_client.js

📂 Location: /web_dashboard/static/websocket_client.js
📌 Purpose: JavaScript WebSocket client to receive real-time updates in the browser.

const socket = io("http://127.0.0.1:5001");

socket.on("stock_update", (data) => {
    document.getElementById("stockPrices").innerText = JSON.stringify(data, null, 2);
});

socket.on("faction_update", (data) => {
    document.getElementById("factionInfluence").innerText = JSON.stringify(data, null, 2);
});

socket.on("ai_event", (data) => {
    document.getElementById("aiEvents").innerText = data;
});

3️⃣ socket_events.py

📂 Location: /telegram_mini_game/socket_events.py
📌 Purpose: Triggers stock price updates and faction shifts based on market events.

from flask_socketio import SocketIO
import sqlite3

socketio = SocketIO(message_queue="redis://")  # Redis for scalability

def send_stock_update():
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT stock, price FROM market")
        stock_data = cursor.fetchall()
    stock_prices = {stock: price for stock, price in stock_data}
    socketio.emit("stock_update", stock_prices)

def send_faction_update():
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT faction, influence FROM faction_stats")
        faction_data = cursor.fetchall()
    faction_influence = {faction: influence for faction, influence in faction_data}
    socketio.emit("faction_update", faction_influence)

def trigger_ai_event(event_message):
    socketio.emit("ai_event", event_message)

4️⃣ (Optional) live_data_api.py

📂 Location: /telegram_mini_game/live_data_api.py
📌 Purpose: API endpoint to fetch stock prices & faction data for external applications.

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT stock, price FROM market")
        stock_data = cursor.fetchall()
    return jsonify({stock: price for stock, price in stock_data})

@app.route('/api/factions', methods=['GET'])
def get_factions():
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT faction, influence FROM faction_stats")
        faction_data = cursor.fetchall()
    return jsonify({faction: influence for faction, influence in faction_data})

if __name__ == '__main__':
    app.run(debug=True, port=5002)

📂 Existing Files That Need Modifications (3-4)

These files require changes to trigger WebSocket updates when stock prices, factions, or AI events change.

1️⃣ app.py (Modify for WebSocket Support)

📂 Location: /web_dashboard/app.py
📌 Changes Needed:
	•	Import websocket_server.py
	•	Integrate WebSocket connections into Flask app.

from websocket_server import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio.init_app(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)

2️⃣ market_engine.py (Modify for Live Stock Updates)

📂 Location: /telegram_mini_game/market_engine.py
📌 Changes Needed:
	•	Trigger send_stock_update() after price changes.

from socket_events import send_stock_update

def update_market():
    # Modify stock prices...
    send_stock_update()  # Send real-time stock update

3️⃣ bot.py (Modify for Live Market Fetching)

📂 Location: /telegram_mini_game/bot.py
📌 Changes Needed:
	•	Allow the Telegram bot to request live stock updates.

import requests

@dp.message_handler(commands=['live_market'])
async def live_market(message: types.Message):
    response = requests.get("http://127.0.0.1:5002/api/stocks")
    stocks = response.json()
    stock_list = "\n".join([f"{k}: {v}" for k, v in stocks.items()])
    await message.answer(f"📊 **Live Stock Prices:**\n{stock_list}")

4️⃣ ui.py (Modify for Live UI)

📂 Location: /telegram_mini_game/ui.py
📌 Changes Needed:
	•	Add new UI buttons for real-time updates.

def live_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📊 Live Market", callback_data="live_market"))
    return keyboard

📜 Final Summary

Type	Files	Purpose
New Files (3-4)	websocket_server.py, websocket_client.js, socket_events.py, (Optional) live_data_api.py	WebSocket server & API
Modified Files (3-4)	app.py, market_engine.py, bot.py, ui.py	Enable live updates
Total Changes	6-8 Files	Full WebSocket Integration

📜 Next Steps

🚀 When ready, follow these steps to implement real-time updates:
1️⃣ Create the new WebSocket files.
2️⃣ Modify the existing game engine & UI.
3️⃣ Test the WebSocket connections.
4️⃣ Deploy the WebSocket server alongside the Telegram bot.

🔥 This document is now ready to be stored in /docs/WebSocket_Live_Updates.md.
🚀 Would you like me to structure similar documents for future planned updates?