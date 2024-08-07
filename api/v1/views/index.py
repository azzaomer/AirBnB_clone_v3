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
from models import storage
from models.engine.db_storage import classes

classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status')
def return_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/status', strict_slashes=False)
def count_obj():
    """
    Retrieves the number of each objects by type
    """
    count_objects = {}
    for cls in classes:
        count_objects[cls] = storage.count(classes[cls])
    return jsonify(count_objects)
