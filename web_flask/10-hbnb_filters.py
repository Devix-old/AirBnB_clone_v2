#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display hbnb_filters page."""
    states = storage.all(State).values()
    if states:
        return render_template('10-hbnb_filters.html', states=states)
    else:
        return render_template('10-hbnb_filters.html', not_found=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
