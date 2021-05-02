#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ starts a Flask web application """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ display “C ” followed by the value of the text variable"""
    if text:
        new_text = text.replace("_", " ")
        return 'C {}'.format(new_text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text=None):
    """ display 'Python' followed by the value of the text variable """
    if text is None:
        text = 'is cool'
    else:
        text = text.replace("_", " ")
        return ('Python' + ' ' + text)


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_a_number(n):
    """ display “n is a number” only if n is an integer """
    if isinstance(n, int):
        return ('{:d} is a number'.format(n))
    else:
        return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
