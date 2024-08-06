#!/usr/bin/python3
"""Routes Handling for the App.

This module contains route handlers for the Flask app.
It defines the various routes and their corresponding functions
to handle incoming HTTP requests.
Each route is responsible for a specific endpoint or functionality of the app.

Routes:
- GET /status: Returns the status of the API.
- GET /stats: Retrieves the number of each object by type.
"""
from api.v1.views import app_views
from flask import Response, jsonify


@app_views.route('/status')
def return_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
