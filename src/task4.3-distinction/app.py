import os

from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def index():
    environment = os.getenv("APP_ENV", "Development")
    message = os.getenv("APP_MESSAGE", "Application is running successfully")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Docker Deployment Status</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 640px; margin: 80px auto; padding: 24px; }}
    main {{ border: 1px solid #ddd; border-radius: 8px; padding: 28px; }}
    .status {{ color: #16794b; font-weight: bold; }}
  </style>
</head>
<body>
  <main>
    <h1>Docker Deployment Status</h1>
    <p class="status">{message}</p>
    <p>Environment: {environment}</p>
  </main>
</body>
</html>"""


@app.get("/health")
def health():
    return jsonify(status="healthy")

