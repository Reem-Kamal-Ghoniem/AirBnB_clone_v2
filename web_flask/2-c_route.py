#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    return return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
