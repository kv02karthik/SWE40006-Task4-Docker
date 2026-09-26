import os

from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def index():
    return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Task 4.2 Credit App</title>
    <style>
      body { font-family: Arial, sans-serif; max-width: 640px; margin: 80px auto; padding: 0 20px; }
      h1 { margin-bottom: 8px; }
      p { color: #444; }
    </style>
  </head>
  <body>
    <h1>Task 4.2 Credit App</h1>
    <p>This Python Flask application is running inside a Docker container.</p>
  </body>
</html>"""


@app.get("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
