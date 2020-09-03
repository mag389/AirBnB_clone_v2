#!/usr/bin/python3
"""creates the first most basic flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ remove current sqlalchemy session """
    storage.close()


@app.route('/states', strict_slashes=False)
def just_states():
    """ display just the states """
    states = storage.all(State)
    return render_template("9-states.html", states=states, just=1)


@app.route('/states/<id>', strict_slashes=False)
def state_list(id=None):
    """ displays hbnb """
    states = storage.all(State)
    cities = storage.all(City)
    exists = 0
    state = None
    for v in states.values():
        if id == v.id:
            exists = 1
            state = v
    return render_template("9-states.html", states=states,
                           cities=cities, just=0, exists=exists,
                           state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
