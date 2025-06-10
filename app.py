from flask import Flask, request

app = Flask(__name__)
VERIFY_TOKEN = "Mytoken_03"

@app.route("/")
def index():
    return "Webhook opérationnel", 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        return "Erreur : token invalide", 403
    elif request.method == "POST":
        data = request.json
        print("Reçu :", data)
        return "Message reçu", 200
