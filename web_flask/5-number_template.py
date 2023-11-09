#!/usr/bin/python3
""" Initializes an initial flask web app

Listen: 0.0.0.0, port 5000
Route:
    /: Display 'Hello HBNB!'
    /hbnb: Display 'HBNB'
    /c/<text>: Diplay 'c ' followed by value of text
    /python/<text>: Display Python + text, with default
    /number/<int: n>: If n is int, display <n> is a number
    /number_template/<int: n>: Display an HTML page if <n> is an int
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Display 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_bnb():
    """ Displays only 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display c + value of text """
    new_text = text.replace('_', " ")
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Display python + value of text """
    new_text = text.replace('_', " ")
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Checks if n is a an int,
    then displays 'n is a number' if it is """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display a template HTML page only if <n> is an int """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
