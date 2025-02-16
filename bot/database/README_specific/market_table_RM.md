Key Enhancements

✔ Default Stocks & Initial Prices
	•	Ensures that the market starts with a baseline set of stocks.

✔ Logging for Debugging
	•	Tracks successful initialization and potential errors.

✔ Failsafe Mechanism
	•	Prevents duplicate entries if the table is already populated.
	
	——
	
	Key Improvements Explained

🔹 📌 Default Stock Listings
	•	Ensures the market starts with realistic stock values rather than an empty table.

🔹 ✅ Prevents Duplicate Entries
	•	If the table already contains data, it won’t overwrite it.

🔹 🛠 Logs Initialization
	•	Stores logs in "logs/market_init.log" to help debug database setup issues.

🔹 Next Steps?
	•	Run init_db.py again to confirm updates:

python bot/database/init_db.py


	•	Check logs under logs/market_init.log to verify stock entries.