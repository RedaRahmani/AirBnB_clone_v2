#!/usr/bin/python3
""" Module documents """
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Hello():
    """ hello documentation """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb documentation """
    return "HBNB"

if __name__ == '__main__':
    app.run(port=5000)
    app.run(host="0.0.0.0")
