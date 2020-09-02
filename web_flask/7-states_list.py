#!/usr/bin/python3
"""creates the first most basic flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ remove current sqlalchemy session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ displays hbnb """
    l = storage.all(State)
    return render_template("7-states_list.html", l=l)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
