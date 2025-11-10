from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import price_controller
from ..model.insert_record import insert_record
from ..model.price_model import Price

price_bp = Blueprint('price', __name__, url_prefix='/price')


@price_bp.route('', methods=['GET'])
def get_all_prices() -> Response:
    """
    Get all prices
    ---
    tags:
      - Price
    responses:
      200:
        description: List of all prices
        schema:
          type: array
          items:
            type: object
    """
    return make_response(jsonify(price_controller.find_all()), HTTPStatus.OK)


@price_bp.route('', methods=['POST'])
def create_price() -> Response:
    """
    Create a new price
    ---
    tags:
      - Price
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            product_id:
              type: integer
            amount:
              type: number
            currency:
              type: string
    responses:
      201:
        description: Price created
        schema:
          type: object
      400:
        description: Invalid input
    """
    content = request.get_json()
    price = Price.create_from_dto(content)
    price_controller.create(price)
    return make_response(jsonify(price.put_into_dto()), HTTPStatus.CREATED)


@price_bp.route('/<int:price_id>', methods=['GET'])
def get_price(price_id: int) -> Response:
    """
    Get a price by ID
    ---
    tags:
      - Price
    parameters:
      - in: path
        name: price_id
        type: integer
        required: true
        description: ID of the price
    responses:
      200:
        description: Price object
        schema:
          type: object
      404:
        description: Price not found
    """
    return make_response(jsonify(price_controller.find_by_id(price_id)), HTTPStatus.OK)


@price_bp.route('/<int:price_id>', methods=['PUT'])
def update_price(price_id: int) -> Response:
    """
    Replace an existing price by ID
    ---
    tags:
      - Price
    consumes:
      - application/json
    parameters:
      - in: path
        name: price_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            amount:
              type: number
            currency:
              type: string
    responses:
      200:
        description: Price updated
      400:
        description: Invalid input
      404:
        description: Price not found
    """
    content = request.get_json()
    price = Price.create_from_dto(content)
    price_controller.update(price_id, price)
    return make_response("Price updated", HTTPStatus.OK)


@price_bp.route('/<int:price_id>', methods=['PATCH'])
def patch_price(price_id: int) -> Response:
    """
    Partially update a price by ID
    ---
    tags:
      - Price
    consumes:
      - application/json
    parameters:
      - in: path
        name: price_id
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
        description: Price patched
      400:
        description: Invalid input
      404:
        description: Price not found
    """
    content = request.get_json()
    price_controller.patch(price_id, content)
    return make_response("Price updated", HTTPStatus.OK)


@price_bp.route('/<int:price_id>', methods=['DELETE'])
def delete_price(price_id: int) -> Response:
    """
    Delete a price by ID
    ---
    tags:
      - Price
    parameters:
      - in: path
        name: price_id
        type: integer
        required: true
    responses:
      200:
        description: Price deleted
      404:
        description: Price not found
    """
    price_controller.delete(price_id)
    return make_response("Price deleted", HTTPStatus.OK)


@price_bp.route('/parametrized', methods=['POST'])
def insert_price_record() -> Response:
    """
    Insert a parametrized Price record
    ---
    tags:
      - Price
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Arbitrary parameters for inserting a Price record
    responses:
      201:
        description: Record inserted
      400:
        description: Invalid parameters
    """
    return insert_record(Price, request.get_json())
