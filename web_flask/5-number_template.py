#!/usr/bin/python3
""" Module documents """
from flask import Flask
from flask import render_template
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
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ python doc """
    return 'Python {}'.format(text.replace("_", " "))
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ c documentation """
    return f'{n} is a number'
@app.route('/number_template/<n>')
def number_template(n):
    """ python doc """
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(port=5000)
    app.run(host="0.0.0.0")
