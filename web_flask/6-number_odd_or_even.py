#!/usr/bin/python3
"""
Flask Web App: Three routes displaying greetings on 0.0.0.0:5000.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route: /  Returns: str: Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route: /hbnb  Returns: str: HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Route: /c/<text>  Returns: str: C followed by the value of text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text):
    """Route: /c/<text>  Returns: str: python followed by the value of text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    """route /c/<text> """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_ever(n):
    if (n % 2 == 0):
        str = 'even'
    else:
        str = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, str=str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
