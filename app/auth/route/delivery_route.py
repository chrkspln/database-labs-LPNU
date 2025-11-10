from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import delivery_controller
from ..model.delivery_model import Delivery
from ..model.insert_record import insert_record

delivery_bp = Blueprint('delivery', __name__, url_prefix='/delivery')


@delivery_bp.route('', methods=['GET'])
def get_all_deliveries() -> Response:
    """
    Get all deliveries
    ---
    tags:
      - Delivery
    responses:
      200:
        description: List of all deliveries
        schema:
          type: array
          items:
            type: object
    """
    return make_response(jsonify(delivery_controller.find_all()), HTTPStatus.OK)


@delivery_bp.route('', methods=['POST'])
def create_delivery() -> Response:
    """
    Create a new delivery
    ---
    tags:
      - Delivery
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            store_id:
              type: integer
            address:
              type: string
            urgency_type_id:
              type: integer
    responses:
      201:
        description: Delivery created
        schema:
          type: object
      400:
        description: Invalid input
    """
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.CREATED)


@delivery_bp.route('/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id: int) -> Response:
    """
    Get a delivery by ID
    ---
    tags:
      - Delivery
    parameters:
      - in: path
        name: delivery_id
        type: integer
        required: true
        description: ID of the delivery
    responses:
      200:
        description: Delivery object
        schema:
          type: object
      404:
        description: Delivery not found
    """
    return make_response(jsonify(delivery_controller.find_by_id(delivery_id)), HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id: int) -> Response:
    """
    Replace an existing delivery by ID
    ---
    tags:
      - Delivery
    consumes:
      - application/json
    parameters:
      - in: path
        name: delivery_id
        type: integer
        required: true
        description: ID of the delivery to replace
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            store_id:
              type: integer
            address:
              type: string
            urgency_type_id:
              type: integer
    responses:
      200:
        description: Delivery updated
      400:
        description: Invalid input
      404:
        description: Delivery not found
    """
    content = request.get_json()
    assert content is not None
    delivery = Delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['PATCH'])
def patch_delivery(delivery_id: int) -> Response:
    """
    Partially update a delivery by ID
    ---
    tags:
      - Delivery
    consumes:
      - application/json
    parameters:
      - in: path
        name: delivery_id
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
        description: Delivery patched
      400:
        description: Invalid input
      404:
        description: Delivery not found
    """
    content = request.get_json()
    delivery_controller.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id: int) -> Response:
    """
    Delete a delivery by ID
    ---
    tags:
      - Delivery
    parameters:
      - in: path
        name: delivery_id
        type: integer
        required: true
    responses:
      200:
        description: Delivery deleted
      404:
        description: Delivery not found
      500:
        description: Internal server error
    """
    try:
        delivery_controller.delete(delivery_id)
        return make_response("Delivery deleted", HTTPStatus.OK)
    except Exception as e:
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR)


@delivery_bp.route('/parametrized', methods=['POST'])
def insert_delivery_record() -> Response:
    """
    Insert a parametrized Delivery record
    ---
    tags:
      - Delivery
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Arbitrary parameters for inserting a Delivery record
    responses:
      201:
        description: Record inserted
      400:
        description: Invalid parameters
    """
    return insert_record(Delivery, request.get_json())


@delivery_bp.route('/new_link', methods=['POST'])
def add_link() -> Response:
    """
    Add a new Delivery link between store and urgency type
    ---
    tags:
      - Delivery
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - store_name
            - urgency_type_name
          properties:
            store_name:
              type: string
            urgency_type_name:
              type: string
    responses:
      201:
        description: New link created
        schema:
          type: object
      400:
        description: Bad request (e.g. missing or invalid names)
    """
    content = request.get_json()
    store_name = content['store_name']
    urgency_type_name = content['urgency_type_name']
    try:
        new_link = Delivery.add_link(store_name, urgency_type_name)
        return make_response(jsonify(new_link.put_into_dto()), HTTPStatus.CREATED)
    except ValueError as e:
        return make_response(str(e), HTTPStatus.BAD_REQUEST)
