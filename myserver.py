import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

def run():
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting web server on port {port}")
    app.run(host="0.0.0.0", port=port)

def server_on():
    t = Thread(target=run, daemon=True)
    t.start()