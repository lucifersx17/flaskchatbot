from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response  # This imports the chatbot.py file

app = Flask(__name__)

# Route for home page (description page)
@app.route('/')
def description():
    return render_template('description.html')  # First page (Description)

# Route for login page
@app.route('/login')
def login():
    return render_template('login.html')  # Second page (Login)

# Route for the chatbot page (chat interface)
@app.route('/chat')
def chat_page():
    return render_template('index.html')  # Chat interface for users

# Route to handle chat message sending
@app.route('/send_message', methods=['POST'])
def chat():
    user_message = request.json.get('message')  # Get user input from JSON request
    if not user_message:
        return jsonify({'reply': "Please enter a message!"})  # Handle empty input
    bot_reply = chatbot_response(user_message)  # Process message using chatbot logic
    return jsonify({'reply': bot_reply})  # Return chatbot response


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)