import sqlite3

connection = sqlite3.connect('database.db')

connection.executescript("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL
);
""")

connection.commit()
connection.close()

print("Database initialized successfully.")
