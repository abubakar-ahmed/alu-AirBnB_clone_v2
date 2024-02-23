#!/usr/bin/python3
"""
This is a simple Flask web application.

It defines a single route for the root URL ("/") and displays "Hello HBNB!".

Requirements:
- Your web application must be listening on 0.0.0.0, port 5000
- You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Route for the root URL ("/").

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
