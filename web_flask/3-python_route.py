#!/usr/bin/python3
"""Start Flask App
Listens on 0.0.0.0:5000
Routes:
    '/' - display “Hello HBNB!”
    '/hbnb' - display “HBNB”
    '/c/<text>' - display “C ” followed by the value of the text
    '/python/<text>' - 
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


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Displays C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % exit


@app.route('/python/<string:text>', strict_slashes=False)
def p_text(text="is cool"):
    """Displays Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
