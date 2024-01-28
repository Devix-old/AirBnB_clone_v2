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


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page with information about a specific State."""
    state = None
    states = storage.all(State).values()
    for s in states:
        if s.id == id:
            state = s
    if state:
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', not_found=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
