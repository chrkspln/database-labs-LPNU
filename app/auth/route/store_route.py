from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import store_controller
from ..model.insert_record import insert_record
from ..model.store_model import Store

store_bp = Blueprint('store', __name__, url_prefix='/store')


@store_bp.route('', methods=['GET'])
def get_all_stores() -> Response:
    """
    Get all stores
    ---
    tags:
      - Store
    responses:
      200:
        description: List of all stores
        schema:
          type: array
          items:
            type: object
    """
    return make_response(jsonify(store_controller.find_all()), HTTPStatus.OK)


@store_bp.route('', methods=['POST'])
def create_store() -> Response:
    """
    Create a new store
    ---
    tags:
      - Store
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            address:
              type: string
    responses:
      201:
        description: Store created
        schema:
          type: object
      400:
        description: Invalid input
    """
    content = request.get_json()
    store = Store.create_from_dto(content)
    store_controller.create(store)
    return make_response(jsonify(store.put_into_dto()), HTTPStatus.CREATED)


@store_bp.route('/<int:store_id>', methods=['GET'])
def get_store(store_id: int) -> Response:
    """
    Get a store by ID
    ---
    tags:
      - Store
    parameters:
      - in: path
        name: store_id
        type: integer
        required: true
        description: ID of the store
    responses:
      200:
        description: Store object
        schema:
          type: object
      404:
        description: Store not found
    """
    return make_response(jsonify(store_controller.find_by_id(store_id)), HTTPStatus.OK)


@store_bp.route('/<int:store_id>', methods=['PUT'])
def update_store(store_id: int) -> Response:
    """
    Replace an existing store by ID
    ---
    tags:
      - Store
    consumes:
      - application/json
    parameters:
      - in: path
        name: store_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            address:
              type: string
    responses:
      200:
        description: Store updated
      400:
        description: Invalid input
      404:
        description: Store not found
    """
    content = request.get_json()
    store = Store.create_from_dto(content)
    store_controller.update(store_id, store)
    return make_response("Store updated", HTTPStatus.OK)


@store_bp.route('/<int:store_id>', methods=['PATCH'])
def patch_store(store_id: int) -> Response:
    """
    Partially update a store by ID
    ---
    tags:
      - Store
    consumes:
      - application/json
    parameters:
      - in: path
        name: store_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Fields to update
    responses:
      200:
        description: Store patched
      400:
        description: Invalid input
      404:
        description: Store not found
    """
    content = request.get_json()
    store_controller.patch(store_id, content)
    return make_response("Store updated", HTTPStatus.OK)


@store_bp.route('/<int:store_id>', methods=['DELETE'])
def delete_store(store_id: int) -> Response:
    """
    Delete a store by ID
    ---
    tags:
      - Store
    parameters:
      - in: path
        name: store_id
        type: integer
        required: true
    responses:
      200:
        description: Store deleted
      404:
        description: Store not found
    """
    store_controller.delete(store_id)
    return make_response("Store deleted", HTTPStatus.OK)


@store_bp.route('/parametrized', methods=['POST'])
def insert_store_record() -> Response:
    """
    Insert a parametrized Store record
    ---
    tags:
      - Store
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Arbitrary parameters for inserting a Store record
    responses:
      201:
        description: Record inserted
      400:
        description: Invalid parameters
    """
    return insert_record(Store, request.get_json())
