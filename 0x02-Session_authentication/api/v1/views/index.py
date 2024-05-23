#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ Return a 401 Unauthorized error

    This view is used when the user is not authorized
    to access a protected resource. The user will
    receive a 401 error with a description of 'Unauthorized'.

    Returns:
      str: A JSON string with a 401 error and
      'Unauthorized' as the description.
    """
    abort(401, description='Unauthorized')


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ Return a 403 Forbidden error

    This view is used when the user is not authorized
    to access a protected resource. The user will
    receive a 403 error with a description of 'Forbidden'.

    Returns:
      str: A JSON string with a 403 error and
      'Forbidden' as the description.
    """
    abort(403, description='Forbidden')


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
