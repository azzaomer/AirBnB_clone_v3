#!/usr/bin/python3
"""This module establishes a Flask web server to manage
API requests.
It configures and registers the required routes to
respond to HTTP requests. The server operates on
a specified host and port, which can be customized
using environment variables.
"""

from flask import Blueprint, Flask, jsonify
from models import storage
from os import getenv
import sys


app = Flask(__name__)
from api.v1.views import app_views
app.register_blueprint(app_views)

api_host = getenv("HBNB_API_HOST", "0.0.0.0")
api_port = getenv("HBNB_API_PORT", 5000)


@app.teardown_appcontext
def teardown(self):
    """Closes the DB connection"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=api_host, port=api_port, threaded=True)
