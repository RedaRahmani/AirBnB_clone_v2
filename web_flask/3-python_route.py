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
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ c documentation """
    formatted_text = text.replace('_', ' ')
    response_text = f'C {formatted_text}'
    return response_text
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ python documentation """
    formatted_text = text.replace('_', ' ')
    response_text = f'python {formatted_text}'
    return response_text

if __name__ == '__main__':
    app.run(port=5000)
    app.run(host="0.0.0.0")
