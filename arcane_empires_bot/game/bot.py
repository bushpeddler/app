"""
bot.py - Main bot logic for Observer Protocol Mini Game

This version preserves all original features while improving structure for scalability.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
import game_logic
import ui
import database

# Initialize bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 🎮 Start Game Command
@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    """Starts the game and presents the main menu."""
    database.add_player(message.from_user.id, message.from_user.username)
    await message.answer(
        "💠 Welcome to Observer Protocol! The market is unpredictable, and AI is watching.\n\n"
        "Choose an action:",
        reply_markup=ui.main_menu()
    )

# 📈 Trade System
@dp.callback_query_handler(lambda call: call.data == "trade")
async def handle_trade(call: types.CallbackQuery):
    result = game_logic.trade(call.from_user.id, "BTC", 5)  # Example trade
    await call.message.edit_text(result, reply_markup=ui.trading_menu())

# 🔓 AI Hacking System
@dp.callback_query_handler(lambda call: call.data == "hackAI")
async def handle_hack_ai(call: types.CallbackQuery):
    result = game_logic.hack_ai(call.from_user.id)
    await call.message.edit_text(result, reply_markup=ui.ai_hacking_menu())

# 🏴 Join Faction System
@dp.callback_query_handler(lambda call: call.data == "joinFaction")
async def handle_faction_selection(call: types.CallbackQuery):
    """Allows the player to choose a faction."""
    await call.message.edit_text("🏴 Choose a faction:", reply_markup=ui.faction_menu())

@dp.callback_query_handler(lambda call: call.data in ["Syndicate", "Technocrats", "Decentralists"])
async def handle_join_faction(call: types.CallbackQuery):
    """Handles faction joining process."""
    game_logic.join_faction(call.from_user.id, call.data)
    await call.message.edit_text(f"✅ You have joined **{call.data}**!", reply_markup=ui.main_menu())

# 📊 Market Trends
@dp.callback_query_handler(lambda call: call.data == "market_trends")
async def handle_market_trends(call: types.CallbackQuery):
    """Displays current market trends and AI predictions."""
    market_data = game_logic.get_market_data()  # Example function for market trends
    await call.message.edit_text(f"📊 *Market Trends:*\n{market_data}", reply_markup=ui.market_overview_menu())

# 🚀 Bot Initialization
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    database.init_db()  # Ensure database is initialized
    executor.start_polling(dp, skip_updates=True)