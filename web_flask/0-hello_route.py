#!/usr/bin/python3
"""
Starts Flask Web App
Listens on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
