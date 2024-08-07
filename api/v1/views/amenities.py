#!/usr/bin/python3
"""Retrieves the list of all Amenity objects:
"""

from flask import abort, request, jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity


@app_views.route('/amenities/', strict_slashes=False)
def get_aminities():
    """Retrieves aall Aminity objects"""
    all_amenities = []
    amenities_obj = storage.all(Amenity).items()
    for key, value in amenities_obj:
        all_amenities.append(value.to_dict())
    return jsonify(all_amenities)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
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
        return ({}), 200
    else:
        return abort(404)


@app_views.route('/amenities/', methods=['POST'],
                 strict_slashes=False)
def create_amenity():
    '''Creates an Amenity'''
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')
    amenity_data = request.get_json()

    if 'name' not in amenity_data:
        return abort(400, 'Missing name')
    amenity = Amenity(**amenity_data)

    amenity.save()
    return jsonify(amenity_data.to_dict()), 200


@app_views.route('/amenities/<amenity_id>',strict_slashes=False,
                 methods=['PUT'])
def updates_amenity(amenity_id):
    '''Updates an Amenity object'''
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')
    amenity_data = request.get_json()

    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        keys = ['id', 'created_at', 'updated_at']
        for key, value in amenity_data.items():
            if key not in keys:
                setattr(amenity, key, value)
        amenity.save()
        return jsonify(amenity.to_dict()), 200
    else:
        return abort(404)