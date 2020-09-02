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


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """ displays hbnb """
    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
