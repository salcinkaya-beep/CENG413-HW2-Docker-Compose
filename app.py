import os

import redis
from flask import Flask, jsonify

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
)


@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello from Selin!")
    return jsonify(message=message)


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/info")
def info():
    return jsonify(course="CENG413", author="Selin Alcinkaya")


@app.route("/counter")
def counter():
    count = redis_client.incr("visits")
    return jsonify(visits=count)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
