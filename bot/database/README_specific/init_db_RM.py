Enhancing init_db.py for Scalability & Stability

Your current init_db.py script initializes multiple database tables correctly, but I recommend a few key improvements for better organization, error handling, and logging.

✅ Key Enhancements

✔ Added Error Handling
	•	Ensures that database initialization does not break the script if an error occurs.

✔ Logs Initialization Status
	•	Provides clear feedback on which tables successfully initialized.

✔ Dynamically Imports Future Database Modules
	•	Allows easy expansion without manually adding new imports.
	
	—-
	
	Key Improvements Explained

🔹 🛠 Database Directory Creation
	•	os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
	•	Ensures the database folder exists before initializing.

🔹 ✅ Logging System
	•	Saves logs to "logs/database_init.log" so you can track initialization errors.

🔹 🚀 Dynamic Expansion
	•	If you add new database modules (e.g., ai_traders_db.py), simply add it to init_db.py without refactoring everything.

🔹 Next Steps?
	•	Run the script with:

python bot/database/init_db.py


	•	Check logs under logs/database_init.log to confirm successful initialization.
	