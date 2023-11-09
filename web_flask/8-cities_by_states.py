#!/usr/bin/python3
""" Initializes an initial flask web app

Listen: 0.0.0.0, port 5000
Route:
    /states_list: Displays an HTML page listing states existing in storage
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ Display an HTML page listing states existing in storage """
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Ends the existing SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
