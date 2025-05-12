from flask import Flask, request
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if any(keyword.lower() in text.lower() for keyword in ["пончик", "namelaka", "milk bar", "idealist"]):
        reply = "Боксик замечен! Проверь приложение Experience."
    else:
        reply = "Ожидаю появления боксиков..."

    requests.post(URL, json={
        "chat_id": chat_id,
        "text": reply
    })
    return {"ok": True}

@app.route("/")
def index():
    return "Bot is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))