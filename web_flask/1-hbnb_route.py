from flask import Flask
"""
Starts Flask Web App
Routes '/' => “Hello HBNB!” and
       '/hbnb' => “HBNB”
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
