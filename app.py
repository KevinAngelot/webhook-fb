from flask import Flask, request

app = Flask(__name__)
VERIFY_TOKEN = "EAAU9rjrQWXgBOZBegg6d1zbBiXNZCrfjtEPKCm3lmCq1B0iVqt9RbygMeEZC4mxGJt9rI1ngrNv3HP4wkYgIi0X88yOWg1QInPl3uBlJTHElnByCG0OfiUC3WCstnB7mZC3ZB9uBhPz8C2s4hnEuujgnV7GuiAgESPwMThEIeK5DZBb90FhZCb421a4nQ7lI7seSTKNIwZDZD"

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
