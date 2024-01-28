#!/usr/bin/python3
"""
Flask Web App: Two routes displaying greetings on 0.0.0.0:5000.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route: /  Returns: str: Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route: /hbnb  Returns: str: HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)