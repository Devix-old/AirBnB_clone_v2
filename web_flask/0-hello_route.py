#!/usr/bin/python3
"""
Flask Web App: Simple route displaying "Hello HBNB!" on 0.0.0.0:5000.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route: /  Returns: str: Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
