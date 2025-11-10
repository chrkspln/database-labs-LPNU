from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import os

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login and get JWT token
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: JWT token
        schema:
          type: object
          properties:
            access_token:
              type: string
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == os.environ.get('ADMIN_USER') and password == os.environ.get('ADMIN_PASS'):
        access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401
