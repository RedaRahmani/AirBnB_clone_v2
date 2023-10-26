#!/usr/bin/python3
"""10. States and State"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=None):
    """renders HTML template with states
    """
    states = storage.all('State')
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all('State').values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    """closes SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(port=5000)
    app.run(host="0.0.0.0")
