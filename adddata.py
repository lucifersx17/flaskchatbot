import sqlite3

# Connect to the database
conn = sqlite3.connect('chatbot.db')
cursor = conn.cursor()

# Insert data into the responses table
responses = [
    ("hello", "Hi there! How can I help you?"),
    ("how are you", "I'm just a bot, but I'm doing great! How about you?"),
    ("bye", "Goodbye! Have a great day!"),
    ("your name", "I am a chatbot Raiden created using Flask."),
    ("hi", "Hi there! How can I help you?"),
    ("nice", "You're welcome! Is there anything I can help with?"),
    ("subjects", "s1.php, s2.rdbms, s3.python. Use code (e.g. s1) to choose a subject!"),
    ("s1", "6) state management"),
    ("state management", "topics | 1.cookies, 2.session, 3.difference between cookie and session, use topic name for further query!"),
    ("cookie", "Identified a user"),
    ("s2", "query"),
    ("query", "Choose for requirement: update, select, delete, modify"),
    ("update", "UPDATE students SET age = 19 WHERE name = 'John';"),
    ("select", "SELECT * FROM students;"),
    ("delete", "DELETE FROM students WHERE name = 'John';"),
    ("modify", "ALTER TABLE students MODIFY age INT;")
]

# Insert each response pair into the table
cursor.executemany('''
INSERT INTO responses (keyword, response) VALUES (?, ?)
''', responses)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully!")