import sqlite3

# Connect to database (creates chatbot.db if it doesn't exist)
conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()

# Create a table to store question-response pairs
cursor.execute('''
CREATE TABLE IF NOT EXISTS responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT NOT NULL,
    response TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Database and table created successfully.")