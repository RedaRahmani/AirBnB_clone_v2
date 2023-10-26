#!/usr/bin/python3
"""8. List of states"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states():
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(port=5000)
    app.run(host="0.0.0.0")
