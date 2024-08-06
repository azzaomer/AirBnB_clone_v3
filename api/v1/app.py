#!/usr/bin/python3
"""This module establishes a Flask web server to manage
API requests.
It configures and registers the required routes to
respond to HTTP requests. The server operates on
a specified host and port, which can be customized
using environment variables.
"""

from models import storage
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(self):
    """Closes the DB connection"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    api_host = getenv("HBNB_API_HOST", "0.0.0.0")
    api_port = getenv("HBNB_API_PORT", 5000)
    app.run(host=api_host, port=api_port, threaded=True)
