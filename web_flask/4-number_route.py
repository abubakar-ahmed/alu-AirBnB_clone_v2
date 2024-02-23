#!/usr/bin/python3
"""
This is a simple Flask web application.

It defines four routes:
- Route for the root URL ("/") that displays "Hello HBNB!"
- Route for "/hbnb" that displays "HBNB"
- Route for "/c/<text>" that displays "C <text>" where <text> can be any string
- Route for "/python/(<text>)" that displays "Python <text>"
- Route for the "/number/<n>" URL.

Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Route for the root URL ("/")."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Route for the "/hbnb" URL."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Route for the "/c/<text>" URL."""
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Route for the "/python/" and "/python/<text>" URLs."""
    return "Python %s" % text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Route for the "/number/<n>" URL."""
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
