#!/usr/bin/python3
"""Flask App
Listens on 0.0.0.0:5000
Routes:
    '/' display Hello HBNB
    '/hbnb' display HBNB
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


if __name___ == "__main__":
    app.run(host="0.0.0.0")
