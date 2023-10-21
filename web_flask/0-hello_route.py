#!/usr/bin/python3
""" Module documents """
from flask import Flask
app = Flask(__name__)

@app.route('/about', strict_slashes=False)
def Hello():
    """ hello documentation """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(port=5000)
    app.run(host="0.0.0.0")

