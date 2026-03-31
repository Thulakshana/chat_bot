from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# API key
API_KEY = "AIzaSyAR3dgzwSk7byUHNOT10yrGSE9b61c92ws"  
client = genai.Client(api_key=API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
