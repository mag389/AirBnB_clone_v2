#!/usr/bin/python3
"""creates the first most basic flask app"""
from flask import Flask, render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ display python with dynamic and default """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ displays the number(if it's an int) """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """display an html page onlu if n is an integer """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddeven(n):
    """ displays html with varying info """
    if (n % 2) is 0:
        stri = "{} is even".format(n)
    else:
        stri = "{} is odd".format(n)
    return render_template("6-number_odd_or_even.html", stri=stri)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
