✅ Steps to Run Arcane Empires on GitHub Codespaces

Since you already have a bot set up (but not fully working), follow these steps to migrate everything and ensure it runs properly.

📌 1. Set Up Codespaces Environment

1️⃣ Open GitHub Repo → Click “Code” > “Open with Codespaces”
2️⃣ Create a New Codespace
3️⃣ Install Dependencies (Run in Codespaces terminal):

pip install -r requirements.txt

📌 2. Remove Old, Non-Functional Bot Files

1️⃣ Check the existing bot files → Identify outdated/unused scripts.
2️⃣ Backup if necessary, then delete old files in /telegram_mini_game/.

rm -rf /telegram_mini_game/old_bot_files.py

📌 3. Pull the Latest Files from Your Repo

1️⃣ Run the following in Codespaces terminal:

git pull origin main

2️⃣ Check for missing files (compare with /docs/ folder).

📌 4. Initialize the Database

1️⃣ Run this once to create/update the database:

python -c "import database; database.init_db()"

📌 5. Run & Test the Telegram Bot

1️⃣ Start the bot inside Codespaces:

python bot.py

2️⃣ Test in Telegram:
	•	Send /start to the bot.
	•	Try /trade or /joinFaction to check interactions.
	•	If the bot doesn’t respond, check logs for errors.

📌 6. Start the Web Dashboard (If Needed)

1️⃣ Navigate to the Web Dashboard folder:

cd web_dashboard

2️⃣ Run the Flask app:

python app.py

3️⃣ Open in browser:
	•	Codespaces gives a public URL → Click on the preview link.

📌 7. Enable Live Updates (Optional for Later)

1️⃣ Start WebSocket Server (For real-time market updates)

python websocket_server.py

📌 8. Debugging & Fixing Issues

1️⃣ Check logs for errors:

tail -f logs/bot.log

2️⃣ Manually test database queries:

sqlite3 observer_protocol.db

📌 9. Push Any Fixes Back to GitHub

1️⃣ After fixing or updating anything, commit and push:

git add .
git commit -m "Fixed bot issues & updated files"
git push origin main

✅ Final Checklist Before Running Live

✔ Deleted old bot files
✔ Pulled latest repo updates
✔ Installed dependencies
✔ Initialized the database
✔ Ran & tested the Telegram bot
✔ Ran the Web Dashboard (if needed)
✔ Checked for errors and fixed issues

🚀 Let me know where you get stuck, and I’ll help debug!