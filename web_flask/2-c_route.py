#!/usr/bin/python3
"""creates the first most basic flask app"""
from flask import Flask, escape, request


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ rerouting '/' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def bnb():
    """ displays hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """ displays the text after the c """
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
