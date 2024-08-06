#!/usr/bin/python3
"""Retrieves the list of all Amenity objects:
"""

from flask import abort, request, jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from datetime import datetime
from models.engine.db_storage import classes


@app_views.route('/amenities/', methods=['GET'],
                 strict_slashes=False)
def get_aminities():
    """Retrieves aall Aminity objects"""
    all_amenities = []
    amenities_obj = storage.all(Amenity).values()
    for obj in amenities_obj:
        all_amenities.append(obj.to_dict())
    return jsonify(all_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves a spcific amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_amenity(amenity_id):
    """Delete an amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        return ({})
    else:
        abort(404)


@app_views.route('/amenities/', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    '''Creates an Amenity'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    amenities = []
    new_amenity = Amenity(name=request.json['name'])
    storage.new(new_amenity)
    storage.save()
    amenities.append(new_amenity.to_dict())
    return jsonify(amenities[0]), 201


@app_views.route('/amenities/<amenity_id>',strict_slashes=False,
                 methods=['PUT'])
def updates_amenity(amenity_id):
    '''Updates an Amenity object'''
    all_amenities = storage.all("Amenity").values()
    amenity = [obj.to_dict() for obj in all_amenities
               if obj.id == amenity_id]
    if amenity == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    amenity[0]['name'] = request.json['name']
    for obj in all_amenities:
        if obj.id == amenity_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(amenity[0]), 200
