from flask import Flask, render_template, request, jsonify
from chat import get_response, bot_name

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_text = request.json.get("msg")
    response = get_response(user_text)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)