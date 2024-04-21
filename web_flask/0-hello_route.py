#!/usr/bin/python3
"""Flask Web
Listens on 0.0.0.0:5000
Route '/' Displays Hello HBNB
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
