#!/usr/bin/python3
""" Initializes an initial flask web app

Listen: 0.0.0.0, port 5000
Route:
    /: Display 'Hello HBNB!'
    /hbnb: Display 'HBNB'
    /c/<text>: Diplay 'c ' followed by value of text
    /python/<text>: Display Python + text, with default
"""
from flask import Flask

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


@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Display python + value of text """
    new_text = text.replace('_', " ")
    return "Python {}".format(new_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
