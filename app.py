from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Invalid input"}), 400
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
