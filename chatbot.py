import sqlite3
from rapidfuzz import fuzz, process

def chatbot_response(user_input):
    # Connect to the database
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Fetch all keywords from the database
    cursor.execute("SELECT keyword FROM responses")
    keywords = [row[0] for row in cursor.fetchall()]

    # Try exact/sub-string match first
    for keyword in keywords:
        if keyword in user_input:
            # Fetch the corresponding response
            cursor.execute("SELECT response FROM responses WHERE keyword = ?", (keyword,))
            response = cursor.fetchone()[0]
            conn.close()
            return response

    # Fuzzy match using rapidfuzz
    best_match = process.extractOne(user_input, keywords, scorer=fuzz.partial_ratio)
    if best_match and best_match[1] > 70:  # confidence threshold
        # Fetch the corresponding response
        cursor.execute("SELECT response FROM responses WHERE keyword = ?", (best_match[0],))
        response = cursor.fetchone()[0]
        conn.close()
        return response

    # If no match is found
    conn.close()
    return "I'm not sure how to respond to that."